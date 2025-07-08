import os
import random
import textwrap
from colorama import Fore, Style, init as colorama_init
from config import constants

# Initialize colorama
colorama_init(autoreset=True)

def get_terminal_width(default=80):
    """Get terminal width dynamically with fallback"""
    try:
        return os.get_terminal_size().columns
    except OSError:
        return default

def color_text(text, color):
    return getattr(Fore, color.upper(), "") + text + Style.RESET_ALL

def print_help(helpmsg):
    """Print responsive help text for Termux"""
    # Get terminal width
    width = min(100, get_terminal_width() - 4)
    
    # Create border
    border = "━" * (width - 2)
    top_border = f"┏{border}┓"
    bottom_border = f"┗{border}┛"
    
    # Print help with responsive wrapping
    print(color_text(top_border, "CYAN"))
    for paragraph in helpmsg.strip().split('\n\n'):
        wrapped = textwrap.fill(
            paragraph, 
            width=width,
            replace_whitespace=False
        )
        for line in wrapped.split('\n'):
            print(color_text(f"┃ {line.ljust(width-2)} ┃", "CYAN"))
    print(color_text(bottom_border, "CYAN"))

def boxed_text(text, color="WHITE", width=None):
    """Responsive boxed text for Termux"""
    if width is None:
        width = min(60, get_terminal_width() - 10)
    
    lines = []
    for paragraph in text.split('\n'):
        lines.extend(textwrap.wrap(paragraph, width=width) or [''])
    
    if not lines:
        lines = ['']
        
    maxlen = max(len(line) for line in lines)
    top = '┌' + '─' * (maxlen + 2) + '┐'
    bot = '└' + '─' * (maxlen + 2) + '┘'
    mid = [f"│ {line.ljust(maxlen)} │" for line in lines]
    box = [top] + mid + [bot]
    return color_text('\n'.join(box), color)

def prompt_boxed(msg, default=None, color="MAGENTA", width=None, helpmsg=None):
    """Prompt with responsive help for Termux"""
    while True:
        prompt_str = f"{msg}" + (f" [{default}]" if default else "")
        print(boxed_text(prompt_str, color, width))
        val = input("> ").strip()
        if val.lower() in ["-help", "--help", "help", "-h", "?"]:
            if helpmsg:
                print_help(helpmsg)
            continue
        return val if val else default

def confirm_overwrite(filename):
    print(boxed_text(
        f"File '{filename}' exists.\nOverwrite? (y/N)", "YELLOW"
    ))
    ans = input("> ").strip().lower()
    return ans == 'y'

def print_error(msg):
    print(boxed_text("Error: " + msg, "RED"))

def print_success(msg):
    print(boxed_text(msg, "GREEN"))

def print_info(msg):
    print(boxed_text(msg, "CYAN"))

def print_banner():
    print(color_text(random.choice(constants.ASCII_BANNERS), "CYAN"))

def print_outro():
    print(color_text("\n".join([
        "Thanks for using AniMal! 🐾",
        "Follow your anime dreams!",
        random.choice(constants.QUOTES)
    ]), "YELLOW"))
