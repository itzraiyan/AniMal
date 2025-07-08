import random
import textwrap
from config.constants import ASCII_BANNERS, QUOTES

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    class DummyColors:
        RED = GREEN = YELLOW = CYAN = MAGENTA = WHITE = RESET = ""
    Fore = Style = DummyColors()

def color_text(text, color):
    return getattr(Fore, color.upper()) + text + Style.RESET_ALL

def boxed_text(text, color="WHITE", width=60):
    lines = textwrap.wrap(text, width=width) or ['']
    max_len = max(len(line) for line in lines)
    border = '─' * (max_len + 2)
    box = [
        f"┌{border}┐",
        *[f"│ {line.ljust(max_len)} │" for line in lines],
        f"└{border}┘"
    ]
    return color_text('\n'.join(box), color)

def prompt_boxed(msg, default=None, color="MAGENTA", width=60, helpmsg=None):
    while True:
        full_msg = f"{msg}{f' [{default}]' if default else ''}"
        print(boxed_text(full_msg, color, width))
        user_input = input("> ").strip()
        if user_input == "-help" and helpmsg:
            print(boxed_text(helpmsg, "CYAN", width))
            continue
        return user_input or default

def confirm_overwrite(filename):
    print(boxed_text(f"Overwrite {filename}? (y/N)", "YELLOW"))
    return input("> ").lower() == 'y'

def print_error(msg): print(boxed_text(f"ERROR: {msg}", "RED"))
def print_success(msg): print(boxed_text(msg, "GREEN"))
def print_info(msg): print(boxed_text(msg, "CYAN"))

def print_banner():
    banner = random.choice(ASCII_BANNERS)
    print(color_text(banner, "CYAN"))

def print_outro():
    outro = [
        "Thanks for using AniMal! 🐾",
        "Follow your anime dreams!",
        random.choice(QUOTES)
    ]
    print(color_text('\n'.join(outro), "YELLOW"))
