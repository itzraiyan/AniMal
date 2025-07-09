# core/utils.py
from config import constants

def show_status_grid(width=44):
    # Improved status grid with margins, padding, and cleaner lines for readability
    # Responsive to width for mobile/Termux but visually appealing
    status_list = constants.STATUS_LIST
    col1 = "Num"
    col2 = "Status"
    col3 = "Description"
    # Calculate dynamic column widths
    num_w = 3
    status_w = max(len(col2), max(len(s[0]) for s in status_list))
    desc_w = width - (num_w + status_w + 9)
    if desc_w < 10:  # fallback for very small terminals
        desc_w = 10
    # Build grid with spacing and extra vertical margin
    lines = []
    border = f"  ┌{'─'*(num_w+2)}┬{'─'*(status_w+2)}┬{'─'*(desc_w+2)}┐"
    header = f"  │ {'Num'.ljust(num_w)} │ {col2.ljust(status_w)} │ {col3.ljust(desc_w)} │"
    sep =    f"  ├{'─'*(num_w+2)}┼{'─'*(status_w+2)}┼{'─'*(desc_w+2)}┤"
    lines.append("")
    lines.append(border)
    lines.append(header)
    lines.append(sep)
    for i, (status, desc) in enumerate(status_list):
        lines.append(
            f"  │ {str(i+1).ljust(num_w)} │ {status.ljust(status_w)} │ {desc.ljust(desc_w)} │"
        )
    lines.append(border.replace('┬', '┴').replace('┐', '┘').replace('┌', '└'))
    lines.append("")
    return "\n".join(lines)

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
    "AniMal - AniList to MAL XML exporter\n"
    "At any prompt, type '-help' for this guide.\n\n"
    "How to use:\n"
    "1. Enter your AniList username (public, no password needed).\n"
    "2. Enter your MAL username (optional, improves XML import compatibility).\n"
    "3. Choose export type:\n"
    "   - 1: Anime only\n"
    "   - 2: Manga only\n"
    "   - 3: Both anime and manga\n"
    "4. Filters (optional):\n"
    "   • By **status**: You may enter one or more status numbers or codes (e.g. 1 3 or COMPLETED,DROPPED).\n"
    "     Status codes:"
    + show_status_grid(width=44) +
    "     (Multiple allowed, separated by space or comma.)\n"
    "   • By **title substring**: Enter any word/phrase to only export entries whose titles contain it (case-insensitive).\n"
    "     Example: 'naruto' => Only titles with 'naruto'.\n"
    "5. Exported files are saved to the ./output/ directory.\n"
    "For best results, use in a terminal at least 45 characters wide.\n"
    "Enjoy!"
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