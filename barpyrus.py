import sys
import contextlib

from barpyrus import hlwm
from barpyrus import widgets as W
from barpyrus.core import Theme
from barpyrus import lemonbar
from barpyrus import conky


@contextlib.contextmanager
def maybe_orange(match, predicate='> 90'):
    with cg.if_('match ${%s} %s' % (match, predicate)):
        cg.fg('#ffc726')
    yield
    cg.fg(None)


hc = hlwm.connect()

monitor = sys.argv[1] if len(sys.argv) >= 2 else 0
x, y, monitor_w, monitor_h = hc.monitor_rect(monitor)
height = 16
width = monitor_w

hc(['pad', str(monitor), str(height)])

cg = conky.ConkyGenerator(lemonbar.textpainter())

## CPU / RAM / df
with cg.temp_fg('#9fbc00'):
    cg.symbol(0xe026)
cg.space(5)
for cpu in '1234':
    with maybe_orange('cpu cpu%s' % cpu):
        cg.var('cpu cpu' + cpu)
        cg.text('% ')

with cg.temp_fg('#9fbc00'):
    cg.symbol(0xe021)
cg.space(5)
with maybe_orange('memperc'):
    cg.var('memperc')
    cg.text('% ')

with cg.temp_fg('#9fbc00'):
    cg.symbol(0x00e1bb)
cg.space(5)
with maybe_orange('fs_used_perc /'):
    cg.var('fs_used_perc /')
    cg.text('% ')


## Network
wifi_icons = [0xe217, 0xe218, 0xe219, 0xe21a]
wifi_delta = 100 / len(wifi_icons)

with cg.if_('up tun0'):
    with cg.temp_fg('#ff0000'):
        cg.symbol(0xe0a6)

for iface in ['eth', 'wlan', 'ppp0']:
    with cg.if_('up %s' % iface), cg.if_('match "${addr %s}" != "No Address"' % iface):
        with cg.temp_fg('#9fbc00'):
            if iface == 'wlan':
                with cg.cases():
                    for i, icon in enumerate(wifi_icons[:-1]):
                        cg.case('match ${wireless_link_qual_perc wlan} < %d' % ((i+1)*wifi_delta))
                        cg.symbol(icon)

                    cg.else_()
                    cg.symbol(wifi_icons[-1])  # icon for 100 percent
                cg.space(5)
            elif iface == 'eth':
                cg.symbol(0xe0af)
            elif iface == 'ppp0':
                cg.symbol(0xe0f3)
            else:
                assert False

        if iface == 'wlan':
            cg.var('wireless_essid')

        if iface != 'ppp0':
            cg.space(5)
            cg.var('addr %s' % iface)

        cg.space(5)
        with cg.temp_fg('#9fbc00'):
            cg.symbol(0xe13c)
        cg.var('downspeedf %s' % iface)
        cg.text('K ')
        cg.var('totaldown %s' % iface)
        cg.space(5)
        with cg.temp_fg('#9fbc00'):
            cg.symbol(0xe13b)
        cg.var('upspeedf %s' % iface)
        cg.text('K ')
        cg.var('totalup %s' % iface)
        cg.space(5)

## Battery
# first icon: 0 percent
# last icon: 100 percent
bat_icons = [
    0xe242, 0xe243, 0xe244, 0xe245, 0xe246,
    0xe247, 0xe248, 0xe249, 0xe24a, 0xe24b,
]
bat_delta = 100 / len(bat_icons)

with cg.if_('existing /sys/class/power_supply/BAT0'):
    cg.fg('#9fbC00')

    with cg.if_('match "$battery" != "discharging $battery_percent%"'):
        cg.symbol(0xe0db)

    with cg.cases():
        for i, icon in enumerate(bat_icons[:-1]):
            cg.case('match $battery_percent < %d' % ((i+1)*bat_delta))
            cg.symbol(icon)

        cg.else_()
        cg.symbol(bat_icons[-1])  # icon for 100 percent

    cg.fg(None)
    cg.space(5)

    with maybe_orange('battery_percent', '< 10'):
        cg.var('battery_percent')
        cg.text('% ')
        cg.var('battery_time')
        cg.space(5)


with cg.temp_fg('#9fbc00'):
    cg.symbol(0xe015)
cg.space(5)
cg.var('time %d. %B, %H:%M')


conky_config = {
    'update_interval': '5',
}


# Widget configuration:
bar = lemonbar.Lemonbar(geometry = (x,y,width,height))
bar.widget = W.ListLayout([
    W.RawLabel('%{l}'),
    hlwm.HLWMTags(hc, monitor, tag_renderer = hlwm.underlined_tags),
    W.RawLabel('%{c}'),
    hlwm.HLWMWindowTitle(hc),
    W.RawLabel('%{r}'),
    conky.ConkyWidget(text=str(cg), config=conky_config),
])
