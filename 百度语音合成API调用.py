import requests
import json
import easygui as g

def token():

	url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials"

	key1 = "" #API Key

	key2 = "EzrFVufa6q00X6vIbanPRS0Wi84AYtrG" #Secret Key

	url2 = url + "&client_id=" + key1 + "&client_secret=" + key2

	a = requests.get(url2)

	b = json.loads(a.text)

	tokens = b['access_token']

	return tokens

def request(token,text,per,output):

	url = "https://tsn.baidu.com/text2audio"

	data = {
		"tex":text.encode('utf-8'),
		"tok":token,
		"cuid":"",  #MAC地址或IMEI码
		"ctp":"1",
		"lan":"zh",
		"per":per
		}

	a = requests.post(url,data=data)

	b = open("./%s.mp3"%output,"wb")

	b.write(a.content)

	b.close()


a = token()

per = g.choicebox("请选择角色","语音合成",("度小宇","度小美","度逍遥","度丫丫","度博文","度小童","度小萌","度米朵","度小娇"))

text = g.enterbox("请输入要合成的文字","语音合成")

output = g.enterbox("请输入要输出的文件名称","语音合成")

per1 = {"度小宇":"1","度小美":"0","度逍遥":"3","度丫丫":"4","度博文":"106","度小童":"110","度小萌":"111","度米朵":"103","度小娇":"5"}

per2 = per1[per]

request(a,text,per2,output)






