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
    "“Do not fear death. Fear the unlived life.” – Nanny McPhee"
]

# Help Text
HELP_TEXT = (
    "AniMal - AniList to MAL XML Exporter\n\n"
    "Steps:\n"
    "1. Enter your AniList username\n"
    "2. Enter your MAL username (optional, for XML compatibility)\n"
    "3. Choose export type: Anime, Manga, or Both\n"
    "4. Apply filters by status or title if needed\n"
    "5. Exported files will be saved in the 'output' directory\n\n"
    "Status Codes:\n" +
    "\n".join([f"{i+1}. {status[0]} - {status[1]}" for i, status in enumerate(STATUS_LIST)]) +
    "\n\nYou can enter status numbers and/or words, separated by spaces or commas."
)
