import sys



try:
    import rich.pretty
    import rich
except ImportError:
    pass
else:
    rich.pretty.install()
    help = rich.inspect
    print = rich.print
    del rich.pretty

def chunk(elems, n):
    for i in range(0, len(elems), n):
        yield elems[i:i+n]

sys.ps1 = '\001\033[96m\002>>> \001\033[0m\002'
sys.ps2 = '\001\033[96m\002... \001\033[0m\002'
