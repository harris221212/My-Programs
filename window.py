import Xlib
import Xlib.display
import wmctrl
from subprocess import os
import subprocess
import sys

dpy = Xlib.display.Display()

def x11_move_window(window_id_dec, x, y, width, height):
    """ Use x11 library to move window From:
        https://gist.github.com/chipolux/13963019c6ca4a2fed348a36c17e1277
    """

    import Xlib.display

    d = Xlib.display.Display()
    window = d.create_resource_object('window', window_id_dec)
    window.configure(x=x, y=y, width=width, height=height, border_width=0,
                     stack_mode=Xlib.X.Above)
    parent = window.query_tree().parent
    print(parent.get_geometry().x)
    d.sync()

output1 = subprocess.run(["xprop", "-root"], stdout=subprocess.PIPE).stdout.decode('utf-8')

output1Lines = output1.split("\n")
lineWanted = ""
for x in output1Lines:
	if "_NET_CLIENT_LIST_STACKING(WINDOW)" in x:
		lineWanted = x

toMakeArray = lineWanted.partition('#')[2]
arrayA = toMakeArray.split(", ")

#arrayA[0] = arrayA[0][1:len(arrayA[0])]
arrayA.pop(0)
arrayA.pop(len(arrayA)-1)

current = arrayA[len(arrayA)-1]
previous = arrayA[len(arrayA)-2]
#previousA = previous.split("x")
#previous = previousA[0] + "x0" + previousA[1]

window_id_dec = int(previous, 16)
#x11_move_window(window_id_dec, 100, 100, 1000, 1000)


d = Xlib.display.Display()
window = d.create_resource_object('window', window_id_dec)
parent = window.query_tree().parent
mousepadx = parent.get_geometry().x
print(mousepadx)
print(parent.get_geometry().height)

window_id_dec = int(current, 16)
x11_move_window(window_id_dec, 0, 0, 2240-(2240-mousepadx)-10, 1326)
