# 运行Action入口
import datetime
import os
# 捕获异常信息
import traceback

# from sendEmail import SendEmail
from signin import NeteaseSignin
from sock_sign import SockBoom
from tools import Tools

if __name__ == '__main__':
    # 获取外部变量
    # username = os.environ['NETEASE_USERNAME']
    # password = os.environ['NETEASE_PASSWORD']
    token_url = os.environ['SOCKBOOM_TOKEN']
    sckey = os.environ['SCKEY']

    tools = Tools('SockBoom的签到',sckey)

    # 网易云音乐签到
    # try:
    #     net_sign = NeteaseSignin(username=username, password=password)
    #     Netease_msg = net_sign.run()
    # except Exception:
    #     print('网易云音乐签到 异常')
    #     traceback.print_exc()

    # SockBoom签到
    try:
        sockboom = SockBoom(token_url=token_url)
        SockBoom_msg = sockboom.get_response_msg()
    except Exception:
        tools.log('SockBoom签到 异常')
        traceback.print_exc()

    context ='SockBoom签到结果如下:\n' + SockBoom_msg
    # context = '网易云签到结果如下:\n' + Netease_msg + '\nSockBoom签到结果如下:\n' + SockBoom_msg
    # context = '网易云签到结果如下:\n' + Netease_msg
    # 发送邮件
    # s = SendEmail()
    # s.setContent(subject='尊敬的用户您好! ', body=context)
    # s.send()
    today = datetime.date.today()
    kaoyan_day = datetime.date(2020, 12, 21)  # 2021考研党的末日
    date = (kaoyan_day - today).days

    one = tools.requests_get('https://api.qinor.cn/soup/').text  # 每日一句的api
    content = (
            "------\n"
            "#### 账户信息\n"
            "------\n"
            + context +
            "------\n"
            "#### 考研倒计时\n- 距考研还有" + str(date) + "天，主人要加油学习啊！\n\n"
			"------\n"
            "#### 今日一句\n- " + one + "\n\n")
    tools.diyText(content)
    tools.server()
