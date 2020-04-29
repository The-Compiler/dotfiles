#!/usr/bin/zsh
### General options ###
# Report time if command runs >2s
REPORTTIME=2
# display PID when suspending processes
setopt longlistjobs
# report status of background jobs
setopt notify
# don't kill background jobs
setopt nohup
# pkgfile command_not_found handler
if [[ -f /usr/share/doc/pkgfile/command-not-found.zsh ]]; then
    source /usr/share/doc/pkgfile/command-not-found.zsh
fi
# easy color names in this config
autoload -U colors && colors

### History ###
# Path to the history file
HISTFILE=$HOME/.zsh_history
# Size of the history and how much to actually save
HISTSIZE=5000
SAVEHIST=$HISTSIZE
# Ignore duplicate commands in the history
setopt hist_ignore_all_dups
# share history among other zsh sessions
setopt SHARE_HISTORY
# Ignore commands starting with a space
setopt hist_ignore_space

### Colors for ls ###
[[ -f ~/.dircolors ]] && eval $(dircolors ~/.dircolors) || eval $(dircolors)

### general colors ###
if which cope_path &>/dev/null; then
    export PATH="$(cope_path):$PATH"
fi

### Colors for less ###
export LESS="-R -M +g"
export LESS_TERMCAP_me=$(printf '\e[0m')
export LESS_TERMCAP_se=$(printf '\e[0m')
export LESS_TERMCAP_ue=$(printf '\e[0m')
export LESS_TERMCAP_mb=$(printf '\e[1;32m')
export LESS_TERMCAP_md=$(printf '\e[1;34m')
export LESS_TERMCAP_us=$(printf '\e[1;32m')
export LESS_TERMCAP_so=$(printf '\e[1;44;1m')

### keybindings ###
# vi mode
bindkey -v
# home/end (urxvt)
bindkey "\e[7~" beginning-of-line
bindkey "\e[8~" end-of-line
# home/end (xterm)
bindkey "\e[1~" beginning-of-line
bindkey "\e[4~" end-of-line
bindkey "\e[H" beginning-of-line
bindkey "\e[F" end-of-line
# Shift=Tab (completion)
bindkey "\e[Z" reverse-menu-complete
# insert
bindkey "\e[2~" overwrite-mode
# delete
bindkey "\e[3~" delete-char
# history search with started command
bindkey "\e[A" up-line-or-search
bindkey "\e[B" down-line-or-search
# Ctrl+R
bindkey '^R' history-incremental-search-backward
# / in command mode
bindkey -M vicmd '/' history-incremental-search-backward

### aliases / functions ###
# default settings
alias ls='ls --color --classify'
alias l='ls --color --classify -lah'
alias grep='grep --color=auto'
alias nano='nano --nowrap'
alias dmesg='dmesg --human --decode --nopager'
# shorthands
alias hc='herbstclient'
alias yu='yaourt -Suya; sudo abs; sudo pkgfile -u; gpg --refresh-keys; gpg --update-trustdb; sudo pacdiffviewer'
alias tx='tmux -2 attach -d'
alias fap='fahrplan -f'
# pseudo-functions
alias pymath='bpython -i <(echo "from math import *")'
alias newx='xinit /usr/bin/urxvt -- :1'
alias nmapa='sudo nmap -T Aggressive -P0 -sT -p 1-65535'
alias leech='wget -r -np -l inf -N -kK -E'
alias oregano='thyme show -i ~/.local/share/thyme.json -w stats > /tmp/thyme.html && qutebrowser /tmp/thyme.html'
# functions
sumcol() { awk 'BEGIN { sum=0 } { sum += $1 } END { print sum }' }
xoj() { for f in "$@"; do xournal "$f" &>/dev/null & disown; done }
pdf() { "$VIEW_PDF" "$@" &>/dev/null & disown }
qr() { qrencode "$1" -o- -t ANSIUTF8; }
genpwd() { tr -dc A-Za-z0-9 < /dev/urandom | head -c 8; echo }
igitt() { git clone "ssh://git@tonks/$1" ;}
bashhelp() { bash -c "help -m '$1'" | $PAGER ;}
pyedit() { vim "${1//.//}.py" }
# ignore dangerous commands from history and make them safer
alias rm='rm -I'
alias chmod=' chmod -c'
alias chown=' chown -c'
alias shred=' shred -u -z'
alias cp='cp -i'
alias mv='mv -i'
alias bell='echo -e "\a"'
alias mi='miiocli airpurifier  --ip $MIROBO_IP --token $MIROBO_TOKEN'

### completion ###
# init completion
autoload -U compinit && compinit
# display menu if there are >5 completions
zstyle ':completion:*' menu select=5 
# use colors for file completion
zstyle ':completion:*:default' list-colors ${(s.:.)LS_COLORS}
# use groups for completion
zstyle ':completion:*:descriptions' format \
    "%{$fg[red]%}completing %B%d%b%{$reset_color%}"
zstyle ':completion:*:matches' group 'yes'
zstyle ':completion:*' group-name ''
# warn if there are no matches
zstyle ':completion:*:warnings' format \
    "%{$fg[red]%}No matches for:%{$reset_color%} %d"
# display all processes for killall/...
zstyle ':completion:*:processes-names' command \
    'ps c -u ${USER} -o command | uniq'
