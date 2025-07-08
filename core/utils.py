# core/utils.py
from config import constants

def show_status_grid():
    grid = "Num | Status      | Description\n"
    grid += "----+------------+-------------------------\n"
    for i, (status, desc) in enumerate(constants.STATUS_LIST):
        grid += f"{i+1:<3} | {status:<10} | {desc}\n"
    return grid

def get_status_codes(input_str):
    results = set()
    tokens = [tok.strip() for tok in input_str.replace(',', ' ').split() if tok.strip()]
    for tok in tokens:
        if tok.isdigit():
            idx = int(tok) - 1
            if 0 <= idx < len(constants.STATUS_LIST):
                results.add(constants.STATUS_LIST[idx][0])
        else:
            for code, _ in constants.STATUS_LIST:
                if tok.upper() == code:
                    results.add(code)
    return list(results)

def filter_entries(entries, statuses=None, title=None):
    filtered = []
    for entry in entries:
        if statuses and entry.get("status") not in statuses:
            continue
        if title and title.lower() not in entry.get("media", {}).get("title", {}).get("romaji", "").lower():
            continue
        filtered.append(entry)
    return filtered

HELP_TEXT = (
    "AniMal - AniList exporter (XML only)\n"
    "At any input, type '-help' for this guide.\n"
    "1. Enter your AniList username.\n"
    "2. Enter your MAL username (for XML compatibility, can be left blank).\n"
    "3. Choose export type (anime, manga, both).\n"
    "4. You can filter by status or title.\n"
    "   - Status choices (multiple allowed, e.g. 1 3 5 or COMPLETED,DROPPED):\n" +
    show_status_grid() +
    "   - You can enter status numbers and/or words, separated by space or comma.\n"
    "5. All files go to ./output/\n"
    "Enjoy!\n"
)

def format_date(d):
    if not d or not d.get("year"):
        return "0000-00-00"
    year, month, day = d.get("year", 0), d.get("month", 0), d.get("day", 0)
    return f"{year:04d}-{month or 0:02d}-{day or 0:02d}"

def anilist_status_to_mal(status, media):
    if status == "COMPLETED": return "Completed"
    if status == "CURRENT": return "Watching" if media == "anime" else "Reading"
    if status == "DROPPED": return "Dropped"
    if status == "PAUSED": return "On-Hold"
    if status == "PLANNING": return "Plan to Watch" if media == "anime" else "Plan to Read"
    if status == "REPEATING": return "Watching" if media == "anime" else "Reading"
    return ""

def print_stats(entries, kind):
    if not entries:
        from utils.cli_helpers import print_info
        print_info(f"No {kind} entries to analyze.")
        return
    scores = [e.get("score") for e in entries if e.get("score")]
    statuses = {}
    for e in entries:
        st = e.get("status")
        statuses[st] = statuses.get(st, 0) + 1
    mean_score = f"{sum(scores)/len(scores):.2f}" if scores else "N/A"
    from utils.cli_helpers import print_info, color_text
    print_info(f"Stats for {kind}:")
    for st, count in statuses.items():
        print(color_text(f"{st}: {count}", "yellow"))
    print(color_text(f"Mean Score: {mean_score}", "blue"))
