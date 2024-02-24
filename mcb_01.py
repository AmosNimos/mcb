from pynput.keyboard import Key, Controller
from pyautogui import press
from math import cos
from math import sin
from time import sleep
keyboard = Controller()

#x = int(input("x:"))
#y = int(input("y:"))
#z = int(input("z:"))
#s = int(input("size:"))

x=100
y=4
z=200
h=100

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
for hip in range(h):
	for i in range(s):
		spr=int(cos(0.1*i)*(s/4.5))
		ssr=int(sin(0.1*i)*(s/4.5))
		press('t')
		keyboard.type('/setblock '+str(x+spr)+" "+str(y+hip)+" "+str(z+ssr)+" minecraft:magma_block replace")
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

