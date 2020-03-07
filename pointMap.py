import numpy as np

def pointMap():
	"""
	Generates map for point robot

	:returns:   Map
	:rtype:     numpy array
	"""
	a = np.zeros((200,300),np.uint8)
	for i in range(0,a.shape[0]):
		for j in range(0,a.shape[1]):
				if ((j-225)**2 + (i-50)**2 < (25**2)):
					a[i,j]=255

				if (((j-150)/40)**2 + ((i-100)/20)**2 < 1   ):
					a[i,j]=255

				if ((0.6*j+i-295)>0) and ((0.6*j+i-325)<0) and ((-0.6*j+i-25)>0) and ((-0.6*j+i-55)<0):
					a[i,j]=255

				if ((i-0.58*j-115.15)<0)  and ((i-0.58*j-103.6)>0) and ((i+1.73*j-184.55)>0) and ((i+1.73*j-334.55)<0):
					a[i,j]=255

				if ((i-15>0)) and ((i-1.4*j+90)>0) and ((i+1.2*j-170)<0) and ((i-1.2*j+10)<0):
					a[i,j]=255
				if ((i+j-100)<0) and ((i+13*j-340)>0) and ((i-1.4*j+90)>0) and (i-15>0):
					a[i,j]=255

	return a