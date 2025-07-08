# core/xml_builder.py
import os
from utils.cli_helpers import print_error, print_success, confirm_overwrite
from core.utils import anilist_status_to_mal, format_date

def make_myinfo_block(username, user_id, entries, kind):
    status_map = {
        'anime': {
            "Watching": "user_total_watching",
            "Completed": "user_total_completed",
            "On-Hold": "user_total_onhold",
            "Dropped": "user_total_dropped",
            "Plan to Watch": "user_total_plantowatch",
        },
        'manga': {
            "Reading": "user_total_reading",
            "Completed": "user_total_completed",
            "On-Hold": "user_total_onhold",
            "Dropped": "user_total_dropped",
            "Plan to Read": "user_total_plantoread",
        }
    }
    status_counts = {v: 0 for v in status_map[kind].values()}
    for e in entries:
        malstatus = anilist_status_to_mal(e.get("status"), kind)
        for k, v in status_map[kind].items():
            if malstatus == k:
                status_counts[v] += 1
    total = len(entries)
    lines = []
    lines.append("  <myinfo>")
    lines.append(f"    <user_id></user_id>")
    lines.append(f"    <user_name>{username}</user_name>")
    lines.append(f"    <user_export_type>{1 if kind=='anime' else 2}</user_export_type>")
    lines.append(f"    <user_total_{'anime' if kind == 'anime' else 'manga'}>{total}</user_total_{'anime' if kind == 'anime' else 'manga'}>")
    for k in status_map[kind].values():
        lines.append(f"    <{k}>{status_counts[k]}</{k}>")
    lines.append("  </myinfo>")
    return "\n".join(lines)

def anime_entry_xml(entry, my_id="0"):
    m = entry['media']
    return f"""  <anime>
    <series_animedb_id>{m.get('idMal') or 0}</series_animedb_id>
    <series_title><![CDATA[{m.get('title', {}).get('romaji', '')}]]></series_title>
    <series_type></series_type>
    <series_episodes>{m.get('episodes') or 0}</series_episodes>
    <my_id>{my_id}</my_id>
    <my_watched_episodes>{entry.get('progress') or 0}</my_watched_episodes>
    <my_start_date>{format_date(entry.get('startedAt'))}</my_start_date>
    <my_finish_date>{format_date(entry.get('completedAt'))}</my_finish_date>
    <my_rated></my_rated>
    <my_score>{entry.get('score') or 0}</my_score>
    <my_dvd></my_dvd>
    <my_storage></my_storage>
    <my_status>{anilist_status_to_mal(entry.get('status'), 'anime')}</my_status>
    <my_comments><![CDATA[{entry.get('notes') or ''}]]></my_comments>
    <my_times_watched>0</my_times_watched>
    <my_rewatch_value></my_rewatch_value>
    <my_tags><![CDATA[]]></my_tags>
    <my_rewatching>NO</my_rewatching>
    <my_rewatching_ep>0</my_rewatching_ep>
    <update_on_import>1</update_on_import>
  </anime>
"""

def manga_entry_xml(entry):
    m = entry['media']
    return f"""  <manga>
    <manga_mangadb_id>{m.get('idMal') or ''}</manga_mangadb_id>
    <manga_title><![CDATA[{m.get('title', {}).get('romaji', '')}]]></manga_title>
    <manga_volumes>{m.get('volumes') or 0}</manga_volumes>
    <manga_chapters>{m.get('chapters') or 0}</manga_chapters>
    <my_id></my_id>
    <my_read_volumes>{entry.get('progressVolumes') or 0}</my_read_volumes>
    <my_read_chapters>{entry.get('progress') or 0}</my_read_chapters>
    <my_start_date>{format_date(entry.get('startedAt'))}</my_start_date>
    <my_finish_date>{format_date(entry.get('completedAt'))}</my_finish_date>
    <my_scanalation_group><![CDATA[]]></my_scanalation_group>
    <my_score>{entry.get('score') or 0}</my_score>
    <my_storage></my_storage>
    <my_status>{anilist_status_to_mal(entry.get('status'), 'manga')}</my_status>
    <my_comments><![CDATA[{entry.get('notes') or ''}]]></my_comments>
    <my_times_read>0</my_times_read>
    <my_tags><![CDATA[]]></my_tags>
    <my_reread_value></my_reread_value>
    <my_rereading>NO</my_rereading>
    <update_on_import>1</update_on_import>
  </manga>
"""

def write_xml(entries, filename, kind="anime", username="", user_id="0", overwrite=False):
    if os.path.isfile(filename) and not overwrite:
        if not confirm_overwrite(filename):
            print_error(f"Skipped writing {filename}")
            return
    root_tag = "myanimelist" if kind == "anime" else "mymangalist"
    with open(filename, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write(f"<{root_tag}>\n")
        f.write(make_myinfo_block(username, user_id, entries, kind) + "\n")
        for entry in entries:
            if kind == "anime":
                f.write(anime_entry_xml(entry, my_id=user_id))
            else:
                f.write(manga_entry_xml(entry))
        f.write(f"</{root_tag}>\n")
    msg = f"Exported XML to\n{filename}"
    print_success(msg)
