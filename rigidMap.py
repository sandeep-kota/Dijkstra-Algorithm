import numpy as np

def rigidMap(r,c):
	"""
	Generates map for rigid robot

	:param      r:    Radius
	:type       r:    int
	:param      c:    Clearence
	:type       c:    int

	:returns:   Map
	:rtype:     numpy array
	"""
	b = np.zeros((200,300),np.int8)

	for i in range(0,b.shape[0]):
		for j in range(0,b.shape[1]):
				# Circle
				if ((j-225)**2 + (i-50)**2 < ((25+r+c)**2)):
					b[i,j]=-1

				# Ellipse
				if (((j-150)/(40+r+c))**2 + ((i-100)/(20+r+c))**2 < 1   ):
					b[i,j]=-1

				# Diamond
				if ((0.6*j+i-(295-(r+c)))>0) and ((0.6*j+i-(325+(r+c)))<0) and ((-0.6*j+i-(25-(r+c)))>0) and ((-0.6*j+i-(55+(r+c)))<0):
					b[i,j]=-1

				# Line
				if ((i-0.58*j-(115.15+(r+c)))<0)  and ((i-0.58*j-(103.6-(r+c)))>0) and ((i+1.73*j-(184.55-(r+c)))>0) and ((i+1.73*j-(334.55+(r+c)))<0):
					b[i,j]=-1

				# Right Poly
				if ((i-(15-(r+c))>0)) and ((i-1.4*j+(90+(r+c)))>0) and ((i+1.2*j-(170+(r+c)))<0) and ((i-1.2*j+(10-(r+c)))<0) and ((i+13*j-(340-(r+c)))>0):
					b[i,j]=-1

				if ((i+j-(100+(r+c)))<0) and ((i+13*j-(340-(r+c)))>0) and ((i-1.4*j+(90+(r+c)))>0) and (i-(15-(r+c))>0):
					b[i,j]=-1	

	return b