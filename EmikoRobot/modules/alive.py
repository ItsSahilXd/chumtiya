import asyncio
import os
import requests
import datetime
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telegram import __version__ as telever
from telethon import events, Button, custom, version
from EmikoRobot.events import register
from EmikoRobot import telethn as aasf
from EmikoRobot import StartTime, dispatcher
from telethon.tl.types import ChannelParticipantsAdmins

edit_time = 5
""" =======================Kobo Kanaeru====================== """
file1 = "https://telegra.ph/file/fccf074e6d1b333c635e8.jpg"
file2 = "https://telegra.ph/file/79c74ae56bb5a59511727.jpg"
file3 = "https://telegra.ph/file/958b115b91dc56437de7f.jpg"
file4 = "https://telegra.ph/file/7bcc93bff54ec80184d59.jpg"
file5 = "https://telegra.ph/file/ce349a523b465ebcc0e43.jpg"
""" =======================Kobo Kanaeru====================== """

BUTTON = [[Button.url("Help", "https://t.me/KoboKanaeru_Robot?start=help"), Button.url("Support", "https://t.me/AkoUpdate")]]


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

@register(pattern=("/alive"))
async def hmm(yes):
    chat = await yes.get_chat()
    await yes.delete()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    pm_caption = "**Yo, I,m Kobo Kanaeru!! **\n\n"
    pm_caption += f"**⚪ My Uptime :** `{uptime}`\n\n"
    pm_caption += f"**⚪ Telethon Version :** `{version.__version__}`\n\n"
    pm_caption += "**⚪ My Owner :** [Human](https://t.me/Humaaancarees)\n\n"
    pm_caption += "**⚪ My Developer:** [Ako](https://t.me/erosei_1)\n"
    BUTTON = [[Button.url("Help", "https://t.me/KoboKanaeru_Robot?start=help"), Button.url("Support", "https://t.me/AkoUpdate")]]
    on = await aasf.send_file(yes.chat_id, file=file1,caption=pm_caption, buttons=BUTTON)
    

    await asyncio.sleep(edit_time)
    ok = await aasf.edit_message(yes.chat_id, on, file=file2, buttons=BUTTON) 

    await asyncio.sleep(edit_time)
    ok2 = await aasf.edit_message(yes.chat_id, ok, file=file3, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok3 = await aasf.edit_message(yes.chat_id, ok2, file=file4, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok4 = await aasf.edit_message(yes.chat_id, ok3, file=file5, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok5 = await aasf.edit_message(yes.chat_id, ok4, file=file1, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok6 = await aasf.edit_message(yes.chat_id, ok5, file=file2, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok7 = await aasf.edit_message(yes.chat_id, ok6, file=file3, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok8 = await aasf.edit_message(yes.chat_id, ok7, file=file4, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok9 = await aasf.edit_message(yes.chat_id, ok8, file=file5, buttons=BUTTON)
