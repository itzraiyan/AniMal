import os
import random  # ADDED MISSING IMPORT
import textwrap
from colorama import Fore, Style, init as colorama_init
from config import constants

# Initialize colorama
colorama_init(autoreset=True)

def get_terminal_width():
    """Get terminal width with fallback"""
    try:
        return os.get_terminal_size().columns
    except OSError:
        return 80  # Default width

def color_text(text, color):
    return getattr(Fore, color.upper(), "") + text + Style.RESET_ALL

def print_help(helpmsg):
    """Print clean help text without distortion"""
    # Get terminal width
    width = min(80, get_terminal_width())
    
    # Split into sections
    sections = helpmsg.strip().split('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
    
    # Print top border
    print(color_text("┌" + "─" * (width-2) + "┐", "CYAN"))
    
    for section_idx, section in enumerate(sections):
        # Process each line in section
        lines = section.split('\n')
        for line in lines:
            # Wrap long lines
            wrapped = textwrap.wrap(line, width=width-4)
            if not wrapped:
                wrapped = [""]
                
            for wline in wrapped:
                # Pad and print each line
                padded = wline.ljust(width-4)
                print(color_text(f"│ {padded} │", "CYAN"))
        
        # Add separator between sections
        if section_idx < len(sections) - 1:
            print(color_text("├" + "─" * (width-2) + "┤", "CYAN"))
    
    # Print bottom border
    print(color_text("└" + "─" * (width-2) + "┘", "CYAN"))

def boxed_text(text, color="WHITE", width=None):
    """Clean boxed text without distortion"""
    if width is None:
        width = min(60, get_terminal_width() - 10)
    
    lines = textwrap.wrap(text, width=width) or ['']
    maxlen = max(len(line) for line in lines)
    
    top = '┌' + '─' * (maxlen + 2) + '┐'
    bot = '└' + '─' * (maxlen + 2) + '┘'
    mid = [f"│ {line.ljust(maxlen)} │" for line in lines]
    
    return color_text('\n'.join([top] + mid + [bot]), color)

def prompt_boxed(msg, default=None, color="MAGENTA", width=None, helpmsg=None):
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
