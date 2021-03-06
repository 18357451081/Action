'''
    Server推送
    '''
import datetime
import json

import requests
class Tools():
    def __init__(self,name,sckey):
        # Server酱的密匙,不需要推送就留空,密匙的免费申请参考:http://sc.ftqq.com/
        self.sckey = sckey
        # 本Tools的名称
        self.name = name

    def server(self,content):
            if self.sckey == '':
                return
            url = 'https://sc.ftqq.com/' + self.sckey + '.send'
            self.diyText(content) # 构造发送内容
            response = requests.get(url,params={"text":'SockBoom签到详情', "desp":self.content})
            data = json.loads(response.text)
            if data['errno'] == 0:
                self.log('用户:' + self.name + '  Server酱推送成功')
            else:
                self.log('用户:' + self.name + '  Server酱推送失败,请检查sckey是否正确')


    '''
    自定义要推送到微信的内容
    title:消息的标题
    content:消息的内容,支持MarkDown格式
    '''
    def diyText(self,content):
        self.content = content

    '''
    打印日志
    '''
    def log(self, text):
        time_stamp = datetime.datetime.now()
        print(time_stamp.strftime('%Y.%m.%d-%H:%M:%S') + '   ' + str(text))
        self.time =time_stamp.strftime('%H:%M:%S')

    def requests_get(self,url):
        requestHead = {'User-Agent': 'Chrome/83.0.4103.116 Safari/537.36'}
        return requests.get(url=url, headers=requestHead)