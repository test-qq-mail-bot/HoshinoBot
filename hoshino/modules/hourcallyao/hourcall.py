import pytz
from datetime import datetime
import hoshino
from hoshino import Service

sv = Service('hourcallyao', enable_on_default=True, help_='提醒买药,地下城等')
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
    if 1 <= now.hour <= 5:
        return  # 宵禁 免打扰
    msg = get_hour_call()[now.hour]
    await sv.broadcast(msg, 'hourcallyao', 0)
