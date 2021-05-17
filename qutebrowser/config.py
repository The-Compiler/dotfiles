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

css = '~/proj/solarized-everything-css/css/gruvbox/gruvbox-all-sites.css'
config.bind(',n', f'config-cycle content.user_stylesheets {css} ""')

c.url.searchengines['rfc'] = 'https://tools.ietf.org/html/rfc{}'
c.url.searchengines['pypi'] = 'https://pypi.org/project/{}/'
c.url.searchengines['qtbug'] = 'https://bugreports.qt.io/browse/QTBUG-{}'
c.url.searchengines['qb'] = 'https://github.com/The-Compiler/qutebrowser/issues/{}'
c.url.searchengines['btc'] = 'https://www.blockchain.com/btc/address/{}'
c.url.searchengines['http'] = 'https://httpstatuses.com/{}'
c.url.searchengines['duden'] = 'https://www.duden.de/suchen/dudenonline/{}'
c.url.searchengines['dictcc'] = 'https://www.dict.cc/?s={}'
#c.url.searchengines['maps'] = 'https://www.google.com/maps?q=%s'

c.aliases['ytdl'] = """spawn -v -m bash -c 'cd ~/vid/yt && youtube-dl "$@"' _ {url}"""

# c.fonts.tabs = '8pt monospace'
# c.fonts.statusbar = '8pt monospace'
c.fonts.web.family.fantasy = 'Arial'

c.search.incremental = False
c.editor.command = ['emacs', '{}']

#c.qt.args = ['ppapi-widevine-path=/usr/lib/qt/plugins/ppapi/libwidevinecdmadapter.so']

c.content.javascript.enabled = False
config.source('perdomain.py')
config.source('gruvbox.py')
