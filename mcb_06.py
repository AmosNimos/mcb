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
#glass_color = "black_stained_glass"
glass_color = "gray_stained_glass"
y = int(input("y:"))
if y<1:
	y=1
print("0:glass 1:stone 2:bricks 3:stone_bricks","4:sea_lantern")
block_id = int(input("block:"))
block_list=["glass","stone","bricks","stone_bricks","sea_lantern"]
block = block_list[block_id]
size = int(input("size:"))
initial_size = size
addglass = False
height  = 0
h = 5
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
	#keyboard.press(Key.enter)
	#keyboard.release(Key.enter)

for yy in range(int(size*1.3)):
	if size>6:
		size -= 1
	else:
		break
		exit()
		print("stop")
	size_str = str(int(size)+5)
	size_corection_str = str(int(initial_size-size)+5)
	floor_bot = str(int(y-height))
	floor_top = str(int(y-height-h))
	pos_1 = x+size_corection_str+" "+floor_bot+" "+z+size_corection_str
	pos_2 = x+size_str+" "+floor_top+" "+z+size_str
	enter_txt('/fill '+pos_1+" "+pos_2+" minecraft:"+block+" hollow")
	if addglass == True:
		#glass
		size_str = str(int(size)+5)
		size_corection_str = str(int(initial_size-size)+5)
		floor_bot = str(int(y-height)-4)
		floor_top = str(int(y-height-h)+4)
		pos_1 = x+size_corection_str+" "+floor_bot+" "+z+size_corection_str
		pos_2 = x+size_str+" "+floor_top+" "+z+size_str
		enter_txt('/fill '+pos_1+" "+pos_2+" minecraft:"+glass_color+" replace "+block)
	#go up one floor
	height+=h
											

