# made by LEGENDX22

from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.utils import admin_cmd
naam = str('Lel')

bot = "@Hexamonbot"

Pokes = ('Here Are Your HexaPokes\n➖➖➖➖➖➖➖➖➖➖➖\n\n')

@borg.on(admin_cmd("mypokes ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/mypokemon")
                audio = await conv.get_response()
                card = audio.text
                a = card.replace('/display: Level', '')
                b = a.replace('/sort by: Order caught ↑', '')
                c = b.replace('/pagesize: 20', '')
                d = c.replace('/pagesize: 10', '')
                e = d.replace('/pagesize: 15', '')
                f = e.replace('/pagesize: 25', '')
                g = f.replace('/display: IV points', '')
                h = g.replace('/display: EV points', '')
                i = h.replace('/display: Nature', '')
                j = i.replace('/display: Type', '')
                k = j.replace('/display: Type Symbol', '')
                l = k.replace('/display: Catch Rate', '')
                m = l.replace('/display: HP points', '')
                n = m.replace('/display: Attack points', '')
                o = n.replace('/display: Defense points', '')
                p = o.replace('/display: Sp. Attack points', '')
                q = p.replace('/display: Sp defense points', '')
                r = q.replace('/display: Speed points', '')
                s = r.replace('/display: None', '')
                t = s.replace('/display: Total stats points', '')
                u = t.replace('/sort by: Order caught ↓', '')
                v = u.replace('/sort by: Level ↑', '')
                w = v.replace('/sort by: Level ↓', '')
                x = w.replace('/sort by: Pokedex number ↓', '')
                y = x.replace('/sort by: Pokedex number ↑', '')
                z = y.replace('/sort by: IV points ↑', '')
                1 = z.replace('/sort by: IV points ↓', '')
                2 = 1.replace('/sort by: EV points ↓', '')
                3 = 2.replace('/sort by: EV points ↑', '')
                4 = 3.replace('/sort by: Name ↑', '')
                5 = 4.replace('/sort by: Name ↓', '')
                6 = 5.replace('/sort by: Nature ↑', '')
                7 = 6.replace('/sort by: Nature ↓', '')
                8 = 7.replace('/sort by: Type ↓', '')
                9 = 8.replace('/sort by: Type ↑', '')
                10 = 9.replace('/sort by: Catch Rate ↑', '')
                11 = 10.replace('/sort by: Catch Rate ↓', '')
                12 = 11.replace('/sort by: HP points ↑', '')
                13 = 12.replace('/sort by: HP points ↓', '')
                14 = 13.replace('/sort by: Attack points ↓', '')
                15 = 14.replace('/sort by: Attack points ↑', '')
                16 = 15.replace('/sort by: Defense points ↓', '')
                17 = 16.replace('/sort by: Defense points ↑', '')
                18 = 17.replace('/sort by: Sp. Attack points ↑', '')
                19 = 18.replace('/sort by: Sp. Attack points ↓', '') 
                20 = 19.replace('/sort by: Sp defense points ↑', '')
                21 = 20.replace('/sort by: Sp defense points ↓', '')
                22 = 21.replace('/sort by: Speed points ↓', '')
                23 = 22.replace('/sort by: Speed points ↑', '')
                24 = 23.replace('/sort by: Total stats points ↑', '')
                25 = 24.replace('/sort by: Total stats points ↓', '')
                await borg.send_message(event.chat_id, Pokes)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: UnBlock @Hexamonbot firstly, and then retry!")
    elif "@" in sysarg:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/mypokemon " + sysarg)
                audio = await conv.get_response()
                card = audio.text
                text = f'{card.splitlines()[0]}\n'
                text += f'{card.splitlines()[1]}\n'
                text += f'{card.splitlines()[2]}\n'
                await borg.send_message(event.chat_id, Pokes + text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: UnBlock @Hexamonbot firstly, and then retry!")
    elif "" in sysarg:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/mypokemon " + sysarg)
                audio = await conv.get_response()
                card = audio.text
                text = f'{card.splitlines()[0]}\n'
                text += f'{card.splitlines()[1]}\n'
                text += f'{card.splitlines()[2]}\n'
                await borg.send_message(event.chat_id, Pokes + text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: UnBlock @Hexamonbot firstly, and then retry!")
