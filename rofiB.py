#!/usr/bin/env python3

from rofi import Rofi
import pyperclip3

fileName = "/home/ethan/Programs/log/bookmarks.txt"
f = open(fileName, "r")
bookmarks = f.readlines()
#lengthA = len(bookmarks)
#del bookmarks[lengthA-1]
f.close()

for i,x in enumerate(bookmarks):
	bookmarks[i] = x.strip()
r = Rofi()
index, key = r.select("Select Bookmark To Copy To Clipboard", bookmarks, key5=("Alt+w", "Delete"))
if key == 5:
	del bookmarks[index]
	f = open(fileName, "w")
	for x in bookmarks:
		f.write(x)
		f.write("\n")
	f.close()
elif key == 0:
	pyperclip3.copy(bookmarks[index])
#pyperclip.paste()

