# AniMal: AniList to MAL XML Exporter 🐾

![Anime Export Tool](https://files.catbox.moe/o74pow.png)

Effortlessly migrate your AniList anime and manga library to MyAnimeList (MAL) with this streamlined, user-friendly CLI tool! AniMal converts your AniList data into MAL-compatible XML files—preserving your scores, progress, status, dates, and notes for a seamless transition.

> **Note:** This project utilizes some AI-generated components, but the core idea, design, and structure are entirely crafted by the original author.

---

## ✨ Features

- 🎨 **Vivid terminal interface** with stylish ASCII art banners
- 🔍 **Smart filtering** — Export only specific entries by status or title
- 📊 **Collection stats** — Instantly see averages and status breakdowns
- 🔄 **Overwrite safeguards** — Prevents accidental data loss
- ⚡ **Zero setup needed** — Just run and follow intuitive prompts
- 🐍 **Pure Python** — No heavy dependencies or frameworks

---

## 📥 Installation

### Linux

```bash
# 1. Install Python and Git
sudo apt update
sudo apt install python3 python3-pip git

# 2. Clone the repository
git clone https://github.com/itzraiyan/AniMal.git
cd AniMal

# 3. Install Python dependencies
pip3 install colorama requests

# 4. Run the tool
python3 main.py
```

### Android (Termux)

```bash
# 1. Update packages and install requirements
pkg update
pkg install python git

# 2. Clone the repository
git clone https://github.com/itzraiyan/AniMal.git
cd AniMal

# 3. Install Python dependencies
pip install colorama requests

# 4. Run the tool
python main.py
```

### Windows

1. [Download Python](https://www.python.org/downloads/)
2. [Download Git](https://git-scm.com/download/win)
3. Open Command Prompt or PowerShell:
   ```bash
   git clone https://github.com/itzraiyan/AniMal.git
   cd AniMal
   pip install colorama requests
   python main.py
   ```

---

## 🚀 Quick Start

1. **Launch the program:**
   ```bash
   python main.py
   ```

2. **Enter your AniList username** when prompted:
   ```
   ┌─────────────────────────────────────────────────────┐
   │ Enter AniList username (type '-help' for help)      │
   └─────────────────────────────────────────────────────┘
   > your_anilist_username
   ```

3. **(Optional) Enter your MAL username** for improved XML compatibility:
   ```
   ┌─────────────────────────────────────────────────────┐
   │ Enter your MyAnimeList (MAL) username (optional):   │
   └─────────────────────────────────────────────────────┘
   > your_mal_username
   ```

4. **Select export type:**
   ```
   ┌─────────────────────────────────────────────────────┐
   │ Export options:                                     │
   │ 1: Anime only                                       │
   │ 2: Manga only                                       │
   │ 3: Both anime and manga                             │
   └─────────────────────────────────────────────────────┘
   > 3
   ```

5. **Apply filters (optional):**
   ```
   ┌─────────────────────────────────────────────────────┐
   │ Filter by status? (y/N) [N]                         │
   └─────────────────────────────────────────────────────┘
   > y

   ┌─────────────────────────────────────────────────────┐
   │ Enter AniList status(es) (numbers/words)            │
   └─────────────────────────────────────────────────────┘
   > 1 3 5  # COMPLETED, DROPPED, PLANNING
   ```

6. **Locate your XML files** in the `output/` directory:
   ```
   output/your_anilist_username_anime.xml
   output/your_anilist_username_manga.xml
   ```

---

## 🧩 Project Structure

```
AniMal/
├── core/                    # Core logic modules
│   ├── fetcher.py           # Fetches data from AniList API
│   ├── utils.py             # Helpers and status mapping
│   └── xml_builder.py       # Generates MAL-compatible XML
├── utils/                   # Terminal and I/O utilities
│   ├── cli_helpers.py       # Colorful CLI interface
│   └── io_helpers.py        # Output and file handling
├── config/                  # Config and constants
│   └── constants.py         # API URLs, statuses, ASCII art
├── main.py                  # Entry point
└── README.md                # This file
```

---

## ❓ FAQ

**Why use AniMal?**  
When switching from AniList to MAL (or vice versa), AniMal preserves your detailed library stats—no more manual re-entry!

**What does AniMal export?**
- Titles (romaji, English, native)
- Scores (1–10 scale)
- Progress (episodes/chapters)
- Status (watching, completed, on-hold, etc.)
- Start/end dates
- Personal notes

**Is my AniList password needed?**  
Never! AniMal only requires your public username.

**Can I use AniMal on Windows?**  
Absolutely! Just follow the [Windows instructions above](#windows).

---

## 🤝 Contributing

All contributions are welcome!  
To get started:

1. Fork this repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit (`git commit -m 'Describe your feature'`)
5. Push your branch (`git push origin feature/your-feature`)
6. Open a pull request

---

## 📜 License

Licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

**Happy exporting!** ✨  
If you find AniMal helpful, please star the repository on [GitHub](https://github.com/itzraiyan/AniMal)!
