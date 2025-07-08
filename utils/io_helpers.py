import os
from core.xml_builder import make_myinfo_block, anime_entry_xml, manga_entry_xml
from utils.cli_helpers import print_success, confirm_overwrite

def ensure_output_dir():
    if not os.path.exists("output"):
        os.makedirs("output")

def write_xml(entries, filename, kind, username, user_id):
    if os.path.isfile(filename) and not confirm_overwrite(filename):
        print("Skipped file creation.")
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
    
    print_success(f"Exported {len(entries)} entries to:\n{filename}")
