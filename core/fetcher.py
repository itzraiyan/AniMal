import requests
from config.constants import ANILIST_API
from utils.cli_helpers import print_error

def get_user_id(username):
    query = '''
    query ($name: String) {
        User(search: $name) { id }
    }
    '''
    variables = {'name': username}
    resp = requests.post(ANILIST_API, json={'query': query, 'variables': variables})
    if resp.status_code == 200:
        return resp.json()['data']['User']['id']
    print_error(f"User '{username}' not found")
    exit(1)

def fetch_list(user_id, media_type):
    query = '''
    query ($userId: Int, $type: MediaType) {
        MediaListCollection(userId: $userId, type: $type) {
            lists { entries {
                status score(format: POINT_10) progress progressVolumes
                notes private
                startedAt { year month day }
                completedAt { year month day }
                media { id idMal episodes chapters volumes title { romaji } }
            }}
        }
    }
    '''
    variables = {'userId': user_id, 'type': media_type}
    resp = requests.post(ANILIST_API, json={'query': query, 'variables': variables})
    if resp.status_code == 200:
        lists = resp.json()["data"]["MediaListCollection"]["lists"]
        return [entry for lst in lists for entry in lst["entries"]]
    print_error(f"Failed to fetch {media_type} list")
    exit(1)
