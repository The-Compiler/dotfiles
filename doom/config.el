;;; $DOOMDIR/config.el -*- lexical-binding: t; -*-

;; Place your private configuration here! Remember, you do not need to run 'doom
;; sync' after modifying this file!


;; Some functionality uses this to identify you, e.g. GPG configuration, email
;; clients, file templates and snippets.
(setq user-full-name "Florian Bruhin"
      user-mail-address "me@the-compiler.org")

;; Doom exposes five (optional) variables for controlling fonts in Doom. Here
;; are the three important ones:
;;
;; + `doom-font'
;; + `doom-variable-pitch-font'
;; + `doom-big-font' -- used for `doom-big-font-mode'; use this for
;;   presentations or streaming.
;;
;; They all accept either a font-spec, font string ("Input Mono-12"), or xlfd
;; font string. You generally only need these two:
;; (setq doom-font (font-spec :family "monospace" :size 12 :weight 'semi-light)
;;       doom-variable-pitch-font (font-spec :family "sans" :size 13))

(setq doom-font (font-spec :family "Iosevka Nerd Font" :size 15 :weight 'medium)
      doom-big-font (font-spec :family "Iosevka Nerd Font" :size 30 :weight 'medium)
      doom-variable-pitch-font (font-spec :family "sans" :size 13))

;; There are two ways to load a theme. Both assume the theme is installed and
;; available. You can either set `doom-theme' or manually load a theme with the
;; `load-theme' function. This is the default:
(setq doom-theme 'gruvbox)

;; If you use `org' and don't want your org files in the default location below,
;; change `org-directory'. It must be set before org loads!
(setq org-directory "~/org/")

;; This determines the style of line numbers in effect. If set to `nil', line
;; numbers are disabled. For relative line numbers, set this to `relative'.
(setq display-line-numbers-type t)


;; Here are some additional functions/macros that could help you configure Doom:
;;
;; - `load!' for loading external *.el files relative to this one
;; - `use-package!' for configuring packages
;; - `after!' for running code after a package has loaded
;; - `add-load-path!' for adding directories to the `load-path', relative to
;;   this file. Emacs searches the `load-path' when you load packages with
;;   `require' or `use-package'.
;; - `map!' for binding new keys
;;
;; To get information about any of these functions/macros, move the cursor over
;; the highlighted symbol at press 'K' (non-evil users must press 'C-c c k').
;; This will open documentation for it, including demos of how they are used.
;;
;; You can also try 'gd' (or 'C-c c d') to jump to their definition and see how
;; they are implemented.

; (minimap-mode)
(custom-set-faces!
  '(minimap-active-region-background :background "#3c3836")
  '(minimap-current-line-face :background "#504945"))

;; for magit force
(setq auth-sources '("~/.authinfo"))

;; https://github.com/hlissner/doom-emacs/issues/2688
; (setq confirm-kill-emacs nil)

;; FIXME doesn't seem to work?
;; zoom keys
(global-set-key (kbd "C-+") 'text-scale-increase)
(global-set-key (kbd "C--") 'text-scale-decrease)
(global-set-key (kbd "C-=") (lambda () (interactive) (text-scale-set 0)))
;; SPC /
(map! :leader :desc "Search project" "p /" #'+default/search-project)

;; Never use pylint for flycheck (fails to load qute_pylint)
(after! flycheck (setq-default flycheck-disabled-checkers '(python-pylint)))

;; Don't display DOOM ascii banner
(remove-hook '+doom-dashboard-functions 'doom-dashboard-widget-banner)

;; nicer magit diffs
(magit-delta-mode)

;; Various customizations
;; most from https://tecosaur.github.io/emacs-config/config.html
(setq-default
 tab-width 4
 uniquify-buffer-name-style 'forward
 window-combination-resize t
 evil-want-fine-undo t
 truncate-string-ellipsis "…")

(global-subword-mode)
(mouse-avoidance-mode 'exile)

;; Prompt for buffer after splitting
;; From https://tecosaur.github.io/emacs-config/config.html
(setq evil-vsplit-window-right t
      evil-split-window-below t)
(defadvice! prompt-for-buffer (&rest _)
  :after '(evil-window-split evil-window-vsplit)
  (+ivy/projectile-find-file))
(setq +ivy-buffer-preview t)

;; Others from tecosaur
(setq which-key-idle-delay 0.4)

;; Custom modes
(use-package! feature-mode :mode ("\\.feature\\'" . feature-mode))
(add-to-list 'auto-mode-alist '("\\.feature\\'" . 'feature-mode))
