from pointMap import pointMap
from rigidMap import rigidMap
import cv2
import sys
import Map

import matplotlib.pyplot as plt

def cart2img(idx):
	"""
	Converts point in Cartesian coords to Img Coords 

	:param      idx:  The index
	:type       idx:  list of x and y coords

	:returns:   list in image coords
	:rtype:     list of x and y coords
	"""
	return [(200-idx[1]),idx[0]]

def main():

	r = input("Enter Robot Radius :")
	c = input("Enter Robot Clearence :")

	r = int(r)
	c = int(c)
	# Generate Map
	a = rigidMap(r,c)

	plt.imshow(a,cmap="gray")
	plt.show()
	sys.exit()
	# Get start node
	sx = input("Enter the start node x coordinate :")
	sy = input("Enter the start node y coordinate :")
	sx = int(sx)
	sy = int(sy)
	s = [sx,sy]
	start = cart2img(s)
	if (a[start[0],start[1]]==255) or ((start[0]<0 and start[0]>300) and (start[1]<0 and start[1]>200)):
		print("Start Node Not Valid! EXIT!!!!!")
		sys.exit(0)

	# Get goal node
	gx = input("Enter the goal node x coordinate :")
	gy = input("Enter the goal node y coordinate :")
	gx = int(gx)
	gy = int(gy)
	g = [gx,gy]
	goal = cart2img(g)
	if (a[goal[0],goal[1]]==255) or ((goal[0]<0 and goal[0]>300) and (goal[1]<0 and goal[1]>200)):
		print("Goal Node Not Valid! EXIT!!!!!")
		sys.exit(0)
	
	# Create map object
	n = Map.Map(a,start,goal)
	ret = n.dijkstra()

	# Backtracking
	sp = n.shortestPath()
	for s in sp:
		n.relaxedMap[:,:,2][s[0],s[1]]=255

	cv2.imshow("Animation",n.relaxedMap)
	k = cv2.waitKey()
	if k==27 & 0xff:
		cv2.destroyAllWindows()

if __name__=='__main__':
	main()