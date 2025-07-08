from config.constants import STATUS_LIST

def format_date(d):
    if not d or not d.get("year"): return "0000-00-00"
    return f"{d['year']:04}-{d.get('month', 0):02}-{d.get('day', 0):02}"

def anilist_status_to_mal(status, media):
    mapping = {
        "COMPLETED": "Completed",
        "CURRENT": "Watching" if media == "anime" else "Reading",
        "DROPPED": "Dropped",
        "PAUSED": "On-Hold",
        "PLANNING": "Plan to Watch" if media == "anime" else "Plan to Read",
        "REPEATING": "Watching" if media == "anime" else "Reading"
    }
    return mapping.get(status, "")

def get_status_codes(input_str):
    codes = set()
    for token in input_str.replace(',', ' ').split():
        if token.isdigit():
            idx = int(token) - 1
            if 0 <= idx < len(STATUS_LIST):
                codes.add(STATUS_LIST[idx][0])
        else:
            token_upper = token.upper()
            for code, _ in STATUS_LIST:
                if token_upper == code:
                    codes.add(code)
    return list(codes)

def filter_entries(entries, statuses=None, title=None):
    filtered = []
    for entry in entries:
        if statuses and entry["status"] not in statuses:
            continue
        romaji_title = entry["media"]["title"]["romaji"].lower()
        if title and title.lower() not in romaji_title:
            continue
        filtered.append(entry)
    return filtered

def print_stats(entries, kind):
    if not entries: return
    scores = [e.get("score", 0) for e in entries]
    avg_score = sum(scores) / len(scores) if scores else 0
    print(f"• {kind} entries: {len(entries)}")
    print(f"• Average score: {avg_score:.2f}/10")
