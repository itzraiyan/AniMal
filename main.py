# main.py
import os
from utils.io_helpers import ensure_output_dir
from utils.cli_helpers import print_banner, print_outro, print_info, print_success, prompt_boxed, boxed_text
from utils.mal_id_fetcher import get_mal_id_from_username
from core.fetcher import get_user_id, fetch_list
from core.utils import HELP_TEXT, show_status_grid, get_status_codes, filter_entries, print_stats
from core.xml_builder import write_xml

def main():
    ensure_output_dir()
    print_banner()
    print_info("Welcome to AniMal!\nExport your AniList to MAL XML with style.")

    username = None
    while not username:
        username = prompt_boxed(
            "Enter AniList username (type '-help' for help)",
            color="CYAN",
            helpmsg=HELP_TEXT
        )

    mal_username = prompt_boxed(
        "Enter your MyAnimeList (MAL) username (for XML compatibility, optional):",
        color="MAGENTA",
        helpmsg="Your MAL username is used to set your <my_id> in the XML for best compatibility. If left blank, '0' will be used for anime, blank for manga.",
        default=""
    )
    my_id = get_mal_id_from_username(mal_username)
    if mal_username:
        print_success(f"MAL user ID for {mal_username} is {my_id}")
    else:
        print_info("No MAL username provided. Using '0' as user id for anime, blank for manga.")

    user_id = get_user_id(username)
    print_success(f"AniList user ID for {username} is {user_id}")

    # Always show boxed export options before prompt, to avoid border confusion.
    print(boxed_text("Export options:\n1: Anime only\n2: Manga only\n3: Both anime and manga", "MAGENTA"))
    
    choice = None
    while choice not in ["1", "2", "3"]:
        choice = prompt_boxed(
            "Choose export type (1/2/3) (type '-help' for help)",
            default="3",
            color="CYAN",
            helpmsg=HELP_TEXT
        )

    if prompt_boxed("Filter by status? (y/N)", default="N", color="YELLOW").lower() == "y":
        status_help = (
            "Select one or more statuses (by number or code, space/comma separated):\n"
            + show_status_grid(width=44)
            + "\nExamples: 1 3 5   or   COMPLETED,DROPPED"
        )
        status_input = prompt_boxed(
            "Enter AniList status(es) (numbers/words, e.g. 1 3 or COMPLETED)",
            color="YELLOW",
            helpmsg=status_help
        )
        statuses = get_status_codes(status_input)
        while not statuses:
            status_input = prompt_boxed(
                "Invalid status. Enter valid status numbers/words (see grid above)",
                color="YELLOW",
                helpmsg=status_help
            )
            statuses = get_status_codes(status_input)
    else:
        statuses = None

    if prompt_boxed("Filter by title substring? (y/N)", default="N", color="YELLOW").lower() == "y":
        print(boxed_text(
            "Enter a word or phrase. Only titles containing this substring will be exported.\n"
            "Example: 'one piece' exports all entries with 'one piece' in the title.",
            "YELLOW"
        ))
        title_sub = prompt_boxed("Enter substring to match in title", color="YELLOW")
    else:
        title_sub = None

    if choice in ["1", "3"]:
        print_info("Fetching anime list...")
        anime_entries = fetch_list(user_id, "ANIME")
        if statuses or title_sub:
            anime_entries = filter_entries(anime_entries, statuses, title_sub)
        print_stats(anime_entries, "Anime")
        basefile = os.path.join("output", f"{username}_anime")
        write_xml(anime_entries, basefile + ".xml", kind="anime", username=mal_username, user_id=my_id)

    if choice in ["2", "3"]:
        print_info("Fetching manga list...")
        manga_entries = fetch_list(user_id, "MANGA")
        if statuses or title_sub:
            manga_entries = filter_entries(manga_entries, statuses, title_sub)
        print_stats(manga_entries, "Manga")
        basefile = os.path.join("output", f"{username}_manga")
        write_xml(manga_entries, basefile + ".xml", kind="manga", username=mal_username, user_id=my_id)

    print_outro()

if __name__ == "__main__":
    main()