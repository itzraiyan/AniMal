import random
import textwrap
from colorama import Fore, Style, init as colorama_init
from config import constants

# Initialize colorama
colorama_init(autoreset=True)

def color_text(text, color):
    return getattr(Fore, color.upper(), "") + text + Style.RESET_ALL

def boxed_text(text, color="WHITE", width=60):
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

def prompt_boxed(msg, default=None, color="MAGENTA", width=60, helpmsg=None):
    while True:
        prompt_str = f"{msg}" + (f" [{default}]" if default else "")
        print(boxed_text(prompt_str, color, width))
        val = input("> ").strip()
        if val.lower() == "-help" and helpmsg:
            print(boxed_text(helpmsg, "CYAN", width))
            continue
        return val if val else default

def confirm_overwrite(filename):
    print(boxed_text(
        f"File '{filename}' already exists.\nOverwrite? (y/N)", "YELLOW", width=60
    ))
    ans = input("> ").strip().lower()
    return ans == 'y'

def print_error(msg):
    print(boxed_text("Error: " + msg, "RED", width=60))

def print_success(msg):
    print(boxed_text(msg, "GREEN", width=60))

def print_info(msg):
    print(boxed_text(msg, "CYAN", width=60))

def print_banner():
    print(color_text(random.choice(constants.ASCII_BANNERS), "CYAN"))

def print_outro():
    print(color_text("\n".join([
        "Thanks for using AniMal! 🐾",
        "Follow your anime dreams!",
        random.choice(constants.QUOTES)
    ]), "YELLOW"))
