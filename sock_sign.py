import requests


class SockBoom():
    def __init__(self, token_url):
        # 获取外部的token的链接,访问并签到
        url = token_url
        requestHead = {'User-Agent': 'Chrome/83.0.4103.116 Safari/537.36'}
        r = requests.get(url, headers=requestHead)

        # 获得的格式 [{"success":0,"traffic":""}]
        data = eval(r.text)
        success_response = data['success']
        traffic = 0
        if success_response == 1:
            success = '成功'
            traffic = data['traffic'] / (1024 * 1024)
        else:
            success = '失败'
        print('返回值: ' + str(success_response))
        self.msg = '本次SockBoom签到: ' + success + '\r\n共获取流量:' + str(traffic) + 'MB'
        print(self.msg)
        # 发送邮箱

    def get_response_msg(self):
        return self.msg
