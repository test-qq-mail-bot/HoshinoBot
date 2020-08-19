import requests
from nonebot import on_command, CommandSession

from hoshino.service import Service

sv = Service('lovelive', help_='土味情话')

@on_command('lovelive', aliases=('土味情话'), only_to_me=False)
async def lovelive(session: CommandSession):
    lovelive_send = await get_lovelive()
    await session.send(lovelive_send, at_sender=True)


async def get_lovelive():
    url = 'https://api.lovelive.tools/api/SweetNothings'
    return requests.get(url).text
