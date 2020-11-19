### Variables ###
export BROWSER="qutebrowser"
export EDITOR="emacs"
export VISUAL="$EDITOR"
export PATH="$PATH:$HOME/bin:$HOME/bin/go/bin:$HOME/.emacs.d/bin"
export VIEW_PDF="zathura" # for latex-makefile
# export TERMINAL="termite"
export TERMINAL="kitty"
export PYTHONSTARTUP=~/.config/startup.py
export ARDUINO_PATH=/usr/share/arduino

### ccache ###
export PATH="/usr/lib/ccache/bin/:$PATH"
export CCACHE_COMPRESS=1
export CCACHE_DIR=~/.cache/ccache
export CCACHE_BASEDIR=~
export CCACHE_PREFIX=$(which cope)

### settings
export SUDO_PROMPT=$'\033[33m[sudo]\033[0m password for \033[32m%u@%h\033[0m (-> \033[31m%U\033[0m): '
export QT_QPA_PLATFORMTHEME='qt5ct'
export QT_AUTO_SCREEN_SCALE_FACTOR=0
export DOTNET_CLI_TELEMETRY_OPTOUT=1
export CM_LAUNCHER=rofi  # clipmenu

### ndless
#export PATH="/home/florian/code/Ndless/ndless-sdk/toolchain/install/bin:/home/florian/code/Ndless/ndless-sdk/bin:$PATH"

source ~/.profile-private
