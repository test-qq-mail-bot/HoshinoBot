import itertools
from hoshino import util, R
from hoshino.typing import CQEvent
from . import sv

p1 = R.img('priconne/quick/台服/1.png').cqcode
p2 = R.img('priconne/quick/台服/2.png').cqcode
p3 = R.img('priconne/quick/台服/3.png').cqcode
p4 = R.img('priconne/quick/日服/1.jpg').cqcode
p5 = R.img('priconne/quick/日服/2.jpg').cqcode
p6 = R.img('priconne/quick/日服/3.jpg').cqcode
p7 = R.img('priconne/quick/国服/1.png').cqcode
p8 = R.img('priconne/quick/国服/2.png').cqcode

@sv.on_rex(r'^(\*?([日台国陆b])服?([前中后]*)卫?)?rank(表|推荐|指南)?$')
async def rank_sheet(bot, ev):
    match = ev['match']
    is_jp = match.group(2) == '日'
    is_tw = match.group(2) == '台'
    is_cn = match.group(2) == '国' or match.group(2) in ['b','陆']
    if not is_jp and not is_tw and not is_cn:
        await bot.send(ev, '\n请问您要查询哪个服务器的rank表？\n*日rank表\n*台rank表\n*B服rank表\n※r10前无需考虑卡rank，装备强化消耗较多mana，如非前排建议不强化', at_sender=True)
        return
    msg = [
        '\n※表格仅供参考，升r有风险，强化需谨慎',
    ]
    if is_jp:
        msg.append('※不定期搬运来自NGA的pjttcn\n※如有好用的rank表,也可以私聊推荐给我\nrank表：')
        pos = match.group(3)
        if not pos or '前' in pos:
            msg.append(str(p4))
        if not pos or '中' in pos:
            msg.append(str(p5))
        if not pos or '后' in pos:
            msg.append(str(p6))
        await bot.send(ev, '\n'.join(msg), at_sender=True)
        #await util.silence(ev, 60)
    elif is_tw:
        msg.append(f'※7月已更新\n※不定期搬运自Nonplume\n※NGA有原图及原文档\nrank表：\n{p1}{p2}{p3}')
        await bot.send(ev, '\n'.join(msg), at_sender=True)
        #await util.silence(ev, 60)

    elif is_cn:
        msg.append(f'※不定期搬运自lucky213\n※NGA有原图及原文档\n rank表：\n{p7}{p8}')
        await bot.send(ev, '\n'.join(msg), at_sender=True)        
        

#    elif is_cn:
#        await bot.send(ev, #'\n※r10前无需考虑卡rank\n※暂未发现公开的靠谱rank推荐表\n※装备强化消耗较多mana，如非前排建议不强化\n※关于卡r的原因可发送#"bcr速查"研读【为何卡R卡星】一帖', at_sender=True)
        # await bot.send(ev, str(p7))
        # await util.silence(ev, 60)


@sv.on_fullmatch(('jjc', 'JJC', 'JJC作业', 'JJC作业网', 'JJC数据库', 'jjc作业', 'jjc作业网', 'jjc数据库', 'JJC作業', 'JJC作業網', 'JJC數據庫', 'jjc作業', 'jjc作業網', 'jjc數據庫'))
async def say_arina_database(bot, ev):
    await bot.send(ev, '公主连接Re:Dive 竞技场编成数据库\n日文：https://nomae.net/arenadb \n中文：https://pcrdfans.com/battle')


OTHER_KEYWORDS = '【日rank】【台rank】【b服rank】【jjc作业网】【黄骑充电表】【一个顶俩】'
PCR_SITES = f'''
【繁中wiki/兰德索尔图书馆】pcredivewiki.tw
【日文wiki/GameWith】gamewith.jp/pricone-re
【日文wiki/AppMedia】appmedia.jp/priconne-redive
【竞技场作业库(中文)】pcrdfans.com/battle
【竞技场作业库(日文)】nomae.net/arenadb
【论坛/NGA社区】bbs.nga.cn/thread.php?fid=-10308342
【iOS实用工具/初音笔记】bbs.nga.cn/read.php?tid=14878762
【安卓实用工具/静流笔记】bbs.nga.cn/read.php?tid=20499613
【台服卡池千里眼】bbs.nga.cn/read.php?tid=16986067
【日官网】priconne-redive.jp
【台官网】www.princessconnect.so-net.tw

===其他查询关键词===
{OTHER_KEYWORDS}
※B服速查请输入【bcr速查】'''

BCR_SITES = f'''
【PJJC防守阵容搭配思路】https://bbs.nga.cn/read.php?tid=22372410
【公会战排名网页端查询】https://kengxxiao.github.io/Kyouka/
【2020/6月Rank9-3推荐表】https://bbs.nga.cn/read.php?tid=22247310
【赫斯海德计轴器演示】https://www.bilibili.com/video/BV16C4y1a7oh?p=1
【角色动作帧数表】https://bbs.nga.cn/read.php?tid=21952354&_fp=2
【黄骑充电详解】https://bbs.nga.cn/read.php?tid=21913703&_fp=2
【仓鼠玩家pjjc登顶教程】https://bbs.nga.cn/read.php?tid=21850496&_fp=2

===其他查询关键词===
{OTHER_KEYWORDS}
※日台服速查请输入【pcr速查】
'''

@sv.on_fullmatch(('pcr速查', 'pcr图书馆', 'pcr圖書館', '图书馆', '圖書館'))
async def pcr_sites(bot, ev: CQEvent):
    await bot.send(ev, PCR_SITES, at_sender=True)
    #await util.silence(ev, 60)
@sv.on_fullmatch(('bcr速查', 'bcr攻略'))
async def bcr_sites(bot, ev: CQEvent):
    await bot.send(ev, BCR_SITES, at_sender=True)
    #await util.silence(ev, 60)


YUKARI_SHEET_ALIAS = map(lambda x: ''.join(x), itertools.product(('黄骑', '酒鬼', '黃騎'), ('充电', '充电表', '充能', '充能表')))
YUKARI_SHEET = f'''
{R.img('priconne/quick/黄骑充电.jpg').cqcode}
※大圈是1动充电对象 PvP测试
※黄骑四号位例外较多
※对面羊驼或中后卫坦 有可能歪
※我方羊驼算一号位
※图片搬运自漪夢奈特'''
@sv.on_fullmatch(YUKARI_SHEET_ALIAS)
async def yukari_sheet(bot, ev):
    await bot.send(ev, YUKARI_SHEET, at_sender=True)
    #await util.silence(ev, 60)

@sv.on_fullmatch(('角色位置','角色站位','站位'))
async def stand_position(bot,ev):
	await bot.send(ev,R.img('图片/角色站位表/1.png').cqcode)
	await bot.send(ev,R.img('图片/角色站位表/2.png').cqcode)
	await bot.send(ev,R.img('图片/角色站位表/3.png').cqcode, at_sender=True)

DRAGON_TOOL = f'''
拼音对照表：{R.img('priconne/KyaruMiniGame/注音文字.jpg').cqcode}{R.img('priconne/KyaruMiniGame/接龙.jpg').cqcode}
龍的探索者們小遊戲單字表 https://hanshino.nctu.me/online/KyaruMiniGame
镜像 https://hoshino.monster/KyaruMiniGame
网站内有全词条和搜索'''
@sv.on_fullmatch(('一个顶俩', '拼音接龙', '韵母接龙'))
async def dragon(bot, ev):
    await bot.send(ev, DRAGON_TOOL, at_sender=True)
    #await util.silence(ev, 60)
