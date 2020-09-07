## Python
source /home/florian/proj/cpython/Misc/gdbinit


## Qt
python
import sys
sys.path.insert(0, '/usr/share/kdevgdb/printers/')

from qt import register_qt_printers
register_qt_printers(None)
end

## pwndbg
# source /usr/share/pwndbg/gdbinit.py
#source /home/florian/.gdbinit-gef.py
