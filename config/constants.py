# ========== CONFIG & CONSTANTS ==========

# API Endpoints
ANILIST_API = "https://graphql.anilist.co"
MAL_USER_ID_API = "https://api.jikan.moe/v4/users/{username}/full"
OUTPUT_DIR = "output"

# Status Mapping
STATUS_LIST = [
    ("COMPLETED", "Completed"),
    ("CURRENT", "Watching/Reading"),
    ("DROPPED", "Dropped"),
    ("PAUSED", "On-hold"),
    ("PLANNING", "Planned"),
    ("REPEATING", "Rewatch/Reread"),
]

# ASCII Art
ASCII_BANNERS = [
    r"""
██      ▄   ▄█ █▀▄▀█ ██   █     
█ █      █  ██ █ █ █ █ █  █     
█▄▄█ ██   █ ██ █ ▄ █ █▄▄█ █     
█  █ █ █  █ ▐█ █   █ █  █ ███▄  
   █ █  █ █  ▐    █     █     ▀ 
  █  █   ██      ▀     █        
 ▀                    ▀
    """,
    r"""
░█▀▀█ █▀▀▄ ░▀░ ░░ ▒█▀▄▀█ █▀▀█ █░░ 
▒█▄▄█ █░░█ ▀█▀ ▀▀ ▒█▒█▒█ █▄▄█ █░░ 
▒█░▒█ ▀░░▀ ▀▀▀ ░░ ▒█░░▒█ ▀░░▀ ▀▀▀                 
    """,
    r"""
▄▀█ █▄░█ █ ▄▄ █▀▄▀█ ▄▀█ █░░
█▀█ █░▀█ █ ░░ █░▀░█ █▀█ █▄▄
    """,
    r"""
░█████╗░███╗░░██╗██╗░░░░░░███╗░░░███╗░█████╗░██╗░░░░░  
██╔══██╗████╗░██║██║░░░░░░████╗░████║██╔══██╗██║░░░░░  
███████║██╔██╗██║██║█████╗██╔████╔██║███████║██║░░░░░  
██╔══██║██║╚████║██║╚════╝██║╚██╔╝██║██╔══██║██║░░░░░  
██║░░██║██║░╚███║██║░░░░░░██║░╚═╝░██║██║░░██║███████╗  
╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝
    """,
    r"""
 █████╗ ███╗   ██╗██╗    ███╗   ███╗ █████╗ ██╗     
██╔══██╗████╗  ██║██║    ████╗ ████║██╔══██╗██║     
███████║██╔██╗ ██║██║    ██╔████╔██║███████║██║     
██╔══██║██║╚██╗██║██║    ██║╚██╔╝██║██╔══██║██║     
██║  ██║██║ ╚████║██║    ██║ ╚═╝ ██║██║  ██║███████╗
╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝
    """,
    r"""
▄▄▄       ███▄    █  ██▓ ███▄ ▄███▓ ▄▄▄       ██▓    
▒████▄     ██ ▀█   █ ▓██▒▓██▒▀█▀ ██▒▒████▄    ▓██▒    
▒██  ▀█▄  ▓██  ▀█ ██▒▒██▒▓██    ▓██░▒██  ▀█▄  ▒██░    
░██▄▄▄▄██ ▓██▒  ▐▌██▒░██░▒██    ▒██ ░██▄▄▄▄██ ▒██░    
 ▓█   ▓██▒▒██░   ▓██░░██░▒██▒   ░██▒ ▓█   ▓██▒░██████▒
 ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░▓  ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░▓  ░
  ▒   ▒▒ ░░ ░░   ░ ▒░ ▒ ░░  ░      ░  ▒   ▒▒ ░░ ░ ▒  ░
  ░   ▒      ░   ░ ░  ▒ ░░      ░     ░   ▒     ░ ░   
      ░  ░         ░  ░         ░         ░  ░    ░  ░
    """
]

