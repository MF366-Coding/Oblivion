from sys import stdout
from typing import Iterable

__f = None

def init(file):
    global __f
    
    __f = file

def write(__s: str, __report: bool = True) -> int:
    if __report:
        __f.write(__s)
    
    return stdout.write(__s)
    
def writelines(__lines: Iterable[str]) -> None:
    return stdout.writelines(__lines)
