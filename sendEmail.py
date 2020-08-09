import os
import email
import smtplib
# 负责构造文本
from email.mime.text import MIMEText

# 负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart
from email.header import Header


class SendEmail():
    def __init__(self, receiver='18357451081@163.com'):
        # 邮件接收者
        self.mail_receivers = receiver
        # SMTP服务器,这里使用q邮箱
        # mail_host = "smtp.163.com"
        mail_host = "smtp.qq.com"
        # 发件人邮箱
        self.mail_sender = "1639822499@qq.com"
        # 邮箱授权码,注意这里不是邮箱密码,如何获取邮箱授权码,请看本文最后教程
        # 在环境中获取Secrets的密码
        license = os.environ['AUTHORIZATION_CODE']

        # 收件人邮箱，可以为多个收件人
        # mail_receivers = ["123.com", "456.com"]

        # 创建SMTP对象
        self.stp = smtplib.SMTP()
        # 设置发件人邮箱的域名和端口，端口地址为25
        self.stp.connect(mail_host, 25)
        # set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
        self.stp.set_debuglevel(1)
        # 登录邮箱，传递参数1：邮箱地址，参数2：邮箱授权码
        self.stp.login(self.mail_sender, license)

    def setContent(self, subject="邮件主题", body="正文内容"):
        self.msg = MIMEMultipart('related')

        # 邮件主题
        # subject_content = """Python邮件测试"""
        subject_content = subject
        # 设置发送者,注意严格遵守格式,里面邮箱为发件人邮箱
        self.msg["From"] = "sender_name<1639822499@qq.com>"
        # 设置接受者,注意严格遵守格式,里面邮箱为接受者邮箱

        self.msg["To"] = "receiver_1_name<18357451081@163.com>"
        # 设置邮件主题
        self.msg["Subject"] = Header(subject_content, 'utf-8')

        # 邮件正文内容
        # body_content = "你好，这是一个测试邮件！"
        body_content = body
        # 构造文本,参数1：正文内容，参数2：文本格式，参数3：编码方式
        message_text = MIMEText(body_content, "plain", "utf-8")
        # 向MIMEMultipart对象中添加文本对象
        self.msg.attach(message_text)

    def send(self):
        # 发送邮件，传递参数1：发件人邮箱地址，参数2：收件人邮箱地址，参数3：把邮件内容格式改为str
        self.stp.sendmail(self.mail_sender, self.mail_receivers, self.msg.as_string())
        print("邮件发送成功")
        # 关闭SMTP对象
        self.stp.quit()
