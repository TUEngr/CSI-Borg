#!/usr/bin/env
import roslib
import rospy
from geometry_msgs.msg import *
from subprocess import call
import time
def main():
	#Startup Block
	call('gnome-terminal -e \'mplayer -geometry +1280+0 -fs blackscreen.mov\'',shell=True)#need to know actual screen dimensions
	call('gnome-terminal -e \'roslaunch turtlebot_bringup minimal.launch\'',shell=True)
	call('gnome-terminal -e \'roslaunch turtlebot_navigation amcl_demo.launch map_file:=/home/maps/csi_2nd_floor.yaml\'',shell=True)
	time.sleep(15)
	call('rostopic pub -1 /initialpose geometry_msgs/PoseWithCovarianceStamped \'{header: {stamp: now, frame_id: /map}, pose: {pose: {position: {x: '+x+', y: '+y+', z: 0.0}, orientation: {z: '+z+', w: '+w+'}},xCoord = y[0]; yCoord = y[1]; wCoord = y[2]; zCoord = y[3] covariance: [0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.06853891945200942]}}\'',shell=True)#This will fail until coords are put in
	#tOpt = 0
	#while (tOPt == 0)
		#time.sleep(1)
	#The GUI will need to be able to change this value
	#tName = 'tour'+tName+'.txt' #The idea is that the different tours will just have a different number appended to the end of the file name
	#call('mplayer -geometry +1280+0 -fs introtour_'+tOpt+'.mov',shell=True)
	tData = open(tName,'r')
	for line in tData:
		line = line.rstrip('\n')
		x = line.split('$')
		if x[0] == 'mg': #movegoal
                        y = x[1].split(' ')
			xCoord = y[0]; yCoord = y[1]; zCoord = y[2]; wCoord = y[3] 
                        lastGoal = moveGoal(xCoord,yCoord,zCoord,wCoord)
		elif x[0] == 'mgwc': #movegoal with check
			xCoord = y[0]; yCoord = y[1]; zCoord = y[2]; wCoord = y[3] 
			lastGoal = goalCheck(0,xCoord,yCoord,zCoord,wCoord)
		elif x[0] == 'mav': #moving audio video
			lastName=moveAV(x[1])
		elif x[0] == 'sav': #stationary audio video
			stillAV(x[1],lastName)
		elif x[0] == 'elev': #elevator protocol
		#stuff the robot needs to do to change floors
		elif x[0] == 'pose': #initial pose
			y = x[1].split(' ')
			xPose = y[0]; yPose = y[1]; zPose = y[2]; wPose = y[3]
			inPose(xPose,yPose,zPose,wPose)  
	tData.close()

def moveGoal(x,y,z,w):
	info = 'rostopic pub -1 /move_base_simple/goal geometry_msgs/PoseStamped \'{header: {stamp: now, frame_id: /map}, pose: {position: {x: '+x+', y: '+y+', z: 0.0}, orientation: {z: '+z+', w: '+w+'}}}\''	
	call(info,shell=True)
	return (x,y,z,w)

def goalCheck(count,thresh,x,y,z,w):
	state = self.move_base.get_state()
        if count > thresh:
                ox = lastGoal[0]; oy = lastGoal[1]; oz = lastGoal[2]; ow = lastGoal[3];
		moveGoal(ox,oy,oz,ow)
                goalCheck(0,thresh/2,x,y,z,w)
	if state == GoalStatus.SUCCEEDED:
                moveGoal(x,y,z,w)
        elif:
                time.sleep(2)
                goalCheck(count+1,x,y,z,w)
		
def moveAV(name):
	info = 'gnome-terminal -e \'mplayer -geometry +1280+0 -fs '+name+'\''
	call(info,shell=True)
	return name
	#commands to select the proper screen and turnon/off
	#code for fullscreen other screen with mplayer: mplayer -geometry +1280+0 -fs sample_iTunes.mov 

def stillAV(name,lastName):
	info = 'ps aux|grep '+lastName+'>>procs.txt'
	num = 3
	while num>1:
		call = (info,shell=True)
    	data = open('procs.txt','r')	
		num = 0
		for stuff in data:
			num=num+1
		call('rm procs.txt',shell=True)
	info2 = 'mplayer -geometry +1280+0 -fs '+name
	call(info2,shell=True)

def inPose(x,y,w,z):		
	info = 'rostopic pub -1 /initialpose geometry_msgs/PoseWithCovarianceStamped \'{header: {stamp: now, frame_id: /map}, pose: {pose: {position: {x: '+x+', y: '+y+', z: 0.0}, orientation: {z: '+z+', w: '+w+'}},xCoord = y[0]; yCoord = y[1]; wCoord = y[2]; zCoord = y[3] covariance: [0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.06853891945200942]}}\''
	call(info,shell=True)

def bumpCheck():

def errorCatch():
        #routine to restart the bot in the case of fatal error. includes rebooting all the os of the robot and possibly setting an initial pose of last known spot

def elev(floor):
        
if __name__ == '__main__':
	main()
