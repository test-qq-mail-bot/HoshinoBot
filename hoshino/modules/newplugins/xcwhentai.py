import os
import random

from nonebot.exceptions import CQHttpError
from nonebot import MessageSegment

from hoshino import R, Service, priv

sv = Service('xcwhentai', visible=True)
xcw_folder = R.get('record/mawo/').path

def xcw_gener():
    while True:
        filelist = os.listdir(xcw_folder)
        random.shuffle(filelist)
        for filename in filelist:
            if os.path.isfile(os.path.join(xcw_folder, filename)):
                yield R.get('record/mawo/', filename)

xcw_gener = xcw_gener()

def get_xcw():
    return xcw_gener.__next__()


@sv.on_keyword(('骂我','变态','hentai'))
async def xcw(bot, ev) -> MessageSegment:
    # conditions all ok, send a xcw.
    file = get_xcw()
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(file.path)}')
        await bot.send(ev, rec, at_sender=True)
    except CQHttpError:
        sv.logger.error("发送失败")
