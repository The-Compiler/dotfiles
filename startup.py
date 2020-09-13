import sys
from pprint import pprint as pp  # convenience

try:
    from rich import pretty
except ImportError:
    pass
else:
    pretty.install()
    del pretty

sys.ps1 = '\001\033[96m\002>>> \001\033[0m\002'
sys.ps2 = '\001\033[96m\002... \001\033[0m\002'
