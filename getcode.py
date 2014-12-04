#coding=utf-8
import requests

data={
		userName:"sonidigg",
		passWord:"dddd",
		verifycode:"e0LD",
		loginStatus:"userLogin",
		ischecked:"0"		
}

s = requests.session()
s.post(url='http://www.uuwise.com/Common/AjaxLogin.aspx',data=data)

r=s.get('http://www.uuwise.com/User/History.aspx?Action=&d=2014-12-03&page=5')
print r.text