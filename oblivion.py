import requests
from bs4 import BeautifulSoup
import os
from colorama import Fore as fg
from write import write
import random, time

def raw_body(response: requests.Response):
    write(f"{fg.BLUE}HTML/Raw Body{fg.RESET}\n{fg.LIGHTCYAN_EX}{response.text}{fg.RESET}\n\n")

def keyword_parser(response: requests.Response, keywords: list | None = []):
    write(fg.BLUE)
    write("Keyword Parser\n")
    
    x = 1
    
    for keyword in keywords:
        if keyword in response.text:
            write(f'{fg.CYAN}[{x}] Keyword {fg.YELLOW}"{keyword}"{fg.CYAN} was found and appears {fg.YELLOW}{response.text.count(keyword)}{fg.CYAN} time(s).\n')
        else:
            write(f'{fg.RED}[{x}] Keyword {fg.YELLOW}"{keyword}"{fg.RED} was not found.\n')
        
        x += 1
        
    write(f"{fg.GREEN}All keywords parsed.\n\n{fg.RESET}")
    
def html_parser(response: requests.Response):
    write(fg.MAGENTA)
    
    write("HTML Parser\n")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')

    x = 1

    for link in links:
        if str(link.get('href')).replace(" ", "") == "":
            continue
        
        write(f"{fg.YELLOW}[{x}] Link found: {fg.CYAN}{link.get('href')}\n")
        x += 1
    
    write(fg.RESET)
    write(f"\n{fg.GREEN}All done!{fg.RESET}\n\n")
    

def redirect_parser(link: str):
    response: requests.Response = requests.get(link, timeout=5, allow_redirects=False)
    
    if response.status_code == 301 or response.status_code == 302:
        write(f"{fg.RED}Redirected to: {fg.RESET}{response.headers['Location']}\n\n")

    else:
        write(f'{fg.GREEN}No redirects.{fg.RESET}\n\n')

def status_code(response: requests.Response) -> int | str:
    if response.status_code == 200:
        write(fg.GREEN)
        
    else:
        write(fg.RED)
        
    write(f"\nStatus Code: {fg.RESET}{response.status_code}\n\n")
    
    return response.status_code

def start(link: str, keywords: str | None = None, redirects: bool = False, file = None):   
    words: list = []
    
    if os.path.exists(keywords):
        with open(os.path.abspath(keywords), "r", encoding="utf-8") as f:
            words = f.read().split("\n")
            f.close()
    
    write(f"\n{fg.YELLOW}Starting analysis")
    
    for dot in range(random.randint(5, 15)):
        write(".")
        time.sleep(random.random() * random.randint(1, 2) + random.randint(0, 1))
    
    response: requests.Response = requests.get(link, timeout=5, allow_redirects=redirects)
    
    write('\n\n')
    write(fg.RESET)
    
    raw_body(response)
    status_code(response)
    redirect_parser(link)
    keyword_parser(response, words)
    html_parser(response)
    
    file.close()
