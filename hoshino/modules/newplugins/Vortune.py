import hoshino
from hoshino import Service, log
from hoshino.typing import CQEvent

import random, pytz, datetime, os, aiofiles

from .Vortune_data import Vortune
from PIL import Image, ImageDraw, ImageFont

try:
    import ujson
except:
    import json as ujson

absPath = './hoshino/modules/newplugins/Vortune-data'
logger = log.new_logger('Vortune', hoshino.config.DEBUG)
tz = pytz.timezone('Asia/Shanghai')

FAILURE = 'failure'
DEFAULT = 'default'

sv = Service('vortune', help_='''
今日人品
今日运势
抽签
人品
运势
'''.strip())


@sv.on_fullmatch(('今日人品', '今日运势', '抽签', '人品', '运势'))
async def nor_vor(bot, ev: CQEvent):
    model = DEFAULT
    #name = ev.message.extract_plain_text().strip()
    #if '' in name:
    #    model = ''
    vortune_msg = ''
    result = Vortune.select().where(Vortune.qqid == ev.user_id)
    now_day = datetime.datetime.now().strftime('%Y-%m-%d')
    for query in result:
        if query.last_time != now_day:
            logger.info('今日未预测')
            logger.info('删除昨日运势文件')
            os.remove(query.vortune_filepath)
            logger.info('获取今日运势')
            outPath = await drawing(model, ev.user_id)
            Vortune.replace(
                qqid = ev.user_id,
                last_time = now_day,
                vortune_filepath = outPath
            ).execute()
            vortune_msg = cqimage(outPath)
        else:
            logger.info('今日已预测')
            vortune_msg = cqimage(query.vortune_filepath)
            await bot.send(ev, '今天已经预测过了哦~再给你看一次结果吧\n' + vortune_msg, at_sender = True)
            return
    if vortune_msg == '':
        logger.info('数据库中未任何记录')
        outPath = await drawing(model, ev.user_id)
        Vortune.replace(
            qqid = ev.user_id,
            vortune_filepath = outPath,
            last_time = now_day
        ).execute()
        vortune_msg = cqimage(outPath)
    await bot.send(ev, '今日的运势为：\n' + vortune_msg, at_sender = False)


def cqimage(outpath):
    outpath = f'[CQ:image,file=file:///{os.path.abspath(outpath)}]'
    return outpath


async def drawing(model, userid):
    fontPath = {
        'title': absPath + '/font/Mamelon.otf',
        'text': absPath + '/font/sakura.ttf'
    }
    imgPath = await randomBasemap()
    imgsavePath = absPath + '/out/userid_' + str(userid) + '.jpg'
    if model != DEFAULT:
        imgPath = absPath + '/img/' + model
    img = Image.open(imgPath)
    # Draw title
    draw = ImageDraw.Draw(img)
    text = await copywriting()
    title = await getTitle(text)
    text = text['content']
    font_size = 45
    color = '#F5F5F5'
    image_font_center = (140, 99)
    ttfront = ImageFont.truetype(fontPath['title'], font_size)
    font_length = ttfront.getsize(title)
    draw.text((image_font_center[0]-font_length[0]/2, image_font_center[1]-font_length[1]/2),
                title, fill=color,font=ttfront)
    # Text rendering
    font_size = 25
    color = '#323232'
    image_font_center = [140, 297]
    ttfront = ImageFont.truetype(fontPath['text'], font_size)
    result = await decrement(text)
    if not result[0]:
        return
    textVertical = []
    for i in range(0, result[0]):
        font_height = len(result[i + 1]) * (font_size + 4)
        textVertical = await vertical(result[i + 1])
        x = int(image_font_center[0] + (result[0] - 2) * font_size / 2 +
                (result[0] - 1) * 4 - i * (font_size + 4))
        y = int(image_font_center[1] - font_height / 2)
        draw.text((x, y), textVertical, fill = color, font = ttfront)
    # Save
    await checkFolder(imgsavePath)
    img.save(imgsavePath)
    return imgsavePath


async def randomBasemap():
    p = absPath + '/img'
    ranpath = random.choice(os.listdir(p))
    return p + '/' + ranpath


async def copywriting():
    p = absPath + '/fortune/copywriting.json'
    content = await readJson(p)
    return random.choice(content['copywriting'])


async def getTitle(structure):
    p = absPath + '/fortune/goodLuck.json'
    content = await readJson(p)
    for i in content['types_of']:
        if i['good-luck'] == structure['good-luck']:
            return i['name']
    raise Exception('Configuration file error')


async def readJson(p):
    if not os.path.exists(p):
        return FAILURE
    async with aiofiles.open(p, 'r', encoding='utf-8') as f:
        content = await f.read()
    content = ujson.loads(content)
    return content


async def decrement(text):
    length = len(text)
    result = []
    cardinality = 9
    if length > 4 * cardinality:
        return [False]
    numberOfSlices = 1
    while length > cardinality:
        numberOfSlices += 1
        length -= cardinality
    result.append(numberOfSlices)
    # Optimize for two columns
    space = ' '
    length = len(text)
    if numberOfSlices == 2:
        if length % 2 == 0:
            # even
            fillIn = space * int(9 - length / 2)
            return [numberOfSlices, text[:int(length / 2)] + fillIn, fillIn + text[int(length / 2):]]
        else:
            # odd number
            fillIn = space * int(9 - (length + 1) / 2)
            return [numberOfSlices, text[:int((length + 1) / 2)] + fillIn,
                                    fillIn + space + text[int((length + 1) / 2):]]
    for i in range(0, numberOfSlices):
        if i == numberOfSlices - 1 or numberOfSlices == 1:
            result.append(text[i * cardinality:])
        else:
            result.append(text[i * cardinality:(i + 1) * cardinality])
    return result


async def vertical(str):
    list = []
    for s in str:
        list.append(s)
    return '\n'.join(list)


async def exportFilePath(originalFilePath):
    outPath = originalFilePath.replace('/img/', '/out/')
    await checkFolder(outPath)
    print(outPath)
    return outPath


async def checkFolder(path):
    dirPath = path[:path.rfind('/')]
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)