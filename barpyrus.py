from barpyrus import hlwm
from barpyrus import widgets as W
from barpyrus.core import Theme
from barpyrus import lemonbar
from barpyrus import conky
import sys
# Copy this config to ~/.config/barpyrus/config.py

# set up a connection to herbstluftwm in order to get events
# and in order to call herbstclient commands
hc = hlwm.connect()

# get the geometry of the monitor
monitor = sys.argv[1] if len(sys.argv) >= 2 else 0
(x, y, monitor_w, monitor_h) = hc.monitor_rect(monitor)
height = 16 # height of the panel
width = monitor_w # width of the panel
hc(['pad', str(monitor), str(height)]) # get space for the panel

cg = conky.ConkyGenerator()

with cg.temp_fg(0x9fbc00):
    cg.symbol(0xe026)

cg.space()
for cpu in '1234':
    cg.var('cpu cpu' + cpu)
    cg.text('% ')

with cg.temp_fg(0x9fbc00):
    cg.symbol(0xe021)
cg.space()
cg.var('memperc')
cg.text('% ')

## Network
for iface, icon, extra in [('eth', 0xe0af, ''), ('wlan', 0xe21a, '${wireless_essid}'), ('ppp0', 0xe0f3, '')]:
    with cg.if_('up %s' % iface):
        with cg.temp_fg(0x9fbc00):
            cg.symbol(icon)
        if extra:
            cg.space()
            cg.text(extra)

        cg.space()
        with cg.temp_fg(0x9fbc00):
            cg.symbol(0xe13c)
        cg.var('downspeedf %s' % iface)
        cg.text('K')
        with cg.temp_fg(0x9fbc00):
            cg.symbol(0xe13b)
        cg.var('upspeedf %s' % iface)
        cg.text('K')

## Battery
# first icon: 0 percent
# last icon: 100 percent
bat_icons = [
    0xe242, 0xe243, 0xe244, 0xe245, 0xe246,
    0xe247, 0xe248, 0xe249, 0xe24a, 0xe24b,
]
bat_delta = 100 / len(bat_icons)

with cg.if_('existing /sys/class/power_supply/BAT0'):
    cg.text(' %{T2}')
    with cg.if_('match "$battery" == "discharging $battery_percent%%"'):
        cg.fg(0xFFC726)
        cg.else_()
        cg.fg(0x9FbC00)

    with cg.cases():
        for i, icon in enumerate(bat_icons[:-1]):
            cg.case('match $battery_percent < %d' % ((i+1)*bat_delta))
            cg.text(chr(icon))

        cg.else_()
        cg.text(chr(bat_icons[-1]))  # icon for 100 percent

    cg.text('%{T-} ')
    cg.var('battery_percent')
    cg.text('% ')
    cg.fg(None)


# Widget configuration:
bar = lemonbar.Lemonbar(geometry = (x,y,width,height))
bar.widget = W.ListLayout([
    W.RawLabel('%{l}'),
    hlwm.HLWMTags(hc, monitor, tag_renderer = hlwm.underlined_tags),
    W.RawLabel('%{c}'),
    hlwm.HLWMWindowTitle(hc),
    W.RawLabel('%{r}'),
    conky.ConkyWidget(text=str(cg)),
    W.RawLabel("%{F#ffffff}"),
    W.DateTime('%d. %B, %H:%M'),
])


