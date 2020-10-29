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
    token = os.environ['SOCKBOOM_TOKEN']
    sckey = os.environ['SCKEY_CODE']

    tools = Tools('SockBoom的签到',sckey)
    tools.log(sckey)

    # SockBoom签到
    sockboom_msg = "消息未空(异常)!"
    try:
        sockboom = SockBoom(token=token)
        sockboom_msg = sockboom.get_response_msg()
    except Exception:
        tools.log('SockBoom签到 异常')
        traceback.print_exc()
    context = sockboom_msg
    today = datetime.date.today()
    kaoyan_day = datetime.date(2020, 12, 21)  # 2021考研党的末日
    date = (kaoyan_day - today).days

    one = tools.requests_get('https://api.qinor.cn/soup/').text  # 每日一句的api
    content = (
            "------\n"
            "#### 账户信息\n"
            "------\n"
            "#### SockBoom签到结果\n"
            + "- " + context + "\n\n" +
            "------\n"
            "#### 考研倒计时\n- 距考研还有" + str(date) + "天，主人要加油学习啊！\n\n"
			"------\n"
            "#### 今日一句\n- " + one + "\n\n")
    tools.server(content)
