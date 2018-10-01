# Sergio Rosendo 
# Digital Image Processing 
# September 30, 2018 

# Script calculates the Eucledian and Manhattan distance between two points 
import math 


def calculateEucledianDistance(pointA, pointB):
	print("Eucledian Distance: " + str(round(math.sqrt(math.pow((pointA[0] - pointB[0]), 2) + math.pow((pointA[1] - pointB[1]), 2)), 3)))


def calculateManhattanDistance(pointA, pointB):
	print("Manhattan Distance: " + str(round(math.fabs(pointA[0] - pointB[0]) + math.fabs(pointA[1] - pointB[1]), 3)))



# Core of program 
stopProgram = 0

pointA = [0, 0]
pointB = [0, 0]

while stopProgram == 0:
	print("Enter point A")
	pointA[0] = float(input("A_x: "))
	pointA[1] = float(input("A_y: "))
	print("-")

	print("Enter point B")
	pointB[0] = float(input("B_x: "))
	pointB[1] = float(input("B_y: "))
	print("-")

	calculateEucledianDistance(pointA, pointB)
	calculateManhattanDistance(pointA, pointB)
	print("-")

	stopProgram = int(input("Enter '0' to continue or '1' to stop: "))
	print("")



