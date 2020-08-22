import json
import re
import random

from hoshino import Service,aiorequests,R

sv = Service('longwang',visible=True)

@sv.on_command('迫害龙王')
async def longwang(session):
    gid = session.ctx['group_id']
    dragon_king=await session.bot.get_group_honor_info(group_id=gid,type='talkative')
    dragon_king=dragon_king['current_talkative']['user_id']
    if dragon_king==session.ctx['self_id']:
        longwangme=R.img('图片/龙王/longwangme.jpg').cqcode
        session.finish(f'{longwangme}')
    n = random.randint(0, 7)
    if 0==n:
        img="龙王出来喷水"
    elif 7==n:
        img="龙王出来挨透"
    else:
        img = R.img('图片/龙王/longwang{}.jpg'.format(n)).cqcode
    session.finish(f'[CQ:at,qq={dragon_king}]\n{img}')
