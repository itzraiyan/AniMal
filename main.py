"""
AniMal: AniList to MAL XML Exporter
Main entry point for the application
"""

from core.fetcher import fetch_list, get_user_id
from core.utils import get_status_codes, filter_entries, print_stats
from utils.cli_helpers import (
    print_banner, print_outro, print_error, print_success, print_info,
    prompt_boxed, boxed_text, confirm_overwrite
)
from utils.io_helpers import ensure_output_dir, write_xml
from config.constants import STATUS_LIST, HELP_TEXT
from core.xml_builder import make_myinfo_block
from utils.mal_id_fetcher import get_mal_id_from_username

def main():
    ensure_output_dir()
    print_banner()
    print_info("Welcome to AniMal! Type '-help' for assistance.")

    username = None
    while not username:
        username = prompt_boxed(
            "Enter AniList username (type '-help' for guide)",
            color="CYAN",
            helpmsg=HELP_TEXT
        )

    mal_username = prompt_boxed(
        "Enter MAL username (optional, type '-help' for guide)",
        color="MAGENTA",
        helpmsg=HELP_TEXT,
        default=""
    )
    my_id = get_mal_id_from_username(mal_username)
    
    if mal_username:
        print_success(f"MAL user ID for {mal_username} is {my_id}")
    else:
        print_info("No MAL username provided. Using default IDs.")

    user_id = get_user_id(username)
    print_success(f"AniList user ID for {username} is {user_id}")

    print(boxed_text("Export options:\n1: Anime\n2: Manga\n3: Both", "MAGENTA"))
    choice = prompt_boxed(
        "Choose export type (1/2/3, type '-help' for guide)",
        default="3",
        color="CYAN",
        helpmsg=HELP_TEXT
    )

    statuses = None
    if prompt_boxed("Filter by status? (y/N, type '-help' for guide)", default="N", color="YELLOW").lower() == "y":
        status_input = prompt_boxed(
            "Enter status(es) (type '-help' for guide)",
            color="YELLOW",
            helpmsg=HELP_TEXT
        )
        statuses = get_status_codes(status_input)

    title_sub = None
    if prompt_boxed("Filter by title? (y/N)", default="N", color="YELLOW").lower() == "y":
        title_sub = prompt_boxed("Enter title substring", color="YELLOW")

    if choice in ["1", "3"]:
        anime_entries = fetch_list(user_id, "ANIME")
        anime_entries = filter_entries(anime_entries, statuses, title_sub)
        print_stats(anime_entries, "Anime")
        write_xml(
            entries=anime_entries,
            kind="anime",
            username=mal_username,
            user_id=my_id,
            filename=f"output/{username}_anime.xml"
        )

    if choice in ["2", "3"]:
        manga_entries = fetch_list(user_id, "MANGA")
        manga_entries = filter_entries(manga_entries, statuses, title_sub)
        print_stats(manga_entries, "Manga")
        write_xml(
            entries=manga_entries,
            kind="manga",
            username=mal_username,
            user_id=my_id,
            filename=f"output/{username}_manga.xml"
        )

    print_outro()

if __name__ == "__main__":
    main()
