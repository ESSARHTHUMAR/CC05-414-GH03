#this is recevier
import requests
import os
from math import sin,cos,atan2,radians,sqrt,degrees,atan
sen_loc = [0,0]#lat south-north -90,90,long east-west G3 -180,180
des_loc = [0,1]#GH 5
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
if angle>thresold and angle<90-thresold:
	print " west close chose from e and n"
if angle>=90-thresold and angle <=90+thresold:
	print "compulsory straight"
if angle > 90+thresold and angle <180-thresold:
	print "east close chose from w and n"
if angle >= 180-thresold and angle <270-(2*thresold):
	print "compulsory w"
if angle >=270-(2*thresold) and angle <=270+(2*thresold):
	print "U TURN"
if angle >270+(2*thresold) or angle<10:
	print "compulsory east"
