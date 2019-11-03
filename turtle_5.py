from turtle import *
def turtle_5angle():
	n=300
	length=4
	angle=5
	color("blue",)
	begin_fill()
	for _ in range(n):
		for _ in range(4):
			forward(length)
			left(90)
		left(angle)
		length=length*1.01
