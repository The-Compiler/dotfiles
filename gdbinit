## Python
source /home/florian/proj/cpython/Misc/gdbinit

## Qt
python
import sys

# Qt support from KDevelop
sys.path.insert(0, '/usr/share/kdevgdb/printers/')
from qt import register_qt_printers
register_qt_printers(None)

# Qt support from Qt Creator (uses 'pp' so shouldn't conflict)
sys.path.insert(0, '/usr/share/qtcreator/debugger/')
from gdbbridge import *
end

## pwndbg
# source /usr/share/pwndbg/gdbinit.py
# source /home/florian/.gdbinit-gef.py
# source /home/florian/proj/peda/peda.py

set debuginfod enabled ask
