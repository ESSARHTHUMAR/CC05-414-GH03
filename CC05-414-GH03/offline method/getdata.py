#this is recevier
import requests
import os
from math import sin,cos,atan2,radians,sqrt,degrees,atan
sen_loc = [23.2197858,72.6338909]#lat south-north -90,90,long east-west G3 -180,180
des_loc = [23.2329485,72.6513107]#GH 5


dlon = des_loc[1] - sen_loc[1]
dlat = des_loc[0] - sen_loc[0]
dlon = radians(des_loc[1]) - radians(sen_loc[1])
dlat = radians(des_loc[0]) - radians(sen_loc[0])
R = 6373
a = sin(dlat / 2)**2 + cos(radians(sen_loc[0])) * cos(radians(des_loc[0])) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))
distance = R * c
try:
	deg = degrees(atan((radians(des_loc[1]) - radians(sen_loc[1]))/(radians(des_loc[0]) - radians(sen_loc[0]))))
except ZeroDivisionError:
	deg =90
print distance,"km"
latdiff= des_loc[0]-sen_loc[0]
longdiff = des_loc[1]-sen_loc[1]
thresold = 10

def get360deg(deg):
	k=0
	if longdiff>0 and deg>0:
		k= deg
	elif longdiff>0 and deg<0:
		k= 180+deg
	elif longdiff<0 and deg>0:
		k= 180+deg
	elif longdiff<0 and deg<0:
		k= 360+deg
	elif longdiff==0:
		if latdiff >0: k=0
		else: k=180
	return k
angle= get360deg(deg)

def getdata():
	with requests.Session() as c:
			try:
				url = 'http://192.168.132.86:8080/'
				page = c.get(url)
				data= page.content
				dat = data.split(' ')
				return dat
			except:
				url = 'http://192.168.43.1:8080/'
				page = c.get(url)
				data= page.content
				dat = data.split(' ')
				return dat

while(1):
	try:
		os.system('cls')
		x = getdata()
		if angle>thresold and angle<90-thresold:
			if x[1]<x[2]:
				print "Take North path"
			else : print "Take East Path"
		if angle>=90-thresold and angle <=90+thresold:
			print "Go Straight"
		if angle > 90+thresold and angle <180-thresold:
			if x[0]>x[1]:
				print "Take North path"
			else :
				print "Take West Path"
		if angle >= 180-thresold and angle <270-(2*thresold):
			print "Take West path"
		if angle >=270-(2*thresold) and angle <=270+(2*thresold):
			print "Take U-turn"
		if angle >270+(2*thresold) or angle<10:
			print "Take East path"
	except KeyboardInterrupt:
		break
	except:
		continue
		
