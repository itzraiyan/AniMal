# AniMal: AniList to MAL XML Exporter 🐾

![Anime Export Tool](https://files.catbox.moe/o74pow.png)

Convert your AniList anime/manga library to MAL-compatible XML files with this user-friendly CLI tool. Preserve your scores, progress, status, dates, and notes when migrating between platforms!

> **Note**: This project includes AI-generated components, but the core idea and structure are fully created and designed by the original author.

## ✨ Features

- 🎨 **Colorful terminal interface** with ASCII art banners
- 🔍 **Filter by status/title** - Export only specific entries
- 📊 **Collection statistics** - View average scores and status distribution
- 🔄 **Overwrite protection** - Prevent accidental data loss
- 📦 **Zero configuration** - Just run and follow prompts
- 🐍 **Pure Python** - No complex dependencies required

## 📥 Installation

### For Linux Users

```bash
# 1. Install Python and Git
sudo apt update
sudo apt install python3 python3-pip git

#  ascended# 2. Clone the repository
git clone https://github.com/itzraiyan/AniMal.git
cd AniMal

# 3. Install Python dependencies
pip3 install colorama requests

# 4. Run the tool
python3 main.py
```

### For Termux (Android)

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

## 🚀 Usage Guide

1. **Start the program**:
   ```bash
   python main.py
   ```

2. **Enter your AniList username** when prompted:
   ```
   ┌──────────────────────────────────────────────────────────┐
   │ Enter AniList username (type '-help' for help)           │
   └──────────────────────────────────────────────────────────┘
   > your_anilist_username
   ```

3. **Optionally enter your MAL username** for better XML compatibility:
   ```
   ┌──────────────────────────────────────────────────────────┐
   │ Enter your MyAnimeList (MAL) username (optional):        │
   └──────────────────────────────────────────────────────────┘
   > your_mal_username
   ```

4. **Choose export type** (1=Anime, 2=Manga, 3=Both):
   ```
   ┌──────────────────────────────────────────────────────────┐
   │ Export options:                                         │
   │ 1: Anime only                                           │
   │ 2: Manga only                                          │
   │ 3: Both anime and manga                                │
   └──────────────────────────────────────────────────────────┘
   > 3
   ```

5. **Apply filters if desired**:
   ```
   ┌──────────────────────────────────────────────────────────┐
   │ Filter by status? (y/N) [N]                             │
   └──────────────────────────────────────────────────────────┘
   > y

   ┌──────────────────────────────────────────────────────────┐
   │ Enter AniList status(es) (numbers/words)                │
   └──────────────────────────────────────────────────────────┘
   > 1 3 5  # COMPLETED, DROPPED, PLANNING
   ```

6. **Find your XML files** in the `output/` directory:
   ```
   output/your_anilist_username_anime.xml
   output/your_anilist_username_manga.xml
   ```

## 🧩 File Structure

```
AniMal/
├── core/                    # Business logic
│   ├── fetcher.py           # Data fetching from AniList API
│   ├── utils.py             # Helper functions and status mapping
│   └── xml_builder.py       # XML generation for MAL format
├── utils/                   # Utility modules
│   ├── cli_helpers.py       # Colorful terminal interface
│   └── io_helpers.py        # File operations and output handling
├── config/                  # Configuration
│   └── constants.py         # API endpoints, status lists, ASCII art
├── main.py                  # Entry point
└── README.md                # This documentation
```

## ❓ Frequently Asked Questions

**Q: Why would I need this tool?**  
A: When switching from AniList to MyAnimeList (or vice versa), this tool preserves your library data in a format MAL can import.

**Q: What data gets exported?**  
A: The following data is exported:
- Titles
- Scores (1-10 scale)
- Progress (episodes/chapters read)
- Status (watching, completed, etc.)
- Start/end dates
- Personal notes

**Q: Is my AniList password required?**  
A: No! Only your public username is needed to access your public profile.

**Q: Can I run this on Windows?**  
A: Yes! Install Python from [python.org](https://www.python.org) and follow the Linux instructions.

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Happy exporting!** ✨ If you enjoy this tool, please consider starring the repository on [GitHub](https://github.com/itzraiyan/AniMal)!