import os
import re
from utils.io_helpers import ensure_output_dir
from utils.cli_helpers import print_banner, print_outro, print_info, print_success, prompt_boxed, boxed_text
from utils.mal_id_fetcher import get_mal_id_from_username
from core.fetcher import get_user_id, fetch_list
from core.utils import show_status_grid, get_status_codes, filter_entries, print_stats
from core.xml_builder import write_xml

FIELD_HELP = {
    "username": (
        "AniList Username Help:\n"
        "Enter your AniList username. This is used to fetch your list.\n"
        "If you don't know your AniList username, visit your AniList profile page (https://anilist.co/) and look at the URL or your profile name."
    ),
    "private_entries": (
        "Private Entries & AniList Authentication Help:\n"
        "AniList lets you mark some entries as private. To export those, you must use AniList OAuth.\n"
        "If you want to include private entries, answer 'y' at the prompt. You'll need to create an AniList Application (gets you a Client ID and Client Secret), then authorize AniMal to access your account."
    ),
    "client_id": (
        "AniList Client ID Help:\n"
        "To get your Client ID:\n"
        "1. Go to https://anilist.co/settings/developer\n"
        "2. Click 'Create New Client'.\n"
        "3. Give it a name (e.g., AniMal Exporter) and any redirect URL (e.g., https://localhost/ works).\n"
        "4. After creating, you'll see your Client ID. Copy and paste it here."
    ),
    "client_secret": (
        "AniList Client Secret Help:\n"
        "After creating your AniList App at https://anilist.co/settings/developer, copy the Client Secret (shown next to your app).\n"
        "Paste it here. Keep this secret safe!"
    ),
    "auth_url": (
        "AniList Authorization URL Help:\n"
        "Go to the following URL in your browser. Log in and authorize AniMal.\n"
        "After approving, AniList will redirect you to your specified redirect URL (e.g., https://localhost/?code=XXXX).\n"
        "Copy the FULL URL from your browser's address bar and paste it at the next prompt."
    ),
    "token_url": (
        "AniList Token Exchange Help:\n"
        "If asked for a code/token, paste the full redirected URL here (it looks like https://localhost/?code=YOUR_CODE).\n"
        "AniMal will extract the token and use it to access your private list entries."
    ),
    "mal_username": (
        "MAL Username Help:\n"
        "Optional. If you want your exported XML to include your MAL user info for best compatibility, enter your MyAnimeList username here. "
        "If you don't have a MAL account or want to skip this, just press Enter."
    ),
    "export_type": (
        "Export Type Help:\n"
        "Choose what you want to export:\n"
        "  1: Only your Anime list\n"
        "  2: Only your Manga list\n"
        "  3: Both Anime and Manga lists\n"
        "Press Enter to select the default option (3: Both)."
    ),
    "filter_status": (
        "Filter by Status Help:\n"
        "You can limit your export to only certain statuses (like completed, watching, etc).\n"
        "Type 'y' and press Enter to select which statuses to include. Type 'n' to export everything, no filter."
    ),
    "status_select": (
        "Status Selection Help:\n"
        "You can select one or more statuses to export. Use either numbers or status codes, separated by spaces or commas.\n"
        "Examples:\n"
        "  1 3 5\n"
        "  COMPLETED,DROPPED\n"
        "Available statuses:"
        "\n" + show_status_grid(width=44) +
        "Use the numbers or codes shown above."
    ),
    "filter_title": (
        "Filter by Title Substring Help:\n"
        "You can limit your export to titles that contain a certain word or phrase.\n"
        "Type 'y' and press Enter to filter by title substring, or 'n' to skip."
    ),
    "title_substring": (
        "Title Substring Help:\n"
        "Enter any word or phrase. Only entries whose titles contain this text will be exported.\n"
        "Example: If you enter 'one piece', only titles with 'one piece' in them will be included. "
        "Leave blank to export all titles."
    ),
}

