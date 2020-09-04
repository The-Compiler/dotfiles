sy on
set ts=4 sts=4 sw=4 et
set nu
set belloff=error,esc,wildmode  " Disable terminal bell in some situations

if empty(glob('~/.vim/autoload/plug.vim'))
  silent !curl -fLo ~/.vim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
endif

" https://github.com/junegunn/vim-plug
call plug#begin('~/.vim/plugged')
Plug 'morhetz/gruvbox'
call plug#end()

let g:gruvbox_italic=1
" let g:gruvbox_contrast_dark='hard'
set background=dark
colorscheme gruvbox

" if &diff
"   colorscheme github
" endif
