import pytz
from datetime import datetime
import hoshino
from hoshino import Service
from hoshino.service import sucmd
from hoshino.typing import CommandSession

sv = Service('hourcallyao', help_='提醒买药,地下城等')
tz = pytz.timezone('Asia/Shanghai')

def get_hour_call():
    """挑出一组时报，每日更换，一日之内保持相同"""
    cfg = hoshino.config.hourcallyao
    now = datetime.now(tz)
    hc_groups = cfg.HOUR_CALLS_ON
    g = hc_groups[ now.day % len(hc_groups) ]
    return cfg.HOUR_CALLS[g]

@sv.scheduled_job('cron', hour='*')
async def hour_callyao():
    now = datetime.now(tz)
    #if 2 <= now.hour <= 4:
    if not now.hour % 6 == 0:
        return
    msg = get_hour_call()[now.hour]
    await sv.broadcast(msg, 'hourcallyao', 0)

@sucmd('manualhourcall', aliases=('mhc', '手动报时'))
async def manual_hourcall(session: CommandSession):
    msg = session.current_arg
    if msg!="":
        await sv.broadcast(msg, 'hourcallyao', 0)
    await hour_callyao()
