import numpy as np
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import axes3d
np.set_printoptions(threshold=np.inf, suppress=True)

#loading the data inputs
data = np.loadtxt('data.txt')

#P = calibrateCamera3D.calibrateCamera3D(data)
#It's function is to process the given parameters to produce a camera matrix

#To find the length of the data
L = len(data)
#Constructing a matrix whch is of 12Nx12 size
A = np.zeros((L* 2, 12))

#Taking the 2D points of the data
data2D = data[::,3:5]*-1

#Splitting the 2D points into their x and y coordinates
data2Dx = data2D[::,0:1]
data2Dy = data2D[::,1:2]

#Repeating the points so that the matrix becomes a (491,4)
data2Dx = np.repeat(data2Dx,4, axis=1)
data2Dy = np.repeat(data2Dy,4, axis=1)

#The matrix will then be multiplied with th 3D points of the data
#The data will be projected in 3D
#Adding Column of ones to the data
#Converting the data into [X,Y,Z,1] form
data3D = data[::,0:3]
ones3D = np.ones((491,1))
data3D = np.append(data3D,ones3D, axis=1)

#The output of the matrix becomes in the form [-xX,-xY,-xZ,-x] [-yX,-yY,-yZ,-y]
Opx = data2Dx * data3D
Opy = data2Dy * data3D

#Fill in the values for Matrix A
A[::2,0:4] = data3D[::,0:4]
A[1::2,4:8] = data3D[::,0:4]
#Fill in the result of the product between 3Dpoints and 2D points
A[::2,8:12] = Opx[::,0:4]
A[1::2,8:12]= Opy[::,0:4]

#Find eigenvalues and eigenvectors of A'A
#Find index of minimum eigenvalue
Z,W = np.linalg.eig(A.transpose().dot(A))
Ind = W[:,np.argmin(Z)]
#Constructing a 3x4 matrix
P = np.zeros((3,4))
P[0:] = Ind[0:4]
P[1:] = Ind[4:8]
P[2:] = Ind[8:]


#visualiseCameraCalibration3D.visualiseCameraCalibration3D(data, P)
#It's function render a 3-D visualization of the parameters of the calibrated camera 

   
#The data will be projected in 3D
#Adding Column of ones to the data
#Converting the data into [X,Y,Z,1] form
data3D = data[::,0:3]
ones3D = np.ones((491,1))
data3D = np.append(data3D,ones3D, axis=1)
    
#Applying dot product to the above matrix and transposing it
data3Ddt = P.dot(data3D.transpose())
#Transposing the obove obtained result  
data3DT = data3Ddt.transpose()

#The obtained matrix is divided by its z cordinates
data3DT[:,0] = data3DT[:,0]/data3DT[:,2]
data3DT[:,0] = data3DT[:,1]/data3DT[:,2]

#Plotting the outputs
fig = plt.figure()
ax=fig.gca()
ax.plot(data3DT[:,0],data3DT[:,1], 'b.')
ax.plot(data[:,3],data[:,4],'r.')
plt.show()
  
#evaluateCameraCalibration3D.evaluateCameraCalibration3D(data, P)
#It's function is to calculate the mean,standard variance, minimum and maximum distance
    
#The data will be projected in 3D
#Adding Column of ones to the data
#Converting the data into [X,Y,Z,1] form
    
data3D = data[::,0:3]
ones3D = np.ones((491,1))
data3D = np.append(data3D,ones3D, axis=1)
    
#Applying dot product to the above matrix and transposing it
data3Ddt = P.dot(data3D.transpose())
#Transposing the obove obtained result
data3DT = data3Ddt.transpose()
    
data2D = data[::,3:5]
#convert the 2D points in the data into homogenous cordinates [x,y,1]
data2DH = data2D*-1
ones2D = np.ones((491,1))
data2DH = np.append(data2DH,ones2D, axis=1)

# To calculate Mean between the points
distance = np.subtract(data2DH,data3DT)
print("Mean: " + str(np.mean(distance)))
	
# To calculate Variance of the measured 2D points
print("Standard variance of measured 2D points: " + str(np.std(data2DH)))
# To calculate Variance of the re-projected 2D points
print("Standard variance of re-projected 2D points: " + str(np.std(data3DT)))

# To calculate Minimum distance between the two matrices
print("Minimum distance between the two matrices: " + str(np.abs(np.min(distance))))
    
# To calculate Maximum distance between the two matrices
print("Maximum distance between the two matrices: " + str(np.abs(np.max(distance))))