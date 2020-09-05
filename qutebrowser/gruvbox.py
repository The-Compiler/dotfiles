# gruvbox dark hard qutebrowser theme by Florian Bruhin <me@the-compiler.org>
#
# Originally based on:
#   base16-qutebrowser (https://github.com/theova/base16-qutebrowser)
#   Base16 qutebrowser template by theova and Daniel Mulford
#   Gruvbox dark, hard scheme by Dawid Kurek (dawikur@gmail.com), morhetz (https://github.com/morhetz/gruvbox)

bg0_hard = "#1d2021"
# bg0_soft = '#32302f'
# bg0 = '#282828'
bg1 = "#3c3836"
bg2 = "#504945"
bg3 = "#665c54"
bg4 = "#7c6f64"

# fg0 = "#fbf1c7"
# fg1 = "#ebdbb2"
fg2 = "#d5c4a1"
fg3 = "#bdae93"
fg4 = "#a89984"

bright_red = "#fb4934"
bright_green = "#b8bb26"
bright_yellow = "#fabd2f"
bright_blue = "#83a598"
bright_purple = "#d3869b"
bright_aqua = "#8ec07c"
bright_gray = "#928374"
bright_orange = "#fe8019"

dark_red = "#cc241d"
# dark_green = "#98971a"
# dark_yellow = "#d79921"
# dark_blue = "#458588"
# dark_purple = "#b16286"
# dark_aqua = "#689d6a"
# dark_gray = "#a89984"
# dark_orange = "#d65d0e"

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
c.colors.completion.fg = fg2

# Background color of the completion widget for odd rows.
c.colors.completion.odd.bg = bg0_hard

# Background color of the completion widget for even rows.
c.colors.completion.even.bg = bg0_hard

# Foreground color of completion widget category headers.
c.colors.completion.category.fg = bright_blue

# Background color of the completion widget category headers.
c.colors.completion.category.bg = bg0_hard

# Top border color of the completion widget category headers.
c.colors.completion.category.border.top = bg0_hard

# Bottom border color of the completion widget category headers.
c.colors.completion.category.border.bottom = bg0_hard

# Foreground color of the selected completion item.
c.colors.completion.item.selected.fg = fg2

# Background color of the selected completion item.
c.colors.completion.item.selected.bg = bg2

# Top border color of the selected completion item.
c.colors.completion.item.selected.border.top = bg2

# Bottom border color of the selected completion item.
c.colors.completion.item.selected.border.bottom = bg2

# Foreground color of the matched text in the selected completion item.
c.colors.completion.item.selected.match.fg = fg2

# Foreground color of the matched text in the completion.
c.colors.completion.match.fg = bright_orange

# Color of the scrollbar handle in the completion view.
c.colors.completion.scrollbar.fg = fg2

# Color of the scrollbar in the completion view.
c.colors.completion.scrollbar.bg = bg0_hard

# Background color of disabled items in the context menu.
c.colors.contextmenu.disabled.bg = bg1

# Foreground color of disabled items in the context menu.
c.colors.contextmenu.disabled.fg = fg3

# Background color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.bg = bg0_hard

# Foreground color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.fg =  fg2

# Background color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.bg = bg2

#Foreground color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.fg = fg2

# Background color for the download bar.
c.colors.downloads.bar.bg = bg0_hard

# Color gradient start for download text.
c.colors.downloads.start.fg = bg0_hard

# Color gradient start for download backgrounds.
c.colors.downloads.start.bg = bright_blue

# Color gradient end for download text.
c.colors.downloads.stop.fg = bg0_hard

# Color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = bright_aqua

# Foreground color for downloads with errors.
c.colors.downloads.error.fg = bright_red

# Font color for hints.
c.colors.hints.fg = bg0_hard

# Background color for hints.
c.colors.hints.bg = 'rgba(250, 191, 47, 200)'  # bright_yellow

# Font color for the matched part of hints.
c.colors.hints.match.fg = dark_red

# Text color for the keyhint widget.
c.colors.keyhint.fg = fg2

# Highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = fg3

