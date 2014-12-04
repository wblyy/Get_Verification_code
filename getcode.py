#coding=utf-8
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
post_verifycode_url = "http://54.223.153.21:9000/"


def post_verifycode(filepath, code=None):
    codetype = {
        "en": "1004",
        "cn": "2004",
        }
    try:
        r = requests.post(post_verifycode_url+"baike_code?type="+codetype[code], files={'code.png': open(filepath, 'rb')}, timeout=60)
    except Exception, e:
        raise
    return r.content


data={
		'userName':"sonidigg",
		'passWord':"sonidigg",
		'verifycode':"e0LD",
		'loginStatus':"userLogin",
		'ischecked':"0"		
}

s = requests.session()
login=s.get('http://www.uuwise.com/Common/Captcha.aspx?t=1417684633627')


s.post(url='http://www.uuwise.com/Common/AjaxLogin.aspx',data=data)
r=s.get('http://www.uuwise.com/User/History.aspx?Action=&d=2014-12-03&page=5')
r.encoding='utf-8'
print r.text


if __name__ == "__main__":
