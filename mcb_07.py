from pynput.keyboard import Key, Controller
from pyautogui import press
from math import cos
from math import sin
from time import sleep
from random import randint
keyboard = Controller()

#x = int(input("x:"))
#z = int(input("z:"))
x="~"
z="~"
y="~"
#glass_color = "black_stained_glass"
#glass_color = "gray_stained_glass"
glass_color = "glass"
#print("0:glass 1:stone 2:bricks 3:stone_bricks","4:sea_lantern")
#block_id = int(input("block:"))
block_list=["oak_leaves","bookshelf","gray_wool","oak_planks","ice","black_stained_glass","glass","stone","bricks","stone_bricks","sea_lantern","dirt"]
#block = block_list[block_id]
#size = int(input("size:"))
size = 20
#siz=8
siz=5
initial_size = siz
height  = 0
h = 6
zz=1
zzz=zz

print("wait")
sleep(2)
print("3")
sleep(2)
print("2")
sleep(2)
print("1")
sleep(2)

def enter_txt(text):
	sleep(0.4)
	press('t')
	keyboard.type(text)
	press('enter')
	sleep(0.4)
	
def place_block(block_name,pos):
	enter_txt('/setblock '+pos+" minecraft:"+block_name)

for yy in range(int(size*1.3)):
	if siz<size:
		siz += 1
	else:
		break
		exit()
		print("stop")
	size_str = str(int(siz)+initial_size)
	size_corection_str = str(int(initial_size-siz)+initial_size)
	floor_bot = y+str(int(-height))
	floor_top = y+str(int(-height-h))
	pos_1 = x+size_corection_str+" "+floor_bot+" "+z+size_corection_str
	pos_2 = x+size_str+" "+floor_top+" "+z+size_str
	block = block_list[randint(0,len(block_list)-1)]
	enter_txt('/fill '+pos_1+" "+pos_2+" minecraft:"+block+" hollow")
	
	#torches in corner
	c1 = str(int(size_corection_str)+1)
	pos_1 = x+c1+" "+y+str(int(-height-h)+1)+" "+z+c1
	place_block("torch",pos_1)
	#pos_1 = x+size_corection_str+" "+y+str(int(-height-h)+1)+" "+z+c1
	#place_block("torch",pos_1)
	c2 = str(int(size_str)-1)
	pos_2 = x+c2+" "+y+str(int(-height-h)+1)+" "+z+c2
	place_block("torch",pos_2)
	#pos_2 = x+size_str+" "+y+str(int(-height-h)+1)+" "+z+c2
	#place_block("torch",pos_2)
	#glass
	#size_str = str(int(siz)+initial_size)
	#size_corection_str = str(int(initial_size-siz)+initial_size)
	#floor_bot = y+str(int(-height)-4)
	#floor_top = y+str(int(-height-h)+4)
	#pos_1 = x+size_corection_str+" "+floor_bot+" "+z+size_corection_str
	#pos_2 = x+size_str+" "+floor_top+" "+z+size_str
	#enter_txt('/fill '+pos_1+" "+pos_2+" minecraft:"+block_list[randint(0,len(block_list)-1)]+" replace "+block)
	#go up one floor
	height+=h
	#h+1
											