def get_anilist_token_oauth():
    client_id = prompt_boxed(
        "Enter your AniList Client ID:",
        color="CYAN",
        helpmsg=FIELD_HELP["client_id"]
    )
    client_secret = prompt_boxed(
        "Enter your AniList Client Secret:",
        color="CYAN",
        helpmsg=FIELD_HELP["client_secret"]
    )
    redirect_uri = "https://localhost/"
    # Construct OAuth URL
    auth_url = (
        f"https://anilist.co/api/v2/oauth/authorize"
        f"?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
    )
    print(boxed_text(f"Go to this URL to authorize AniMal:\n{auth_url}", "MAGENTA"))
    print(boxed_text(FIELD_HELP["auth_url"], "CYAN"))
    redirected_url = prompt_boxed(
        "Paste the FULL URL you were redirected to after authorizing AniMal (it contains ?code=...):",
        color="CYAN",
        helpmsg=FIELD_HELP["token_url"]
    )
    # Extract code
    code_match = re.search(r"[?&]code=([^&]+)", redirected_url)
    if not code_match:
        print_info("Could not find ?code= in the URL. Please re-try the OAuth flow.")
        return ""
    code = code_match.group(1)
    # Exchange code for token
    import requests
    token_resp = requests.post(
        "https://anilist.co/api/v2/oauth/token",
        data={
            "grant_type": "authorization_code",
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": redirect_uri,
            "code": code,
        },
        timeout=15
    )
    if token_resp.status_code == 200:
        token_data = token_resp.json()
        return token_data.get("access_token", "")
    print_info(f"Failed to exchange code for token: {token_resp.text}")
    return ""

def main():
    ensure_output_dir()
    print_banner()
    print_info("Welcome to AniMal!\nExport your AniList to MAL XML with style.")

    username = None
    while not username:
        username = prompt_boxed(
            "Enter AniList username (type '-help' for info)",
            color="CYAN",
            helpmsg=FIELD_HELP["username"]
        )

    use_private = prompt_boxed(
        "Want to include PRIVATE AniList entries? (y/N)",
        color="YELLOW",
        helpmsg=FIELD_HELP["private_entries"],
        default="N"
    ).lower() == "y"

    anilist_token = ""
    if use_private:
        anilist_token = get_anilist_token_oauth()
        if not anilist_token:
            print_info("No token acquired. Only public entries will be fetched.")

    mal_username = prompt_boxed(
        "Enter your MyAnimeList (MAL) username (optional):",
        color="MAGENTA",
        helpmsg=FIELD_HELP["mal_username"],
        default=""
    )
    my_id = get_mal_id_from_username(mal_username)
    if mal_username:
        print_success(f"MAL user ID for {mal_username} is {my_id}")
    else:
        print_info("No MAL username provided. Using '0' as user id for anime, blank for manga.")

    user_id = get_user_id(username, token=anilist_token)
    print_success(f"AniList user ID for {username} is {user_id}")

    print(boxed_text("Export options:\n1: Anime only\n2: Manga only\n3: Both anime and manga", "MAGENTA"))
    
    choice = None
    while choice not in ["1", "2", "3"]:
        choice = prompt_boxed(
            "Choose export type (1/2/3) (type '-help' for info)",
            default="3",
            color="CYAN",
            helpmsg=FIELD_HELP["export_type"]
        )

    if prompt_boxed("Filter by status? (y/N)", default="N", color="YELLOW", helpmsg=FIELD_HELP["filter_status"]).lower() == "y":
        status_input = prompt_boxed(
            "Enter statuses (numbers/codes, e.g. 1 3 or COMPLETED):",
            color="YELLOW",
            helpmsg=FIELD_HELP["status_select"]
        )
        statuses = get_status_codes(status_input)
        while not statuses:
            status_input = prompt_boxed(
                "Invalid status. Enter valid numbers/codes (see above):",
                color="YELLOW",
                helpmsg=FIELD_HELP["status_select"]
            )
            statuses = get_status_codes(status_input)
    else:
        statuses = None

    if prompt_boxed("Filter by title substring? (y/N)", default="N", color="YELLOW", helpmsg=FIELD_HELP["filter_title"]).lower() == "y":
        title_sub = prompt_boxed("Enter substring to match in title:", color="YELLOW", helpmsg=FIELD_HELP["title_substring"])
    else:
        title_sub = None

    if choice in ["1", "3"]:
        print_info("Fetching anime list...")
        anime_entries = fetch_list(user_id, "ANIME", token=anilist_token)
        if statuses or title_sub:
            anime_entries = filter_entries(anime_entries, statuses, title_sub)
        print_stats(anime_entries, "Anime")
        basefile = os.path.join("output", f"{username}_anime")
        write_xml(anime_entries, basefile + ".xml", kind="anime", username=mal_username, user_id=my_id)

    if choice in ["2", "3"]:
        print_info("Fetching manga list...")
        manga_entries = fetch_list(user_id, "MANGA", token=anilist_token)
        if statuses or title_sub:
            manga_entries = filter_entries(manga_entries, statuses, title_sub)
        print_stats(manga_entries, "Manga")
        basefile = os.path.join("output", f"{username}_manga")
        write_xml(manga_entries, basefile + ".xml", kind="manga", username=mal_username, user_id=my_id)

    print_outro()

if __name__ == "__main__":
    main()
