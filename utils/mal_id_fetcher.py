import requests
from config.constants import MAL_USER_ID_API
from utils.cli_helpers import print_error

def get_mal_id_from_username(username):
    if not username: return "0"
    try:
        response = requests.get(MAL_USER_ID_API.format(username=username))
        if response.status_code == 200:
            return str(response.json()["data"]["id"])
    except Exception as e:
        print_error(f"MAL ID fetch failed: {str(e)}")
    return "0"
