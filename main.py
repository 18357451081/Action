# 运行Action入口
import os

from sendEmail import SendEmail
from signin import NeteaseSignin
from sock_sign import SockBoom

if __name__ == '__main__':
    # 获取外部变量
    username = os.environ['NETEASE_USERNAME']
    password = os.environ['NETEASE_PASSWORD']
    token_url = os.environ['SOCKBOOM_TOKEN']

    # 网易云音乐签到
    net_sign = NeteaseSignin(username=username, password=password)
    Netease_msg = net_sign.run()

    # SockBoom签到
    # sockboom = SockBoom(token_url=token_url)
    # SockBoom_msg = sockboom.get_response_msg()

    # context = '网易云签到结果如下:\n' + Netease_msg + '\nSockBoom签到结果如下:\n' + SockBoom_msg
    context = '网易云签到结果如下:\n' + Netease_msg
    # 发送邮件
    s = SendEmail()
    s.setContent(subject='尊敬的用户您好! ', body=context)
    s.send()
