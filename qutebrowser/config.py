c.tabs.background = True
c.new_instance_open_target = 'window'
c.downloads.position = 'bottom'

config.bind(',ce', 'config-edit')
config.bind(',rta', 'open {url}top/?sort=top&t=all')
config.bind(',p', 'config-cycle -p content.plugins ;; reload')

css = '~/code/solarized-everything-css/css/solarized-all-sites-dark.css'
config.bind(',n', f'config-cycle content.user_stylesheets {css} "" ;; reload')
