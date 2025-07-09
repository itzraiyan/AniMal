# core/fetcher.py
import requests
import sys
from config import constants
from utils.cli_helpers import print_error, print_success

def get_user_id(username, token=None):
    query = '''
    query ($name: String) {
        User(search: $name) { id }
    }
    '''
    variables = {'name': username}
    headers = {}
    if token:
        headers['Authorization'] = f'Bearer {token}'
    resp = requests.post(constants.ANILIST_API, json={'query': query, 'variables': variables}, headers=headers)
    if resp.status_code == 200:
        data = resp.json()
        uid = data.get('data', {}).get('User', {}).get('id')
        if uid:
            return uid
    print_error(f"Unable to find AniList user '{username}'.")
    sys.exit(1)

def fetch_list(user_id, media_type, token=None):
    query = '''
    query ($userId: Int, $type: MediaType) {
        MediaListCollection(userId: $userId, type: $type) {
            lists {
                entries {
                    status
                    score(format: POINT_10)
                    progress
                    progressVolumes
                    notes
                    private
                    startedAt { year month day }
                    completedAt { year month day }
                    media {
                        id
                        idMal
                        episodes
                        chapters
                        volumes
                        title { romaji }
                    }
                }
            }
        }
    }
    '''
    variables = {'userId': user_id, 'type': media_type}
    headers = {}
    if token:
        headers['Authorization'] = f'Bearer {token}'
    resp = requests.post(constants.ANILIST_API, json={'query': query, 'variables': variables}, headers=headers)
    if resp.status_code == 200:
        data = resp.json()
        lists = data["data"]["MediaListCollection"]["lists"]
        entries = [entry for lst in lists for entry in lst["entries"]]
        return entries
    print_error(f"Failed to fetch {media_type} list from AniList.")
    sys.exit(1)
