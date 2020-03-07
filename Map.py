import cv2
import numpy as np

class Map:
	"""
	This class describes a map.
	"""
	
	def __init__(self,obs,start,goal):
		"""
		Constructs a new instance.
	
		:param      obs:    Obstacle map
		:type       obs:    numpy array
		:param      start:  Start Node
		:type       start:  list
		:param      goal:   Goal Node
		:type       goal:   list
		"""
		self.SP = []
		self.obs = obs
		self.start = start
		self.goal = goal
		self.cost = np.matrix(np.ones((obs.shape[0],obs.shape[1])) * np.inf)
		self.cost[start[0],start[1]] = 0
		self.relaxed = [[self.start[0],self.start[1],self.start[0],self.start[1]]]
		self.relaxedMap = np.zeros((self.obs.shape[0],self.obs.shape[1],3),np.uint8)
		self.relaxedMap[:,:,0] = np.copy(self.obs)

	def getPossibleNodes(self,idx):
		"""
		Gets the possible nodes.
	
		:param      idx:  The index
		:type       idx:  list
	
		:returns:   The possible nodes.
		:rtype:     list
		"""
		adj = []
		if (idx[0]!=self.obs.shape[0]-1):
			if (idx[1]!=self.obs.shape[1]-1):
				adj.append([idx[0]+1,idx[1]])
				adj.append([idx[0]+1,idx[1]+1])
				adj.append([idx[0],idx[1]+1])
			if (idx[1]!=0):
				adj.append([idx[0],idx[1]-1])
				adj.append([idx[0]+1,idx[1]-1])
				adj.append([idx[0]+1,idx[1]])

		if (idx[0]!=0):
			if (idx[1]!=0):
				adj.append([idx[0]-1,idx[1]])
				adj.append([idx[0]-1,idx[1]-1])
				adj.append([idx[0],idx[1]-1])
			if (idx[1]!=self.obs.shape[1]-1):
				adj.append([idx[0]-1,idx[1]])
				adj.append([idx[0]-1,idx[1]+1])
				adj.append([idx[0],idx[1]+1])
		adj = np.unique(adj,axis=0)
		dst =[]
		for j in adj:
			dst.append(np.linalg.norm(j-idx))
		sorte = adj[np.argsort(dst)]
		return sorte

	def relax(self,c_idx,n_idx):
		"""
		Check Relaxation criteria
	
		:param      c_idx:  The current node index
		:type       c_idx:  list
		:param      n_idx:  The new node index
		:type       n_idx:  list
		"""
		if self.obs[n_idx[0],n_idx[1]]!=255:
			if (self.cost[c_idx[0],c_idx[1]]+np.linalg.norm(c_idx-n_idx)) < (self.cost[n_idx[0],n_idx[1]]) :
				self.cost[n_idx[0],n_idx[1]] = self.cost[c_idx[0],c_idx[1]]+np.linalg.norm(c_idx-n_idx)
				self.relaxed.append([n_idx[0],n_idx[1],c_idx[0],c_idx[1]])
				self.relaxedMap[:,:,1][n_idx[0],n_idx[1]] = 200

			else:
				pass
		else:
			pass

	def isRelaxed(self,idx):
		"""
		Determines whether the specified index is relaxed.
	
		:param      idx:  The index
		:type       idx:  list
	
		:returns:   True if the specified index is relaxed, False otherwise.
		:rtype:     boolean
		"""
		if self.relaxedMap[:,:,1][idx[0],idx[1]]==255:
			return True
		return False

	def dijkstra(self):
		"""
		Implements Dijkstra Shortest Path
	
		:returns:   None
		:rtype:     None
		"""
		j = 0
		
		# Until cost map at goal is infinity as terminating criteria
		while self.cost[self.goal[0],self.goal[1]]==np.inf:

			# Check Goal node
			if self.cost[self.goal[0],self.goal[1]]!= np.inf:
				return True
			print("Iteration: ",j)
			current = self.relaxed[j]
			c_idx = [current[0],current[1]]

			# Explore available adjacent nodes
			adj = self.getPossibleNodes(c_idx)
			for i in adj:
				# Perfrom relaxation on available nodes
				if self.isRelaxed([i[0],i[1]])==False:
					self.relax(c_idx,i)
					rc = []
					for i in self.relaxed:
						rc.append(self.cost[i[0],i[1]])

					# Sort the relaxed nodes in ascending order of their cost
					self.relaxed = [x for _,x in sorted(zip(rc,self.relaxed))]
				
					# View Animation
					cv2.imshow("Animation",self.relaxedMap)
					k = cv2.waitKey(1)
					if k==27 & 0xff:
						cv2.destroyAllWindows()
			print("______________________________")
			j+=1

	def shortestPath(self):
		"""
		Returns Shortest path
	
		:returns:   Indexes of the shortest path
		:rtype:     list
		"""
		print("Back Tracking: ")
		self.relaxed = self.relaxed[::-1]
		i = 0
		goal_node = [self.relaxed[0][0],self.relaxed[0][1]]
		self.SP.append(goal_node)
		while True:
			for i in self.relaxed:
				if [i[0],i[1]]==goal_node:
					goal_node = [i[2],i[3]]
					if goal_node!=self.start:
						self.SP.append(goal_node)
			break
		self.SP.append(self.start)
		print(self.SP)
		return (self.SP)

	def isObstacle(self,idx):
		"""
		Determines whether the specified index is obstacle.
	
		:param      idx:  The index
		:type       idx:  list
	
		:returns:   True if the specified index is obstacle, False otherwise.
		:rtype:     boolean
		"""
		if self.obs[idx[0],idx[1]]==255:
			return True

		else:
			return False
