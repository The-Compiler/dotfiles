### Variables ###
export BROWSER="qutebrowser"
export EDITOR="emacs"
export VISUAL="$EDITOR"
export PATH="$PATH:$HOME/bin:$HOME/bin/go/bin"
export VIEW_PDF="zathura" # for latex-makefile
export TERMINAL="termite"

### ccache ###
export PATH="/usr/lib/ccache/bin/:$PATH"
export CCACHE_COMPRESS=1
export CCACHE_BASEDIR=$HOME
export CCACHE_PREFIX=$(which cope)

### settings
export SUDO_PROMPT='[sudo] password for %u@%h (-> %U): '
export GIT_PAGER='less +g'
export QT_QPA_PLATFORMTHEME='gtk2'

### ndless
export PATH="/home/florian/code/Ndless/ndless-sdk/toolchain/install/bin:/home/florian/code/Ndless/ndless-sdk/bin:$PATH"
