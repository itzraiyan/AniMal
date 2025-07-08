import requests
from config import constants
from utils.cli_helpers import print_error

def get_mal_id_from_username(username):
    if not username:
        return "0"
    
    url = constants.MAL_USER_ID_API.format(username=username)
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            return str(data["data"]["id"])
        else:
            print_error(f"Could not fetch MAL user ID for '{username}' (HTTP {resp.status_code})")
    except Exception as e:
        print_error(f"Could not fetch MAL user ID: {e}")
    return "0"
