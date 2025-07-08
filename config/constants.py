# ========== CONFIG & CONSTANTS ==========

# API Endpoints
ANILIST_API = "https://graphql.anilist.co"
MAL_USER_ID_API = "https://api.jikan.moe/v4/users/{username}/full"
OUTPUT_DIR = "output"

# Status Mapping
STATUS_LIST = [
    ("COMPLETED", "Finished watching/reading"),
    ("CURRENT", "Currently watching/reading"),
    ("DROPPED", "Dropped"),
    ("PAUSED", "On-hold"),
    ("PLANNING", "Plan to watch/read"),
    ("REPEATING", "Rewatching/rereading"),
]

# ASCII Art
ASCII_BANNERS = [
    r"""
     /\_/\  
    ( o.o ) 
     > ^ <    AniMal: AniList to MAL Exporter
    """,
    r"""
     |\_/|                  
     (°.°)   < meow~        
     (   )    AniMal         
     (___)                 
    """,
    r"""
      ／l、
    （ﾟ､ ｡７
      l、 ~ヽ
      じしf_,)ノ   AniMal
    """,
    r"""
     /\     /\
    {  `---'  }
    {  O   O  }
    ~~>  V  <~~
     \  \|/  /
      `-----'____
      /     \    \_
     {       }\  )_\_   AniMal
     |  \_/  |/ /  /
      \__/  /(_/  /
        (__/
    """,
]

# Quotes
QUOTES = [
    "“The world isn't perfect. But it's there for us, doing the best it can. That's what makes it so damn beautiful.” – Roy Mustang",
    "“No one knows what the future holds. That's why its potential is infinite.” – Rintarou Okabe",
    "“Whatever you lose, you'll find it again. But what you throw away you'll never get back.” – Kenshin Himura",
    "“To know sorrow is not terrifying. What is terrifying is to know you can't go back to happiness you could have.” – Matsumoto Rangiku",
    "“A lesson without pain is meaningless.” – Edward Elric",
    "“If you can't find a reason to fight, then you shouldn't be fighting.” – Akame",
    "“Do not fear death. Fear the unlived life.” – Nanny McPhee",
    "“Power comes in response to a need, not a desire. You have to create that need.” – Goku",
    "“Forgetting is like a wound. The wound may heal, but it has already left a scar.” – Monkey D. Luffy",
    "“You should enjoy the little detours. Because that's where you'll find the things more important than what you want.” – Ging Freecss",
    "“A person grows up when he's able to overcome hardships. Protection is important, but there are some things a person must learn on his own.” – Jiraiya",
    "“A person becomes strong when they have someone they want to protect.” – Haku",
    "“In our society, letting others find out that you're a nice guy is a very risky move. It's extremely likely that someone would take advantage of that.” – Hitagi Senjougahara",
    "“In this world, is the destiny of mankind controlled by some transcendental entity or law? Is it like the hand of God hovering above? At least it is true that man has no control, even over his own will.” – Narration (Berserk)",
    "“It’s not the face that makes someone a monster; it’s the choices they make with their lives.” – Naruto Uzumaki",
    "“The world is not beautiful, therefore it is.” – Kino (Kino's Journey)",
    "“Even if I can’t do it now, I’ll get stronger and stronger until I can. That’s the spirit of a man.” – Kamina",
    "“The world is full of pain and suffering. But there is also hope, and beauty. You just have to look for it.” – Violet Evergarden",
    "“Humans are weak creatures. That’s why we cling to each other. That’s why we help each other.” – Takashi Komuro (Highschool of the Dead)",
    "“A lesson you learn from getting hurt is not something you can learn from being protected.” – Kurisu Makise"
]
# Responsive Help Text
HELP_TEXT = """
AniMal - AniList to MAL XML Exporter

Export your AniList library to MAL XML format.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💻 USAGE:
1. Enter AniList username
2. Enter MAL username (optional)
3. Choose export type (1=Anime, 2=Manga, 3=Both)
4. Apply filters if needed
5. XML files saved in /output

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔍 STATUS FILTERING:
Use numbers or names, separate with spaces/commas

1. COMPLETED  - Finished
2. CURRENT    - Watching/Reading
3. DROPPED    - Dropped
4. PAUSED     - On-Hold
5. PLANNING   - Plan to Watch/Read
6. REPEATING  - Rewatching/Rereading

Examples:
  "1 3 5" 
  "COMPLETED, DROPPED"
  "current planning"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔧 TROUBLESHOOTING:
• User not found? Check spelling
• No entries? Try different filters
• Install missing packages:
  pip install colorama requests

Type '-help' at any prompt for this guide.
"""
