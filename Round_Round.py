from turtle import *
def round_round(): 
	length=4
	color("blue")
	pensize(3)
	for _ in range(360):
		forward(length)
		left(5)
		length=length*1.005
