from PIL import Image,ImageFont,ImageDraw
import os
import base64
def add_text(template_path,save_path,text:str,textsize:int,font='./msyh.ttf',textfill='black',position:tuple=(0,0)):
    #textsize 文字大小
    #font 字体，默认微软雅黑
    #textfill 文字颜色，默认黑色
    #position 文字偏移（0,0）位置，图片左上角为起点
    font_path = os.path.join(os.path.dirname(__file__),font)
    print(font_path)
    img_font = ImageFont.truetype(font=font_path,size=textsize)
    with Image.open(template_path) as img:
        draw = ImageDraw.Draw(img)
        draw.text(xy=position,text=text,font=img_font,fill=textfill)
        save_path = os.path.join(os.path.dirname(__file__),'nowtime.jpg')
        img.save(save_path)

def pic_to_b64(pic_path:str) -> str:
    with open(pic_path,'rb') as f:
        base64_str = base64.b64encode(f.read()).decode()
    return 'base64://' + base64_str

