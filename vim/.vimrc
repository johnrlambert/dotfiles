set nocompatible              " be iMproved, required
filetype off                  " required
set number
" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" The following are examples of different formats supported.
" Keep Plugin commands between vundle#begin/end.
" plugin on GitHub repo
Plugin 'Raimondi/delimitMate'
Plugin 'davidhalter/jedi-vim'
Plugin 'Yggdroot/indentLine'
Plugin 'tpope/vim-fugitive'
Plugin 'kchmck/vim-coffee-script'
Plugin 'scrooloose/nerdtree'
Plugin 'christoomey/vim-tmux-navigator'
Plugin 'flazz/vim-colorschemes'
Plugin 'kudabux/vim-srcery-drk'
Plugin 'hdima/python-syntax'
Plugin 'digitaltoad/vim-pug'
Plugin 'vim-syntastic/syntastic'
Plugin 'alfredodeza/coveragepy.vim'
" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line
"
" size of a hard tabstop
set tabstop=4

" always uses spaces instead of tab characters
set expandtab
"
" size of an indent"
set shiftwidth=4

" Enable NERDTree on every startup
autocmd vimenter * NERDTree

" Change bindings for navigation through buffers
nnoremap <c-j> <c-w>j
nnoremap <c-k> <c-w>k
nnoremap <c-h> <c-w>h
nnoremap <c-l> <c-w>l
" Persistent Undo
set undofile
set undodir=~/.vim/undodir
" Search functions
set hlsearch
" Color scheme info
colorscheme molokai

"Make pylint default linter for syntastic
let g:syntastic_python_checkers = ['pyflakes']
let g:syntastic_coffee_checkers = ['coffeelint']
"No more .pyc python turds
let NERDTreeIgnore = ['\.pyc$']

nnoremap <buffer> <F9> :exec '!python' shellescape(@%, 1)<cr>
" nnoremap <buffer> <F5> :normal iimport pdb; pdb.set_trace()<ESC>
command Pythoscope :exec '!pythoscope' | :exec 'vsplit tests/test_file.py'
