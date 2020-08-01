"""这是一份实例配置文件

将其修改为你需要的配置，并将文件夹config_example重命名为config
"""

# hoshino监听的端口与ip
PORT = 8899
HOST = '127.0.0.1'      # Windows部署使用此条配置
# HOST = '172.17.0.1'   # linux + docker使用此条配置
# docker桥的ip可能随环境不同而有变化
# 使用这行命令`ip addr show docker0 | grep -Po 'inet \K[\d.]+'`查看你的docker桥ip
# HOST = '172.18.0.1'   # 阿里云的linux + docker多数情况是这样
# HOST = '0.0.0.0'      # 开放公网访问使用此条配置（不安全）

DEBUG = False           # 调试模式

SUPERUSERS = [1499049630]    # 填写超级用户的QQ号，可填多个用半角逗号","隔开
NICKNAME = {'妈', '可可萝', '可可罗', '机器人'}           # 机器人的昵称。呼叫昵称等同于@bot，可用元组配置多个昵称

COMMAND_START = {''}    # 命令前缀（空字符串匹配任何消息）
COMMAND_SEP = set()     # 命令分隔符（hoshino不需要该特性，保持为set()即可）

USE_CQPRO = True       # 是否使用Pro版酷Q功能

# 发送图片的协议
# 可选 http, file, base64
# 建议Windows部署使用file协议
# 建议Linux部署配合本地web server使用http协议
# 如果你不清楚上面在说什么，请用base64协议（发送大图时可能会失败）
RES_PROTOCOL = 'file'
# 资源库文件夹，需可读可写，windows下注意反斜杠转义
RES_DIR = r'C:/Users/Administrator/Desktop/res'
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
    'flac',#搜索无损
    'hourcall',#时报
     ##'kancolle',#演习/月常远征提醒
    ##'mikan',#蜜柑
    'pcrclanbattle',#公会战
    'priconne',#抽卡,rank表等
    ##'setu',
    'translate',#翻译
    ##'twitter',#推特
    'gonghui-nowtime',#工会战催刀图
    'hourcallyao',#买药小助手
    'nowtime',#报时
    'Reloader',#重载hoshino程序
    'tencent_ai',#腾讯ai聊天
    'joke',#笑话
    'lovelive',#土味情话
    'zhihu',#知乎
    'generator',#营销号生成器等
    'morning-nowtime',#催起床图
    'bot_manager_web',#lssv的web管理
    'resignationfor',#yobot的数据生成离职报告
    'vortune',#v占卜
    'pcr-competition',#pcr简易赛跑
    #'eclanrank', #会战排名查询
    'deepchat',#从QQ群的聊天记录中根据关键词选出相似度最高的一句话,用来复读
    'clanrank',#会战排名查询2
}
