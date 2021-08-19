import sys
from api import *
from time import sleep
import numpy as np
import random as r
import cv2
im = cv2.imread("map.png")


#######    YOUR CODE FROM HERE #######################
import random
grid =[]
neigh=[[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]

class Node:
	def __init__(self,value,point):
		self.value = value  #0 for blocked,1 for unblocked
		self.point = point
		self.parent = None
		self.move=None
		self.H = 0
		self.G = 0
		
def isValid(pt):
	return pt[0]>=0 and pt[1]>=0 and pt[0]<200 and pt[1]<200

def neighbours(point):  #returns valid neighbours
	global grid,neigh
	x,y = point.point
	links=[]
	for i in range(len(neigh)):
		newX=x+neigh[i][0]
		newY=y+neigh[i][1]
		if not isValid((newX,newY)):
			continue
		links.append((i+1,grid[newX][newY]))
	return links

def correct(l,x,y):
	for i in range(1,9):
		dis = np.square()


########## Default Level 1 ##########
def level1(botId):
	green = []
	for i in range(200):
		for j in range(200):
			if(im[i][j][0] == 0 and im[i][j][1] == 255 and im[i][j][2] == 0):
				green.append([i,j])
	#print(green[1])

	

	# x,y = get_botPose_list[0]			
	
	mission_complete=False
	botId=0

	for j in green:
		while(not mission_complete):
			for i in range(1,9):
				a = get_botPose_list()
				x,y = a[0]
				# if(a[0] in green):

				successful_move, mission_complete = send_command(botId,i)
				if successful_move:
					b = get_botPose_list()
					x1,y1 = b[0]
					if(((j[0]-x)**2 + (j[1]-y)**2) > ((j[0]-x1)**2 + (j[1]-y1)**2)):
						continue
					else:
						if(i<=4):
							_,_ = send_command(botId,i+4)
						else:
							_,_ = send_command(botId,i-4)	




	# while(not mission_complete):
	# 	successful_move, mission_complete = send_command(botId,r.randint(1,8))
	# 	if successful_move:
	# 		print("YES")
	# 	else:
	# 		print("NO")
	# 	if mission_complete:
	# 		print("MISSION COMPLETE")
	# 	pos=get_botPose_list()
	# 	print(pos[0])


def level2(botId):
	pass

def level3(botId):
	pass

def level4(botId):
	pass

def level5(botId):
	pass

def level6(botId):    
	pass


#######    DON'T EDIT ANYTHING BELOW  #######################

if  __name__=="__main__":
	botId = int(sys.argv[1])
	level = get_level()
	if level == 1:
		level1(botId)
	elif level == 2:
		level2(botId)
	elif level == 3:
		level3(botId)
	elif level == 4:
		level4(botId)
	elif level == 5:
		level5(botId)
	elif level == 6:
		level6(botId)
	else:
		print("Wrong level! Please restart and select correct level")

