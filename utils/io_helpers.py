import os
from core.xml_builder import make_myinfo_block, anime_entry_xml, manga_entry_xml
from utils.cli_helpers import print_success, confirm_overwrite

def ensure_output_dir():
    os.makedirs("output", exist_ok=True)

def write_xml(entries, filename, kind, username, user_id):
    if os.path.exists(filename) and not confirm_overwrite(filename):
        return
    
    root_tag = "myanimelist" if kind == "anime" else "mymangalist"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<{root_tag}>\n')
        f.write(make_myinfo_block(username, user_id, entries, kind) + "\n")
        
        for entry in entries:
            xml_entry = (
                anime_entry_xml(entry, user_id) 
                if kind == "anime" 
                else manga_entry_xml(entry)
            )
            f.write(xml_entry)
        
        f.write(f"</{root_tag}>\n")
    
    print_success(f"Exported {len(entries)} entries to:\n{filename}")
