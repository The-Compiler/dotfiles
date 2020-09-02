import sys
import contextlib
import multiprocessing

from barpyrus import hlwm
from barpyrus import widgets as W
from barpyrus.core import Theme, Painter
from barpyrus import lemonbar, conky, trayer


class Gruv:

    # https://github.com/morhetz/gruvbox

    BG0_H = '#1d2021'
    BG0_S = '#32302f'
    BG0 = '#282828'
    BG1 = '#3c3836'
    BG2 = '#504945'
    BG3 = '#665c54'
    BG4 = '#7c6f64'
    FG0 = '#fbf1c7'
    FG1 = '#ebdbb2'
    FG2 = '#d5c4a1'
    FG3 = '#bdae93'
    FG4 = '#a89984'
    FG = FG1
    BG = BG0
    RED_DARK = '#cc241d'
    GREEN_DARK = '#98971a'
    YELLOW_DARK = '#d79921'
    BLUE_DARK = '#458588'
    PURPLE_DARK = '#b16286'
    AQUA_DARK = '#689d6a'
    GRAY_DARK = '#a89984'
    ORANGE_DARK = '#d65d0e'
    RED_LIGHT = '#fb4934'
    GREEN_LIGHT = '#b8bb26'
    YELLOW_LIGHT = '#fabd2f'
    BLUE_LIGHT = '#83a598'
    PURPLE_LIGHT = '#d3869b'
    AQUA_LIGHT = '#8ec07c'
    GRAY_LIGHT = '#928374'
    ORANGE_LIGHT = '#fe8019'


ACCENT_COLOR = Gruv.ORANGE_DARK


@contextlib.contextmanager
def highlight_critical(match, predicate='> 90'):
    with cg.if_('match ${%s} %s' % (match, predicate)):
        cg.fg(Gruv.RED_LIGHT)
    yield
    cg.fg(None)


def tag_renderer(taginfo, painter):
    if taginfo.empty:
        return

    if taginfo.urgent:
        painter.fg(Gruv.RED_LIGHT)
    else:
        painter.fg(None)

    if taginfo.here:
        painter.bg(ACCENT_COLOR)
    else:
        painter.set_flag(painter.underline, taginfo.visible)
        painter.ol(ACCENT_COLOR)

    painter.space(3)
    painter += taginfo.name
    painter.space(3)
    painter.bg()
    painter.ol()
    painter.set_flag(painter.underline, False)
    painter.space(2)


hc = hlwm.connect()

monitor = sys.argv[1] if len(sys.argv) >= 2 else 0
x, y, monitor_w, monitor_h = hc.monitor_rect(monitor)
height = 16
width = monitor_w

hc(['pad', str(monitor), str(height)])

cg = conky.ConkyGenerator(lemonbar.textpainter())

## CPU / RAM / df
with cg.temp_fg(ACCENT_COLOR):
    cg.symbol(0xe026)
cg.space(5)
for cpu in [str(i+1) for i in range(multiprocessing.cpu_count())]:
    with highlight_critical('cpu cpu%s' % cpu):
        cg.var('cpu cpu' + cpu)
        cg.text('% ')

for symbol, command in [(0xe021, 'memperc'),
                        (0xe1bb, 'fs_used_perc /'),
                        (0xe1eb, 'fs_used_perc /mnt/sd')]:
    with cg.temp_fg(ACCENT_COLOR):
        cg.symbol(symbol)
    cg.space(5)
    with highlight_critical(command):
        cg.var(command)
        cg.text('% ')

## temp / fan
with cg.if_('match ${ibm_fan} != 65535'):
    with cg.temp_fg(ACCENT_COLOR):
        cg.symbol(0xe1c0)
    cg.space(5)
    with highlight_critical('ibm_fan', '> 6000'):
        cg.var('ibm_fan')
        cg.text('rpm ')
with cg.temp_fg(ACCENT_COLOR):
    cg.symbol(0xe01b)
cg.space(5)
cg.var('acpitemp')
cg.text('° ')

## Network
wifi_icons = [0xe217, 0xe218, 0xe219, 0xe21a]
wifi_delta = 100 / len(wifi_icons)

with cg.if_('up tun0'):
    with cg.temp_fg('#ff0000'):
        cg.symbol(0xe0a6)

for iface in ['eth', 'dock', 'wlan', 'ppp0']:
    with cg.if_('up %s' % iface), cg.if_('match "${addr %s}" != "No Address"' % iface):
        with cg.temp_fg(ACCENT_COLOR):
            if iface == 'wlan':
                with cg.cases():
                    for i, icon in enumerate(wifi_icons[:-1]):
                        cg.case('match ${wireless_link_qual_perc wlan} < %d' % ((i+1)*wifi_delta))
                        cg.symbol(icon)

                    cg.else_()
                    cg.symbol(wifi_icons[-1])  # icon for 100 percent
                cg.space(5)
            elif iface in ['eth', 'dock']:
                cg.symbol(0xe0af)
            elif iface == 'ppp0':
                cg.symbol(0xe0f3)
            else:
                assert False

        if iface == 'wlan':
            cg.var('wireless_essid wlan')

        if iface != 'ppp0':
            cg.space(5)
            cg.var('addr %s' % iface)

        cg.space(5)
        with cg.temp_fg(ACCENT_COLOR):
            cg.symbol(0xe13c)
        cg.var('downspeedf %s' % iface)
        cg.text('K ')
        cg.var('totaldown %s' % iface)
        cg.space(5)
        with cg.temp_fg(ACCENT_COLOR):
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
    cg.fg(ACCENT_COLOR)

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

    with highlight_critical('battery_percent', '< 10'):
        cg.var('battery_percent')
        cg.text('% ')
        cg.var('battery_time')
        cg.space(5)


with cg.temp_fg(ACCENT_COLOR):
    cg.symbol(0xe015)
cg.space(5)
cg.var('time %d. %B, %H:%M')


conky_config = {
    'update_interval': '5',
}
trayer_config = {
    'tint': Gruv.BG.replace('#', '0x'),
    'iconspacing': '5',
    'padding': '5'
}


# Widget configuration:
bar = lemonbar.Lemonbar(geometry = (x,y,width,height), foreground=Gruv.FG)
bar.widget = W.ListLayout([
    W.RawLabel('%{l}'),
    hlwm.HLWMTags(hc, monitor, tag_renderer=tag_renderer),
    W.RawLabel('%{c}'),
    hlwm.HLWMWindowTitle(hc),
    W.RawLabel('%{r}'),
    conky.ConkyWidget(text=str(cg), config=conky_config),
    trayer.TrayerWidget(args=trayer_config),
])
