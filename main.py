# ---------------------------
# [i] Oblivion, 2024 by MF366
# ---------------------------
from argparse import ArgumentParser, Namespace
import oblivion
from typing import SupportsBytes
from write import write
from write import init as write_init
import os, sys
from datetime import datetime
from colorama import Fore as fg

def clear() -> SupportsBytes | str:
    if sys.platform == "win32":
        os.system("cls")
        return sys.platform
    
    os.system("clear")
    return sys.platform

parser: ArgumentParser = ArgumentParser("Oblivion")

clear()

write(f"""{fg.RED}
 ██████╗ ██████╗ ██╗     ██╗██╗   ██╗██╗ ██████╗ ███╗   ██╗
██╔═══██╗██╔══██╗██║     ██║██║   ██║██║██╔═══██╗████╗  ██║
██║   ██║██████╔╝██║     ██║██║   ██║██║██║   ██║██╔██╗ ██║
██║   ██║██╔══██╗██║     ██║╚██╗ ██╔╝██║██║   ██║██║╚██╗██║
╚██████╔╝██████╔╝███████╗██║ ╚████╔╝ ██║╚██████╔╝██║ ╚████║
 ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                    {fg.YELLOW}(MF366, 2024){fg.RESET}

""", False)

parser.add_argument("url", type=str, help="The URL you want to send to use Oblivion on.")
parser.add_argument("-k", "--keywords", type=str, help="Path to a file that contains the keywords to search.", default="")
parser.add_argument("-r", "--redirects", action="store_true", help="When used, will allow redirects on the URL.", default=False)

args: Namespace = parser.parse_args()

def __get_local_folder(__f: str) -> str:
    return os.path.join(os.path.dirname(__file__), __f)

__reports = __get_local_folder("reports")

if not os.path.exists(__reports):
    os.mkdir(__reports)

f = open(os.path.join(__reports, f"Report_{datetime.now().day}-{datetime.now().month}-{datetime.now().year}_{args.url.split('/')[2]}.txt"), "w", encoding="utf-8")
f.write("=" * len("= REPORT ="))
f.write("= REPORT =")
f.write("=" * len("= REPORT ="))
f.write("\n")

write_init(f)

oblivion.start(args.url, args.keywords, args.redirects, f)
