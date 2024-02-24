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
#y = int(input("y:"))
y=60
s = int(input("size:"))
#print("1.1 to 2")
#b = float(input("border:"))
b=1.2
h = int(input("height:"))
hh=h
r = int(input("range:"))
print("0:glass 1:stone 2:bricks")
block_id = int(input("block:"))

block_list=["glass","stone","bricks"]

print("wait")
sleep(2)
print("3")
sleep(2)
print("2")
sleep(2)
print("1")
sleep(2)
state = " hollow"
top=1
for xx in range(r):
	for yy in range(r):
		if round(randint(2,10)) > 1:
			block = block_list[block_id]
			press('t')
			if(xx>r-2 or xx==0 or yy>r-2 or yy==0):
				h=int(hh*b)+randint(0,1)
			else:
				h=int(hh/b)
			pos_1 = x+str((s*xx))+" "+str(y)+" "+z+str((s*yy))
			pos_2 = x+str(s+(s*xx))+" "+str(int(y+h))+" "+z+str(s+(s*yy))
			keyboard.type('/fill '+pos_1+" "+pos_2+" minecraft:"+block+state)
			keyboard.press(Key.enter)
			keyboard.release(Key.enter)
			sleep(0.4)
			press('t')
			pos_1 = x+str(int(s+(s*xx)-(s/2)))+" "+str(int(y+1))+" "+z+str(int(s+(s*yy)-(s/2)))
			keyboard.type('/setblock '+pos_1+" minecraft:torch")
			keyboard.press(Key.enter)
			keyboard.release(Key.enter)
			sleep(0.3)
			press('t')
			pos_1 = x+str(int(s+(s*xx)-(s/2)))+" "+str(int(y+(h/2)))+" "+z+str(int(s+(s*yy)))
			keyboard.type('/setblock '+pos_1+" minecraft:air")
			keyboard.press(Key.enter)
			keyboard.release(Key.enter)
			sleep(0.2)
			press('t')
			pos_1 = x+str(int(s+(s*xx)))+" "+str(int(y+(h/2)))+" "+z+str(int(s+(s*yy)-(s/2)))
			keyboard.type('/setblock '+pos_1+" minecraft:air")
			keyboard.press(Key.enter)
			keyboard.release(Key.enter)
			sleep(0.2)
			press('t')
			pos_1 = x+str(int((s*xx)+(s/2)))+" "+str(int(y+(h/2)))+" "+z+str(int((s*yy)))
			keyboard.type('/setblock '+pos_1+" minecraft:air")
			keyboard.press(Key.enter)
			keyboard.release(Key.enter)
			sleep(0.2)
			press('t')
			pos_1 = x+str(int((s*xx)))+" "+str(int(y+1))+" "+z+str(int((s*yy)+(s/2)))
			pos_2 = x+str(int((s*xx)))+" "+str(int(y+2))+" "+z+str(int((s*yy)+(s/2)))
			keyboard.type('/fill '+pos_1+" "+pos_2+" minecraft:air")
			keyboard.press(Key.enter)
			keyboard.release(Key.enter)
			sleep(0.2)
			press('t')
			pos_1 = x+str(int((s*xx)))+" "+str(int(y+1))+" "+z+str(int((s*yy)+(s/2)))
			keyboard.type('/setblock '+pos_1+" minecraft:dark_oak_door[half=lower]")
			keyboard.press(Key.enter)
			keyboard.release(Key.enter)
			sleep(0.2)
			press('t')
			pos_2 = x+str(int((s*xx)))+" "+str(int(y+2))+" "+z+str(int((s*yy)+(s/2)))
			keyboard.type('/setblock '+pos_2+" minecraft:dark_oak_door[half=upper]")
			keyboard.press(Key.enter)
			keyboard.release(Key.enter)
			sleep(0.2)
#exit()
#keyboard.type('t/fill '+str(x)+" "+str(y)+" "+str(z)+" "+str(x)+" "+str(y)+" "+str(z))
#keyboard.type('t/fill '+str(x)+" "+str(y)+" "+str(z)+" "+str(x)+" "+str(y)+" "+str(z))
#keyboard.type('t/fill '+str(x)+" "+str(y)+" "+str(z)+" "+str(x)+" "+str(y)+" "+str(z))
#keyboard.type('t/fill '+str(x)+" "+str(y)+" "+str(z)+" "+str(x)+" "+str(y)+" "+str(z))
#keyboard.type('t/fill '+str(x)+" "+str(y)+" "+str(z)+" "+str(x)+" "+str(y)+" "+str(z))
#keyboard.type('t/fill '+str(x)+" "+str(y)+" "+str(z)+" "+str(x)+" "+str(y)+" "+str(z))
#keyboard.type('t/fill '+str(x)+" "+str(y)+" "+str(z)+" "+str(x)+" "+str(y)+" "+str(z))