# Deep/meaningful Quotes (add many, Manga/Anime only, some new for variety)
QUOTES = [
    "“The world isn't perfect. But it's there for us, doing the best it can. That's what makes it so damn beautiful.” – Roy Mustang (Fullmetal Alchemist)",
    "“No one knows what the future holds. That's why its potential is infinite.” – Rintarou Okabe (Steins;Gate)",
    "“Whatever you lose, you'll find it again. But what you throw away you'll never get back.” – Kenshin Himura (Rurouni Kenshin)",
    "“To know sorrow is not terrifying. What is terrifying is to know you can't go back to happiness you could have.” – Matsumoto Rangiku (Bleach)",
    "“A lesson without pain is meaningless.” – Edward Elric (Fullmetal Alchemist)",
    "“If you can't find a reason to fight, then you shouldn't be fighting.” – Akame (Akame ga Kill!)",
    "“Do not fear death. Fear the unlived life.” – Nanny McPhee",
    "“Power comes in response to a need, not a desire. You have to create that need.” – Goku (Dragon Ball)",
    "“Forgetting is like a wound. The wound may heal, but it has already left a scar.” – Monkey D. Luffy (One Piece)",
    "“You should enjoy the little detours. Because that's where you'll find the things more important than what you want.” – Ging Freecss (Hunter x Hunter)",
    "“A person grows up when he's able to overcome hardships. Protection is important, but there are some things a person must learn on his own.” – Jiraiya (Naruto)",
    "“A person becomes strong when they have someone they want to protect.” – Haku (Naruto)",
    "“In our society, letting others find out that you're a nice guy is a very risky move. It's extremely likely that someone would take advantage of that.” – Hitagi Senjougahara (Bakemonogatari)",
    "“In this world, is the destiny of mankind controlled by some transcendental entity or law? Is it like the hand of God hovering above? At least it is true that man has no control, even over his own will.” – Narrator (Berserk)",
    "“It’s not the face that makes someone a monster; it’s the choices they make with their lives.” – Naruto Uzumaki",
    "“The world is not beautiful, therefore it is.” – Kino (Kino's Journey)",
    "“Even if I can’t do it now, I’ll get stronger and stronger until I can. That’s the spirit of a man.” – Kamina (Gurren Lagann)",
    "“The world is full of pain and suffering. But there is also hope, and beauty. You just have to look for it.” – Violet Evergarden",
    "“Humans are weak creatures. That’s why we cling to each other. That’s why we help each other.” – Takashi Komuro (Highschool of the Dead)",
    "“A lesson you learn from getting hurt is not something you can learn from being protected.” – Kurisu Makise (Steins;Gate)",
    "“If you don’t take risks, you can’t create a future!” – Monkey D. Luffy (One Piece)",
    "“You need to accept the fact that you’re not the best and have all the will to strive to be better than anyone you face.” – Roronoa Zoro (One Piece)",
    "“When you hit the point of no return, that’s the moment it truly becomes a journey.” – Hinata Shoyo (Haikyuu!!)",
    "“The world isn’t just black and white. There are so many shades in between.” – Kaneki Ken (Tokyo Ghoul)",
    "“No one knows what tomorrow will bring. That’s why its potential is infinite.” – Rintarou Okabe (Steins;Gate)",
    "“No matter how deep the night, it always turns to day, eventually.” – Brook (One Piece)",
    "“To defeat evil, I shall become an even greater evil.” – Lelouch Lamperouge (Code Geass)",
    "“The strong don’t win. The winners are strong.” – Shinichi Izumi (Parasyte)",
    "“It’s okay not to be okay as long as you are not giving up.” – Karen Aijou (Revue Starlight)",
    "“If you can’t do something, then don’t. Focus on what you can do.” – Shiroe (Log Horizon)",
    "“Living is anxiety and pain. But it’s also precious.” – Homura Akemi (Madoka Magica)",
    "“Don’t beg for things. Do it yourself, or else you won’t get anything.” – Renton Thurston (Eureka Seven)",
    "“I want you to be happy. I want you to laugh a lot. I don’t know what exactly I’ll be able to do for you, but I’ll always be by your side.” – Kagome Higurashi (Inuyasha)",
    "“You can die anytime, but living takes true courage.” – Kenshin Himura (Rurouni Kenshin)",
    "“It’s not the face that makes someone a monster; it’s the choices they make with their lives.” – Naruto Uzumaki",
    "“The only thing we’re allowed to do is to believe that we won’t regret the choice we made.” – Levi Ackerman (Attack on Titan)",
    "“You need to accept the fact that you’re not the best and have all the will to strive to be better than anyone you face.” – Roronoa Zoro (One Piece)",
    "“No matter how hard or impossible it is, never lose sight of your goal.” – Monkey D. Luffy (One Piece)",
    "“When you lose sight of your path, listen for the destination in your heart.” – Allen Walker (D.Gray-man)",
]
