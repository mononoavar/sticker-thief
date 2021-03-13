# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
import os
import requests
from asyncio import sleep
from bs4 import BeautifulSoup as bs
from . import *
XX = "A servant appeared!"
YY = "A qt waifu appeared!" 
@ultroid_bot.on(events.NewMessage(incoming=True))
async def reverse(event):
    if not event.media:
        return
    if not event.sender_id==792028928 or event.sender_id==1232515770:
        return
    if not event.text==XX or event.text==YY:
        return
    dl = await bot.download_media(event.media)
    file = {"encoded_image": (dl, open(dl, "rb"))}
    grs = requests.post(
        "https://www.google.com/searchbyimage/upload", files=file, allow_redirects=False
    )
    loc = grs.headers.get("Location")
    response = requests.get(
        loc,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"
        },
    )
    xx = bs(response.text, "html.parser")
    div = xx.find("div", {"class": "r5a77d"})
    alls = div.find("a")
    text = alls.text
    send = await ultroid_bot.send_message(event.chat_id, f"/protecc {text}")
    await sleep(2)
    await send.delete()
    os.remove(dl)
