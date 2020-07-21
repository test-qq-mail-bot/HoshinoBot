import random

from nonebot import on_command

from hoshino import R, Service, priv, util


# basic function for debug, not included in Service('chat')
@on_command('zai?', aliases=('在','在?', '在？', '在吗', '在么？', '在嘛', '在嘛？'), only_to_me=True)
async def say_hello(session):
    await session.send('はい！私はいつも貴方の側にいますよ！')


sv = Service('chat', visible=False)

@sv.on_fullmatch(('沙雕机器人', '沙雕機器人'))
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
	if random.random() >= 0.05:
		await bot.send(ev, '笨蛋~', at_sender=True)
	else:
		await bot.send(ev, '虽然已经有主人了.我只能偷偷给你一个mua,可别被主人发现了')



@sv.on_fullmatch('来点星奏')
async def seina(bot, ev):
    await bot.send(ev, R.img('星奏.png').cqcode)


#@sv.on_fullmatch(('我有个朋友说他好了', '我朋友说他好了', ))
#async def ddhaole(bot, ev):
#    await bot.send(ev, '那个朋友是不是你弟弟？')
    #await util.silence(ev, 30)


#@sv.on_fullmatch('我好了')
#async def nihaole(bot, ev):
#    await bot.send(ev, '不许好，憋回去！')
    #await util.silence(ev, 30)


@sv.on_keyword('我好了')
async def chat_nihaole(bot, ev):
    if random.random() >= 0.3:
        await bot.send(ev, '不许好，憋回去！')
    else:
        await bot.send(ev, '不,你不好', at_sender=True)

@sv.on_keyword(('我有个朋友说他好了', '我朋友说他好了','朋友说他好了', ))
async def ddhaole(bot, ev):
    if random.random() >= 0.3:
        await bot.send(ev, '那个朋友是不是你弟弟？')
    else:
        await bot.send(ev, '我朋友也好了')

# ============================================ #


@sv.on_keyword(('确实', '有一说一', 'u1s1', 'yysy'))
async def chat_queshi(bot, ctx):
    if random.random() < 0.05:
        await bot.send(ctx, R.img('确实.jpg').cqcode)


@sv.on_keyword(('会战'))
async def chat_clanba(bot, ctx):
    if random.random() < 0.02:
        await bot.send(ctx, R.img('我的天啊你看看都几度了.jpg').cqcode)


@sv.on_keyword(('内鬼'))
async def chat_neigui(bot, ctx):
    if random.random() < 0.05:
        await bot.send(ctx, R.img('内鬼.png').cqcode)

nyb_player = f'''{R.img('newyearburst.jpg').cqcode}
正在播放：New Year Burst
──●━━━━ 1:05/1:30
⇆ ㅤ◁ ㅤㅤ❚❚ ㅤㅤ▷ ㅤ↻
'''.strip()

@sv.on_keyword(('春黑', '新黑'))
async def new_year_burst(bot, ev):
    if random.random() < 0.05:
        await bot.send(ev, nyb_player)


# ============================================ #自己加的



@sv.on_command('爹', aliases=('爸', '爸爸',), only_to_me=True)
async def say_baba(session):
    await session.send('我是你妈!不是你爸!!!!', at_sender=True)



@sv.on_command('晚安', only_to_me=True)
async def wanan(session):
    await session.send('晚安~祝你有个好梦~', at_sender=True)


@sv.on_command('我爱你', aliases=('爱你', ), only_to_me=True)
async def woaini(session):
    await session.send('对不起,你是个好人', at_sender=True)


@sv.on_command('抱抱', only_to_me=True)
async def baobao(session):
    await session.send('抱抱~', at_sender=True)


@sv.on_command('举高高', only_to_me=False)
async def jugaogao(session):
    await session.send(R.img('举高高.jpg').cqcode)

@sv.on_command('???', aliases=('??', '?',), only_to_me=False)
async def wenhao(session):
	if random.random() < 0.10:
		await session.send(R.img('./图片/问号.jpg').cqcode)

@sv.on_command('不懂', aliases=('不会', '不知道',), only_to_me=False)
async def buzhidao(session):
	if random.random() < 0.10:
		await session.send(R.img('./图片/不懂.jpg').cqcode)

@sv.on_command('不行', aliases=('no', '不要',), only_to_me=False)
async def buxing(session):
	if random.random() < 0.10:
		await session.send(R.img('./图片/不行.jpg').cqcode)

@sv.on_command('吃瓜', aliases=('观望', '看看',), only_to_me=False)
async def chigua(session):
	if random.random() < 0.10:
		await session.send(R.img('./图片/吃瓜.jpg').cqcode)

@sv.on_command('哈哈', aliases=('哈哈哈', '哈哈嗝','233','2333',), only_to_me=False)
async def haha(session):
	if random.random() < 0.10:
		await session.send(R.img('./图片/哈哈哈.jpg').cqcode)

@sv.on_command('男妈妈', aliases=('不要男妈妈', ), only_to_me=False)
async def nanmama(session):
	if random.random() < 0.10:
		await session.send(R.img('./图片/男妈妈.jpg').cqcode)

@sv.on_command('你好骚啊', aliases=('好骚啊', '骚啊', 'sao', ), only_to_me=False)
async def sao(session):
	if random.random() < 0.10:
		await session.send(R.img('./图片/你好骚啊.jpg').cqcode)

@sv.on_command('是的', aliases=('yes', '是', '没错', ), only_to_me=False)
async def shide(session):
	if random.random() < 0.10:
		await session.send(R.img('./图片/是的.jpg').cqcode)

@sv.on_command('+1',  aliases=('复读', '复读机', ), only_to_me=False)
async def jia1(session):
	if random.random() < 0.10:
		await session.send(R.img('./图片/+1.jpg').cqcode)

