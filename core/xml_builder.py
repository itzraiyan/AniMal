from core.utils import format_date, anilist_status_to_mal

def make_myinfo_block(username, user_id, entries, kind):
    status_map = {
        'anime': {
            "Watching": "watching", "Completed": "completed",
            "On-Hold": "onhold", "Dropped": "dropped",
            "Plan to Watch": "plantowatch",
        },
        'manga': {
            "Reading": "reading", "Completed": "completed",
            "On-Hold": "onhold", "Dropped": "dropped",
            "Plan to Read": "plantoread",
        }
    }
    counts = {v: 0 for v in status_map[kind].values()}
    for e in entries:
        status = anilist_status_to_mal(e["status"], kind)
        if status in status_map[kind]:
            counts[status_map[kind][status]] += 1

    lines = [
        "  <myinfo>",
        f"    <user_id></user_id>",
        f"    <user_name>{username}</user_name>",
        f"    <user_export_type>{1 if kind=='anime' else 2}</user_export_type>",
        f"    <user_total_{'anime' if kind=='anime' else 'manga'}>{len(entries)}</user_total_{'anime' if kind=='anime' else 'manga'}>"
    ]
    for k, v in counts.items():
        lines.append(f"    <user_total_{k}>{v}</user_total_{k}>")
    lines.append("  </myinfo>")
    return "\n".join(lines)

def anime_entry_xml(entry, my_id):
    m = entry['media']
    return f"""  <anime>
    <series_animedb_id>{m.get('idMal') or 0}</series_animedb_id>
    <series_title><![CDATA[{m['title']['romaji']}]]></series_title>
    <my_watched_episodes>{entry.get('progress', 0)}</my_watched_episodes>
    <my_start_date>{format_date(entry.get('startedAt'))}</my_start_date>
    <my_finish_date>{format_date(entry.get('completedAt'))}</my_finish_date>
    <my_score>{entry.get('score', 0)}</my_score>
    <my_status>{anilist_status_to_mal(entry['status'], 'anime')}</my_status>
    <my_comments><![CDATA[{entry.get('notes', '')}]]></my_comments>
  </anime>
"""

def manga_entry_xml(entry):
    m = entry['media']
    return f"""  <manga>
    <manga_mangadb_id>{m.get('idMal') or ''}</manga_mangadb_id>
    <manga_title><![CDATA[{m['title']['romaji']}]]></manga_title>
    <my_read_volumes>{entry.get('progressVolumes', 0)}</my_read_volumes>
    <my_read_chapters>{entry.get('progress', 0)}</my_read_chapters>
    <my_start_date>{format_date(entry.get('startedAt'))}</my_start_date>
    <my_finish_date>{format_date(entry.get('completedAt'))}</my_finish_date>
    <my_score>{entry.get('score', 0)}</my_score>
    <my_status>{anilist_status_to_mal(entry['status'], 'manga')}</my_status>
    <my_comments><![CDATA[{entry.get('notes', '')}]]></my_comments>
  </manga>
"""
