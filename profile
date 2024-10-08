### Variables ###
export BROWSER="qutebrowser"
export EDITOR="code"
export VISUAL="$EDITOR"
export PATH="$PATH:$HOME/bin:$HOME/bin/go/bin:$HOME/.emacs.d/bin"
export VIEW_PDF="zathura" # for latex-makefile
# export TERMINAL="termite"
export TERMINAL="kitty"
export PYTHONSTARTUP=~/.config/startup.py
export ARDUINO_PATH=/usr/share/arduino

### ccache ###
export PATH="/usr/lib/ccache/bin/:$PATH"
# export CCACHE_PREFIX=$(which cope)

### settings
export SUDO_PROMPT=$'\033[33m[sudo]\033[0m password for \033[32m%u@%h\033[0m (-> \033[31m%U\033[0m): '
export QT_QPA_PLATFORMTHEME='qt5ct'
export QT_AUTO_SCREEN_SCALE_FACTOR=0
export DOTNET_CLI_TELEMETRY_OPTOUT=1
export CM_LAUNCHER=rofi  # clipmenu
export RANGER_DEVICONS_SEPARATOR='  '
export _JAVA_OPTIONS='-Dawt.useSystemAAFontSettings=lcd'
export AWT_TOOLKIT=MToolkit  # fix blank windows
export PIP_REQUIRE_VIRTUALENV=1
export QUTE_QT_WRAPPER=PyQt6
export SWEETHOME3D_JAVA3D=1.6   # fix 3D not working

### ndless
#export PATH="/home/florian/code/Ndless/ndless-sdk/toolchain/install/bin:/home/florian/code/Ndless/ndless-sdk/bin:$PATH"

### pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"

### poetry
export PATH="$HOME/.poetry/bin:$PATH"

source ~/.profile-private
