#this is recevier
import requests
import os

def getdata():
	with requests.Session() as c:
			try:
				url = 'http://192.168.132.86:8080/'
				page = c.get(url)
				data= page.content
				return data.split(' ')
			except:
				url = 'http://192.168.132.72:8080/'
				page = c.get(url)
				data= page.content
				return data.split(' ')

while(1):
	try:
		os.system('cls')
		print getdata()
	except KeyboardInterrupt:
		break
	except:
		continue
		