# group man pages per section
zstyle ':completion:*:manuals' separate-sections true
zstyle ':completion:*:manuals.*' insert-sections true
# match uppercase with lowercase chars
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Z}'
# verbose output
zstyle ':completion:*' verbose true
# show file types
setopt listtypes

### Prompt ###
setopt prompt_subst
autoload -Uz vcs_info
zstyle ':vcs_info:*' stagedstr '%F{green}•%f'
zstyle ':vcs_info:*' unstagedstr '%F{red}•%f'
zstyle ':vcs_info:*' check-for-changes true
zstyle ':vcs_info:(sv[nk]|bzr):*' branchformat '%b:%r'
zstyle ':vcs_info:*' enable git svn bzr hg
zstyle ':vcs_info:*' formats '%F{blue}──[%f%F{red}%s/%b%c%u%m%F{blue}]%f'

venv_prompt_info() {
    if [[ -n "$VIRTUAL_ENV" ]]; then
        if [[ -f "$VIRTUAL_ENV/__name__" ]]; then
            local name=$(cat "$VIRTUAL_ENV/__name__")
        elif [[ $(basename $VIRTUAL_ENV) = "__" ]]; then
            local name=$(basename $(dirname "$VIRTUAL_ENV"))
        else
            local name=$(basename "$VIRTUAL_ENV")
        fi
        echo "${prompt_startsep}%F{red}venv:$name%f${prompt_endsep}"
    fi
}

disp_prompt_info() {
    if [[ -n "$DISPLAY" && "$DISPLAY" != ":0" ]]; then
        echo "${prompt_startsep}%F{red}disp:$DISPLAY%f${prompt_endsep}"
    fi
}

setprompt() {
    local reset="%{$reset_color%}"
    local upper_start='%F{blue}─[%f'
    local other_start='%F{blue}┄─[%f'
    local other_end=']─╼ ${reset}'
    local userhost='%F{green}%n@%m%f'
    local sep='%F{blue}]──[%f'
    prompt_startsep='%F{blue}──[%f'
    prompt_endsep='%F{blue}]%f'
    local fade='%F{blue}────┄%f'
    local dir='%F{red}%~%f'
    local date='%F{yellow}%D%f'
    local dtime='%F{yellow}%T%f'
    local job="%(1j.${prompt_startsep}%F{red}%j job.)%(2j.s.)%(1j.${prompt_endsep}.)%f"
    local vcs='${vcs_info_msg_0_}'
    if [[ -n $RANGER_LEVEL ]]; then
        local ranger="${prompt_startsep}%F{red}ranger"
        (( RANGER_LEVEL > 1 )) && ranger+=":$RANGER_LEVEL"
        ranger+="%f${prompt_endsep}"
    else
        local ranger=
    fi
    local rootwarn='%(!.%F{blue}(%f%F{red}!%f%F{blue}).)%f'
    local promptchar='%F{blue}─╼ %f'
    local n=$'\n'
    local rstatus='%(?..%F{red}╾─[%F{blue}$?%F{red}]──┄)'

    export VIRTUAL_ENV_DISABLE_PROMPT=1
    PROMPT="${upper_start}${userhost}${sep}${dir}${sep}${date}${sep}"
    PROMPT+="${dtime}${prompt_endsep}${job}\$(venv_prompt_info)${vcs}${ranger}"
    PROMPT+="\$(disp_prompt_info)${fade}$n"

    #PROMPT+="${lower_start}${rootwarn}${promptchar}${reset}"

    PROMPT2="${other_start}%_${other_end}"
    PROMPT3="${other_start}?${other_end}"
    PROMPT4="${other_start}%N:%i${other_end}"
    RPROMPT="${rstatus}${reset}"
}

setprompt

### Hooks ###
preexec() { # Gets run before a command gets executed
    # Set screen/tmux window title
    echo -ne "\e]0;$1\e\\" || 
}
precmd() { # gets run after a command before the prompt
    # Reset screen/tmux window title
    echo -ne "\e]0;zsh\e\\"
    # Generate vcs_info
    vcs_info
}

### Autorun tmux ###
if [[ -z "$TMUX" && -n "$SSH_CONNECTION" ]]; then
    tmux -2 attach -d
fi

### Syntax highlighting ###
highlight=
for d in zsh-syntax-highlight{,ing}; do
    f="/usr/share/zsh/plugins/$d/zsh-syntax-highlighting.zsh"
    [[ -f "$f" ]] && source "$f" && highlight=true
done
if [[ -n "$highlight" ]]; then
    ZSH_HIGHLIGHT_HIGHLIGHTERS=(main brackets)
    ZSH_HIGHLIGHT_STYLES[globbing]='fg=cyan'
    ZSH_HIGHLIGHT_STYLES[single-hyphen-option]='fg=magenta'
    ZSH_HIGHLIGHT_STYLES[double-hyphen-option]='fg=magenta'
    ZSH_HIGHLIGHT_STYLES[back-quoted-argument]='fg=yellow'
    ZSH_HIGHLIGHT_STYLES[path]='bold'
    ZSH_HIGHLIGHT_STYLES[unknown-token]='fg=red'
fi

### Humble bundle key ###
[[ -f ~/.humblebundle ]] && source ~/.humblebundle
[[ -f ~/.deltachat ]] && source ~/.deltachat


## infsi1
viewcert() {
    openssl x509 -in "$1" -noout -text
}

## pyenv
export PATH="/home/florian/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
