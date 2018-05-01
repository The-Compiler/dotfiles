config.load_autoconfig()

c.tabs.background = True
c.new_instance_open_target = 'window'
c.downloads.position = 'bottom'
c.spellcheck.languages = ['en-US']

config.bind(',ce', 'config-edit')
config.bind(',p', 'config-cycle -p content.plugins ;; reload')

config.bind(',rta', 'open {url}top/?sort=top&t=all')
config.bind(',rtv', 'spawn termite -e "rtv {url}"')
config.bind(',c', 'spawn -d chromium {url}')

css = '~/code/solarized-everything-css/css/solarized-all-sites-dark.css'
config.bind(',n', f'config-cycle content.user_stylesheets {css} ""')

c.url.searchengines['rfc'] = 'https://tools.ietf.org/html/rfc{}'
#c.url.searchengines['maps'] = 'https://www.google.com/maps?q=%s'

c.fonts.tabs = '8pt monospace'
c.fonts.statusbar = '8pt monospace'
c.fonts.web.family.fantasy = 'Arial'

c.search.incremental = False
c.editor.command = ['emacs', '{}']

c.qt.args = ['ppapi-widevine-path=/usr/lib/qt/plugins/ppapi/libwidevinecdmadapter.so']


c.content.javascript.enabled = False
config.source('perdomain.py')
