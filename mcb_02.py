from pynput.keyboard import Key, Controller
from pyautogui import press
from math import cos
from math import sin
from time import sleep
from random import randint
keyboard = Controller()

x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))
s = int(input("size:"))
h = int(input("height:"))
block = str(input("block:"))

#x=100
#y=4
#z=200
#h=100

#x="~"
#y=4
#z="~"
s=60

print("wait")
sleep(2)
print("3")
sleep(2)
print("2")
sleep(2)
print("1")
sleep(2)
for xx in range(s):
	for yy in range(s):
		if round(randint(2)) == 1:
			state = " outline"
		else:
			state = " hollow"
		spr=int(cos(0.1*i)*(s/4.5))
		ssr=int(sin(0.1*i)*(s/4.5))
		press('t')
		pos_1 = str(x+(s*xx))+" "+str(y)+" "+str(z+(s*yy))
		pos_2 = str(x+s+(s*xx))+" "+str(y+h+randint(-5,5))+" "+str(z+s+(s*yy))
		keyboard.type('/fill '+pos_1+" "+pos_2+" minecraft:"+block+state)
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		sleep(0.3)
#exit()
#keyboard.type('t/fill '+str(x)+" "+str(y)+" "+str(z)+" "+str(x)+" "+str(y)+" "+str(z))
#keyboard.type('t/fill '+str(x)+" "+str(y)+" "+str(z)+" "+str(x)+" "+str(y)+" "+str(z))
#keyboard.type('t/fill '+str(x)+" "+str(y)+" "+str(z)+" "+str(x)+" "+str(y)+" "+str(z))
#keyboard.type('t/fill '+str(x)+" "+str(y)+" "+str(z)+" "+str(x)+" "+str(y)+" "+str(z))
#keyboard.type('t/fill '+str(x)+" "+str(y)+" "+str(z)+" "+str(x)+" "+str(y)+" "+str(z))
#keyboard.type('t/fill '+str(x)+" "+str(y)+" "+str(z)+" "+str(x)+" "+str(y)+" "+str(z))
#keyboard.type('t/fill '+str(x)+" "+str(y)+" "+str(z)+" "+str(x)+" "+str(y)+" "+str(z))

