from subprocess import os
import subprocess
import sys
from notifypy import Notify
import pyautogui


notification = Notify()

output1 = subprocess.run(["xclip", "-o"], stdout=subprocess.PIPE).stdout.decode('utf-8')

toPaste = "#" + output1.replace("\n", "\n#")



output1Lines = output1.split("\n")
print(len(output1Lines))
if output1Lines[len(output1Lines)-1] == "":
	output1Lines.pop(len(output1Lines)-1)
output1 = subprocess.run(["xdotool", "keyup", "Control_L", "Shift_L"], stdout=subprocess.PIPE).stdout.decode('utf-8')

for x in output1Lines:
	toPaste = "#" + x
	print(toPaste)
	print("a")
	pyautogui.typewrite(toPaste)
	#output1 = subprocess.run(["xdotool", "type", "--delay", "0", toPaste], stdout=subprocess.PIPE).stdout.decode('utf-8')
	#output1 = subprocess.run(["xdotool", "key", "Return"], stdout=subprocess.PIPE).stdout.decode('utf-8')

notification.title = "Done paste"
notification.send()






#output1 = subprocess.run(["xdotool", "keyup", "Control_L", "Shift_L"], stdout=subprocess.PIPE).stdout.decode('utf-8')
#output1 = subprocess.run(["xdotool", "type", "--delay", "1", toPaste], stdout=subprocess.PIPE).stdout.decode('utf-8')
#output1 = subprocess.run(["xdotool", "key", "Return"], stdout=subprocess.PIPE).stdout.decode('utf-8')
