import sys
from pprint import pprint as pp  # convenience

try:
    from rich import pretty
except ImportError:
    pass
else:
    pretty.install()
    del pretty

def chunk(elems, n):
    for i in range(0, len(elems), n):
        yield elems[i:i+n]

sys.ps1 = '\001\033[96m\002>>> \001\033[0m\002'
sys.ps2 = '\001\033[96m\002... \001\033[0m\002'
