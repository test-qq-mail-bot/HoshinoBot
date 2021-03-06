"""这是一份实例配置文件

将其修改为你需要的配置，并将文件夹config_example重命名为config
"""

# hoshino监听的端口与ip
PORT = 9991
HOST = '127.0.0.1'      # 本地部署使用此条配置（QQ客户端和bot端运行在同一台计算机）
# HOST = '0.0.0.0'      # 开放公网访问使用此条配置（不安全）

DEBUG = False           # 调试模式

SUPERUSERS = [1499049630]    # 填写超级用户的QQ号，可填多个用半角逗号","隔开
NICKNAME = {'妈', '可可萝', '可可罗', '机器人'}           # 机器人的昵称。呼叫昵称等同于@bot，可用元组配置多个昵称

COMMAND_START = {''}    # 命令前缀（空字符串匹配任何消息）
COMMAND_SEP = set()     # 命令分隔符（hoshino不需要该特性，保持为set()即可）

# 发送图片的协议
# 可选 http, file, base64
# 当QQ客户端与bot端不在同一台计算机时，可用http协议
RES_PROTOCOL = 'file'
# 资源库文件夹，需可读可写，windows下注意反斜杠转义
RES_DIR = r'D:/Desktop/机器人/res/'
# 使用http协议时需填写，原则上该url应指向RES_DIR目录
RES_URL = 'http://127.0.0.1:5000/static/'


# 启用的模块
# 初次尝试部署时请先保持默认
# 如欲启用新模块，请认真阅读部署说明，逐个启用逐个配置
# 切忌一次性开启多个
MODULES_ON = {
    'botmanage',#机器人管理
    'dice',#骰子
    'groupmaster',#生成器
    'hourcall',#时报
    ##'kancolle',#演习/月常远征提醒
    ##'mikan',#蜜柑
    ##'pcrclanbattle',#公会战
    'priconne',#抽卡,rank表等
    ##'setu',    
    ##'translate',#翻译
    ##'twitter',#推特
    'gonghui-nowtime',#工会战催刀图
    'nowtime',#报时
    'Reloader',#重载hoshino程序
    'generator',#营销号生成器等
    'morning-nowtime',#催起床图
    'bot_manager_web',#lssv的web管理
    'clanbattle_report',#离职报告
    'clanrank',#会战排名查询2
    'flac',#搜索无损    
    'calendar',#日程表
    'newplugins',#会战期间可以关闭的插件
    'authMS',#授权
    'image-generate',#生成表情包
    'eqa',#你问我答
    'hourcallyao-cn',#国服-买药小助手
    'hourcallyao-jp',#日服-买药小助手
    'pcrmemorygames',#公主连结记忆小游戏
    'pcrmiddaymusic',#公主连结午间音乐
    'pokemanpcr',#戳机器人集卡小游戏
}