# Background color of the keyhint widget.
c.colors.keyhint.bg = bg0_hard

# Foreground color of an error message.
c.colors.messages.error.fg = bg0_hard

# Background color of an error message.
c.colors.messages.error.bg = bright_red

# Border color of an error message.
c.colors.messages.error.border = bright_red

# Foreground color of a warning message.
c.colors.messages.warning.fg = bg0_hard

# Background color of a warning message.
c.colors.messages.warning.bg = bright_purple

# Border color of a warning message.
c.colors.messages.warning.border = bright_purple

# Foreground color of an info message.
c.colors.messages.info.fg = fg2

# Background color of an info message.
c.colors.messages.info.bg = bg0_hard

# Border color of an info message.
c.colors.messages.info.border = bg0_hard

# Foreground color for prompts.
c.colors.prompts.fg = fg2

# Border used around UI elements in prompts.
c.colors.prompts.border = f'1px solid {bg1}'

# Background color for prompts.
c.colors.prompts.bg = bg0_hard

# Background color for the selected item in filename prompts.
c.colors.prompts.selected.bg = bg2

# Foreground color of the statusbar.
c.colors.statusbar.normal.fg = fg2

# Background color of the statusbar.
c.colors.statusbar.normal.bg = bg0_hard

# Foreground color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = bright_aqua

# Background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = bg0_hard

# Foreground color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.fg = bright_yellow

# Background color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.bg = bg0_hard

# Foreground color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = bright_purple

# Background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = bg0_hard

# Foreground color of the statusbar in command mode.
c.colors.statusbar.command.fg = fg3

# Background color of the statusbar in command mode.
c.colors.statusbar.command.bg = bg1

# Foreground color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = bright_purple

# Background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = bg1

# Foreground color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = bright_blue

# Background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = bg0_hard

# Foreground color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = bright_blue

# Background color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.bg = bg0_hard

# Background color of the progress bar.
c.colors.statusbar.progress.bg = bright_blue

# Default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = fg2

# Foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = bright_red

# Foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = bright_orange

# Foreground color of the URL in the statusbar on successful load
# (http).
c.colors.statusbar.url.success.http.fg = bright_green

# Foreground color of the URL in the statusbar on successful load
# (https).
c.colors.statusbar.url.success.https.fg = bright_green

# Foreground color of the URL in the statusbar when there's a warning.
c.colors.statusbar.url.warn.fg = bright_purple

# Background color of the tab bar.
c.colors.tabs.bar.bg = bg0_hard

# Color gradient start for the tab indicator.
c.colors.tabs.indicator.start = bright_blue

# Color gradient end for the tab indicator.
c.colors.tabs.indicator.stop = bright_aqua

# Color for the tab indicator on errors.
c.colors.tabs.indicator.error = bright_red

# Foreground color of unselected odd tabs.
c.colors.tabs.odd.fg = fg2

# Background color of unselected odd tabs.
c.colors.tabs.odd.bg = bg2

# Foreground color of unselected even tabs.
c.colors.tabs.even.fg = fg2

# Background color of unselected even tabs.
c.colors.tabs.even.bg = bg3

# Background color of pinned unselected even tabs.
c.colors.tabs.pinned.even.bg = bright_green

# Foreground color of pinned unselected even tabs.
c.colors.tabs.pinned.even.fg = bg2

# Background color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.bg = bright_green

# Foreground color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.fg = bg2

# Background color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.bg = bg0_hard

# Foreground color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.fg = fg2

# Background color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.bg = bg0_hard

# Foreground color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.fg = fg2

# Foreground color of selected odd tabs.
c.colors.tabs.selected.odd.fg = fg2

# Background color of selected odd tabs.
c.colors.tabs.selected.odd.bg = bg0_hard

# Foreground color of selected even tabs.
c.colors.tabs.selected.even.fg = fg2

# Background color of selected even tabs.
c.colors.tabs.selected.even.bg = bg0_hard

# Background color for webpages if unset (or empty to use the theme's
# color).
c.colors.webpage.bg = bg4
