# AniMal: AniList to MAL XML Exporter 🐾

![AniMal Banner](https://files.catbox.moe/o74pow.png)

> **Note:** This project utilizes some AI-generated components, but the core idea, design, and structure are entirely crafted by the original author.

---

AniMal is an advanced Python command-line tool that helps you export your AniList anime and manga library to MyAnimeList (MAL) XML files. It preserves your scores, progress, statuses, dates, and personal notes.

Whether you're switching platforms, keeping a backup, or just want more control over your list, AniMal makes the process easy and transparent.

---

## ✨ Features

* 🖼️ **Beautiful terminal interface** with random ASCII art and anime quotes
* 🔍 **Smart filtering** — Export only what you want, by status or title substring
* 📊 **Collection stats** — Instantly see scores and breakdowns
* 🛑 **Overwrite safeguards** — Never lose data by accident
* ⚡ **Zero setup** — Just install Python and run
* 🐍 **Pure Python** — No heavy dependencies, works everywhere
* 📂 **Open-source** — No tracking, no ads, no nonsense
* 🔒 **Private AniList support** — Export private entries securely with AniList OAuth

---

## 📅 Installation

### Linux

```bash
sudo apt update
sudo apt install python3 python3-pip git
git clone https://github.com/itzraiyan/AniMal.git
cd AniMal
pip3 install -r requirements.txt
```

### Android (Termux)

```bash
pkg update
pkg install python git
git clone https://github.com/itzraiyan/AniMal.git
cd AniMal
pip install -r requirements.txt
```

### Windows

1. [Download Python](https://www.python.org/downloads/)
2. [Download Git](https://git-scm.com/download/win)
3. Open Command Prompt or PowerShell:

   ```bash
   git clone https://github.com/itzraiyan/AniMal.git
   cd AniMal
   pip install -r requirements.txt
   ```

---

## ▶️ One-Command Run Setup

You can set up AniMal so you can just type `AniMal` from anywhere in your terminal to launch the program — no need to type `python main.py` every time!

### Linux

```bash
echo "alias AniMal='python3 $HOME/AniMal/main.py'" >> ~/.bashrc
source ~/.bashrc
```

If you're using Zsh:

```bash
echo "alias AniMal='python3 $HOME/AniMal/main.py'" >> ~/.zshrc
source ~/.zshrc
```

### Android (Termux)

```bash
echo "alias AniMal='python $HOME/AniMal/main.py'" >> ~/.bashrc
source ~/.bashrc
```

### Windows

**Option 1: Using a batch file (recommended for beginners)**

1. Open Notepad and paste:

   ```bat
   @echo off
   python "%USERPROFILE%\AniMal\main.py" %*
   ```

   *(Adjust the path if you cloned AniMal elsewhere)*

2. Save as `AniMal.bat` in a folder that's in your PATH (e.g., `C:\Windows` or add a folder like `C:\Users\YourName\bin` to your PATH).

3. Now you can open Command Prompt and run:

   ```
   AniMal
   ```

**Option 2: Add Python scripts to PATH and create a shortcut**

* You can create a shortcut to `python.exe` with the argument `"C:\Path\To\AniMal\main.py"` and place it on your Desktop or in a folder in your PATH.

---

## 🚀 Quick Start Guide

1. **Run the tool:**
   Open your terminal and type:

   ```
   AniMal
   ```

   *(Or `python main.py` if you haven't set up the one-click launcher)*

2. **Follow the on-screen prompts:**
   AniMal guides you step-by-step. You can type `-help` at any prompt for context help!

   * **Enter AniList username:**
     Your AniList username (see your AniList profile page for your username).

   * **Want to include private AniList entries?**
     If you want to include private entries, you'll be guided through AniList's OAuth process:

     1. **Create an AniList Application:**
        - Go to [AniList Developer Settings](https://anilist.co/settings/developer)
        - Click "Create New Client"
        - Name it (e.g., AniMal Exporter) and set the redirect URL to `https://localhost/` or any URL you like.
        - After creating, copy your Client ID and Client Secret.

     2. **Authorize AniMal:**
        - AniMal will show you an authorization URL to visit in your browser.
        - Log in to AniList, approve the permissions, and you'll be redirected (the URL will contain `?code=...`).
        - Copy the full redirected URL and paste it into AniMal.

     3. **Token is handled for you:**
        - AniMal extracts the token and uses it automatically.
        - You can now export both public and private entries.

     *(If you skip this step, only public entries will be exported.)*

   * **Enter MAL username (optional):**
     For best compatibility when importing to MAL, enter your MAL username (or skip).

   * **Choose export type:**
     * 1: Anime only
     * 2: Manga only
     * 3: Both anime and manga (default)

   * **Filter by status?**
     Want only completed, dropped, or a custom selection? Type `y` and select from the grid shown. Or just press Enter for all.

   * **Filter by title substring?**
     Want only entries with a certain word in the title? Enter `y` and specify the word.

3. **Done!**
   Your exported XML files will appear in the `output/` directory, ready to import into MyAnimeList.

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
│   └── constants.py         # API URLs, statuses, ASCII art, quotes
├── main.py                  # Entry point
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

---

## 💡 Frequently Asked Questions

**Q: Do I need my AniList or MAL password?**
A: **Never!** AniMal will *never* ask for your password. To access private entries, you authorize using AniList's official OAuth process (ID, secret, and browser-based approval).

**Q: Where are my exported files?**
A: In the `output/` folder, as XML files:

* `your_anilist_username_anime.xml`
* `your_anilist_username_manga.xml`

**Q: What does the export include?**
A: Titles, scores (1–10), progress (episodes/chapters), status, dates, and your personal notes.

**Q: Can I use this on mobile or in Termux?**
A: Yes! AniMal is tested to work in Termux (Android), Linux, and Windows terminals.

**Q: Something went wrong, how do I get help?**
A: Type `-help` at any prompt for instant guidance, or [open an issue](https://github.com/itzraiyan/AniMal/issues).

---

## 📦 Understanding the Generated XML Files

AniMal generates XML files that are **fully compatible with MyAnimeList (MAL)**. These files are rich, detailed, and advanced, containing everything MAL expects for a smooth import. Here’s what you get:

- **User Block (`myinfo`):**
  - Your username and user ID (if MAL username provided)
  - Export type (anime or manga)
  - Total count of entries and advanced stats (completed, watching/reading, on-hold, dropped, plan to watch/read, etc.)

- **Entry Blocks (`anime` or `manga`):**
  - **IDs:** Both AniList and MAL database IDs when available
  - **Title:** Full romanized title (with support for special characters)
  - **Episodes/Chapters/Volumes:** All progress recorded
  - **Status:** Accurate mapping from AniList (including "repeating", "paused", etc.)
  - **Dates:** Start and finish dates (in proper MAL format)
  - **Scores:** 1–10 scale, supports decimal and integer scores
  - **Notes/Comments:** Any notes you’ve attached on AniList are preserved
  - **Tags:** (if available)
  - **Rewatch/Re-read status:** Progress and flags
  - **Privacy:** Both public and private entries (if you used OAuth)

- **Advanced Features:**
  - All fields are mapped intelligently so MAL can import them without errors.
  - Handles edge cases like missing values, partial progress, unknown titles, and more.
  - Output is **standards-compliant XML**—no hacks, no missing data, no broken imports.

**Why is this awesome?**  
AniMal’s export is not a basic list dump: it’s a complete, detailed, and robust migration tool. Whether you’re a power user with tons of custom notes, a casual with only partial lists, or someone with lots of private entries—everything is exported, safely and accurately.

---

## 🤝 Contributing

All contributions are welcome!
To get started:

1. **Fork** this repository
2. **Create a branch:**
   `git checkout -b feature/your-feature`
3. **Make your changes**
4. **Commit:**
   `git commit -m 'Describe your feature'`
5. **Push:**
   `git push origin feature/your-feature`
6. **Open a Pull Request** on GitHub

---

## 📜 License

AniMal is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

**Happy exporting!** ✨  
If AniMal helped you, please ⭐ star the repo and share with fellow anime/manga fans!
