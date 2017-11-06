c.tabs.background = True
c.new_instance_open_target = 'window'
c.downloads.position = 'bottom'
c.spellcheck.languages = ['en-US']

config.bind(',ce', 'config-edit')
config.bind(',rta', 'open {url}top/?sort=top&t=all')
config.bind(',p', 'config-cycle -p content.plugins ;; reload')

css = '~/code/solarized-everything-css/css/solarized-all-sites-dark.css'
config.bind(',n', f'config-cycle content.user_stylesheets {css} "" ;; reload')

c.url.searchengines['rfc'] = 'https://tools.ietf.org/html/rfc{}'

c.fonts.tabs = '8pt monospace'
c.fonts.statusbar = '8pt monospace'
