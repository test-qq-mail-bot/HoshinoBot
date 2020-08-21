import random

from nonebot import on_command

from hoshino import R, Service, priv, util


# basic function for debug, not included in Service('chat')
@on_command('zai?', aliases=('在?', '在？', '在吗', '在么？', '在嘛', '在嘛？'), only_to_me=True)
async def say_hello(session):
    await session.send('はい！私はいつも貴方の側にいますよ！')


sv = Service('chat', visible=False)

@sv.on_fullmatch(('沙雕机器人','傻屌机器人'))
async def say_sorry(bot, ev):
    await bot.send(ev, 'ごめんなさい！嘤嘤嘤(〒︿〒)')


@sv.on_fullmatch(('老婆', 'waifu', 'laopo'), only_to_me=True)
async def chat_waifu(bot, ev):
    if not priv.check_priv(ev, priv.SUPERUSER):
        await bot.send(ev, R.img('laopo.jpg').cqcode)
    else:
        await bot.send(ev, 'mua~')


@sv.on_fullmatch('老公', only_to_me=True)
async def chat_laogong(bot, ev):
    await bot.send(ev, '你给我滚！', at_sender=True)


@sv.on_fullmatch('mua', only_to_me=True)
async def chat_mua(bot, ev):
    await bot.send(ev, '笨蛋~', at_sender=True)


@sv.on_fullmatch('来点星奏')
async def seina(bot, ev):
    await bot.send(ev, R.img('星奏.png').cqcode)


#@sv.on_fullmatch(('我有个朋友说他好了', '我朋友说他好了', ))
#async def ddhaole(bot, ev):
#    await bot.send(ev, '那个朋友是不是你弟弟？')
#    await util.silence(ev, 30)


#@sv.on_fullmatch('我好了')
#async def nihaole(bot, ev):
#    await bot.send(ev, '不许好，憋回去！')
#    await util.silence(ev, 30)


# ============================================ #


@sv.on_keyword(('确实', '有一说一', 'u1s1', 'yysy'))
async def chat_queshi(bot, ctx):
    if random.random() < 0.05:
        await bot.send(ctx, R.img('确实.jpg').cqcode)


#@sv.on_keyword(('会战'))
#async def chat_clanba(bot, ctx):
#    if random.random() < 0.02:
#        await bot.send(ctx, R.img('我的天啊你看看都几度了.jpg').cqcode)


@sv.on_keyword(('内鬼'))
async def chat_neigui(bot, ctx):
    if random.random() < 0.10:
        await bot.send(ctx, R.img('内鬼.png').cqcode)

nyb_player = f'''{R.img('newyearburst.gif').cqcode}
正在播放：New Year Burst
──●━━━━ 1:05/1:30
⇆ ㅤ◁ ㅤㅤ❚❚ ㅤㅤ▷ ㅤ↻
'''.strip()

@sv.on_keyword(('春黑', '新黑'))
async def new_year_burst(bot, ev):
    if random.random() < 0.02:
        await bot.send(ev, nyb_player)



# ============================================ #自己加的



@sv.on_keyword(('爹','爸'), only_to_me=True)
async def say_baba(bot, ev):
    await bot.send(ev, '我是你妈!不是你爸!!!!', at_sender=True)

@sv.on_keyword(('早'), only_to_me=True)
async def zaoan(bot, ev):
    await bot.send(ev, '早上好，一束阳光照在身，祝你天天都开心，梦想可以变成真！加油呀', at_sender=True)

@sv.on_keyword(('晚'), only_to_me=True)
async def wanan(bot, ev):
    await bot.send(ev, '晚安~祝你有个好梦~', at_sender=True)


@sv.on_keyword(('我爱你'), only_to_me=True)
async def woaini(bot, ev):
    await bot.send(ev, '对不起,你是个好人', at_sender=True)


@sv.on_keyword(('抱抱'), only_to_me=True)
async def baobao(bot, ev):
    await bot.send(ev, '抱抱~', at_sender=True)


@sv.on_keyword(('举高高','生日'))
async def jugaogao(bot, ev):
    await bot.send(ev, R.img('举高高.jpg').cqcode)

@sv.on_keyword(('??', '问题'))
async def wenhao(bot, ev):
	if random.random() < 0.10:
		await bot.send(ev, R.img('./图片/问号.jpg').cqcode)

@sv.on_keyword(('不懂', '不会', '不知道'))
async def buzhidao(bot, ev):
	if random.random() < 0.10:
		await bot.send(ev, R.img('./图片/不懂.jpg').cqcode)

@sv.on_keyword(('不行', 'no', '不要'))
async def buxing(bot, ev):
	if random.random() < 0.10:
		await bot.send(ev, R.img('./图片/不行.jpg').cqcode)

@sv.on_keyword(('吃瓜', '观望', '看看'))
async def chigua(bot, ev):
	if random.random() < 0.10:
		await bot.send(ev, R.img('./图片/吃瓜.jpg').cqcode)

@sv.on_keyword(('哈哈','233'))
async def haha(bot, ev):
	if random.random() < 0.10:
		await bot.send(ev, R.img('./图片/能别笑我吗.jpg').cqcode)

@sv.on_keyword(('男妈妈' ))
async def nanmama(bot, ev):
	if random.random() < 0.10:
		await bot.send(ev, R.img('./图片/男妈妈.jpg').cqcode)

@sv.on_keyword(('你好骚','sao' ))
async def sao(bot, ev):
	if random.random() < 0.10:
		await bot.send(ev, R.img('./图片/你好骚啊.jpg').cqcode)

@sv.on_keyword(('是的', 'yes', '是', '没错' ))
async def shide(bot, ev):
	if random.random() < 0.10:
		await bot.send(ev, R.img('./图片/是的.jpg').cqcode)

@sv.on_keyword(('+1', '复读', '复读机' ))
async def jia1(bot, ev):
	if random.random() < 0.10:
		await bot.send(ev, R.img('./图片/+1.jpg').cqcode)

@sv.on_fullmatch(('刷图', '查图', '刷装备', '装备'))
async def shuatu(bot, ev):
	await bot.send(ev, R.img('./图片/刷图.jpg').cqcode)


@sv.on_fullmatch(('test', 'test1' ))
async def test(bot, ev):
	await bot.send(ev, R.img('./图片/春黑.gif').cqcode)

@sv.on_keyword('我好了')
async def chat_nihaole(bot, ev):
    if random.random() >= 0.3:
        await bot.send(ev, '不许好，憋回去！')
    else:
        await bot.send(ev, '不,你不能好', at_sender=True)

@sv.on_keyword(('我有个朋友说他好了', '我朋友说他好了','朋友说他好了' ))
async def ddhaole(bot, ev):
    if random.random() >= 0.3:
        await bot.send(ev, '那个朋友是不是你弟弟？')
    else:
        await bot.send(ev, '我朋友也好了')    