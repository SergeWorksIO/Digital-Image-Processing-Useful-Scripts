# Sergio Rosendo 
# Digital Image Processing 
# September 30 2018

# Script estimates intensity value at desired pixel location
# given 4 neighboring pixels and their respective pixel values

# EX:

#		  NA

#  NA              NB
# Y0,X0          Y1,X0
# (I0)			 (I1)

#		 (I?)
#		  X,Y

# (I2)			(I3)
# Y0,X1	        Y1,X1
#  NC            ND

#		  NB

def linearInterpolation(point, neighborA, neighborB, type):
	if type == "HORIZONTAL":
		return (neighborA[2] * ((neighborB[0] - point[0]) / (neighborB[0] - neighborA[0]))) + (neighborB[2] * ((point[0] - neighborA[0]) / (neighborB[0] - neighborA[0])))

	elif type == "VERTICAL":
		return (neighborA[2] * ((neighborB[1] - point[1]) / (neighborB[1] - neighborA[1]))) + (neighborB[2] * ((point[1] - neighborA[1]) / (neighborB[1] - neighborA[1])))


def bilinearInterpolation(point, neighborA, neighborB, neighborC, neighborD):
	# Obtaining vertical interpolation points and their estimated values
	verticalInterpolantA = [point[0], neighborA[1], linearInterpolation(point, neighborA, neighborB, "HORIZONTAL")]
	verticalInterpolantB = [point[0], neighborC[1], linearInterpolation(point, neighborC, neighborD, "HORIZONTAL")]

	print("Estimated intensity:" + str(round(linearInterpolation(point, verticalInterpolantA, verticalInterpolantB, "VERTICAL"), 3)))






stopProgram = 0

point     = [0,0]
neighborA = [0, 0, 0]
neighborB = [0, 0, 0]
neighborC = [0, 0, 0]
neighborD = [0, 0, 0]

while stopProgram == 0:
	print("Enter desired pixel location")
	point[0] = float(input("P_x: "))
	point[1] = float(input("P_y: "))
	print("-")

	print("Enter neighbor A")
	neighborA[0] = float(input("NA_x: "))
	neighborA[1] = float(input("NA_y: "))
	neighborA[2] = float(input("NA_i: "))
	print("-")

	print("Enter neighbor B")
	neighborB[0] = float(input("NB_x: "))
	neighborB[1] = float(input("NB_y: "))
	neighborB[2] = float(input("NB_i: "))
	print("-")

	print("Enter neighbor C")
	neighborC[0] = float(input("NC_x: "))
	neighborC[1] = float(input("NC_y: "))
	neighborC[2] = float(input("NC_i: "))
	print("-")

	print("Enter neighbor D")
	neighborD[0] = float(input("ND_x: "))
	neighborD[1] = float(input("ND_y: "))
	neighborD[2] = float(input("ND_i: "))
	print("-")

	bilinearInterpolation(point, neighborA, neighborB, neighborC, neighborD)
	print("---")

	stopProgram = input("Enter '0' to continue or '1' to stop program: ")






