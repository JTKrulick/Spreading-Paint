import pygame
import math
#reduce=0
width = 1440
height = 1220
spreadspeed = 2
addspeed = 10000
points = {}
size =30
mix =100
class Point:
	def __init__(self,X,Y,r,g,b,tot):
		self.x=X
		self.y=Y
		self.red=r
		self.green =g
		self.blue = b
		self.amount =tot
def setup():

	for x in range (0,width/size):
		for y in range(0,height/size):

			points[(x,y)]=Point(x,y,0,0,0,0)

def spread():

	min = spreadspeed;
	for x in range (0,width/size):
		for y in range(0,height/size):
#			points[x,y].amount = points[x,y].amount-reduce
			if(x>0):
				combine(x,y,x-1,y)
			if(x<width/size-1):
				combine(x,y,x+1,y)
			if(y>0):
				combine(x,y,x,y-1,spreadspeed/2)
			if(y<height/size-1):
				combine(x,y,x,y+1,spreadspeed/2)
			if(x<width/size-1 and y>0):
				combine(x,y,x+1,y-1,spreadspeed/2)
			if(x>0 and y>0):
				combine(x,y,x-1,y-1,spreadspeed/2)
			if(x>0 and y<height/size-1):
				combine(x,y,x-1,y+1,spreadspeed/2)
			if(x<width/size-1 and y<height/size-1):
				combine(x,y,x+1,y+1)			
				
			if (points[x,y].amount<min):
				min = points[x,y].amount
#	if(min>0):
#		reduce = min-1
#	else:
#		reduce =0
def combine(x1,y1,x2,y2,spread=spreadspeed):#moves color from point1 to point2
	point1=points[x1,y1]
	point2=points[x2,y2]
	if point1.amount-spread>point2.amount:
		point2.red=(point2.red*point2.amount+point1.red*spread)/(point2.amount+spread)
		point2.green=(point2.green*point2.amount+point1.green*spread)/(point2.amount+spread)
		point2.blue=(point2.blue*point2.amount+point1.blue*spread)/(point2.amount+spread)
		point1.amount = point1.amount - spread;
		point2.amount = point2.amount + spread;
	else:
		temp =math.fabs(point2.red-point1.red)+math.fabs(point2.green-point1.green)+math.fabs(point2.blue-point1.blue)
			
		if point1.amount==point2.amount and point1.amount!=0 and temp>(mix):
			point2.red=(point2.red*point2.amount+point1.red*spread)/(point2.amount+spread)
			point2.green=(point2.green*point2.amount+point1.green*spread)/(point2.amount+spread)
			point2.blue=(point2.blue*point2.amount+point1.blue*spread)/(point2.amount+spread)
		
def add(x,y,r,g,b):
	temp = points[x,y]
	temp.red = (temp.red*temp.amount+r*addspeed)/(temp.amount+addspeed)
	temp.green = (temp.green*temp.amount+g*addspeed)/(temp.amount+addspeed)
	temp.blue = (temp.blue*temp.amount+b*addspeed)/(temp.amount+addspeed)
	temp.amount = temp.amount+addspeed
	
#def test():
	#setup()
	#add(2,2,100,0,0)
	#for temp in range(10):
		#spread()
		#print "	"
		#print "	"
		#for x in range (0,width):
			#print "	"
			#for y in range(0,height):
				#print points[x,y].amount,
def gui():
	setup()
	pygame.init()
	screen = pygame.display.set_mode((width, height))
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	#background.fill((250, 250, 250))
	running = True
	#add(1,1,255,0,0)
	#add(33,1,0,255,0)
	add(25,25,0,0,255)
	while running:
		spread()
		for x in range (0,width/size):
			for y in range(0,height/size):
				pygame.draw.rect(screen,(points[x,y].red, points[x,y].green, points[x,y].blue),(x*size,y*size,size,size))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		pygame.display.flip()
	pygame.quit()
	for x in range (0,width):
		print " "
		for y in range(0,5):
			print(points[x,y].amount),
			
			
