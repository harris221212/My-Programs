#!/usr/bin/env python3

from rofi import Rofi
r = Rofi()
name = r.text_entry("Enter New Bookmark")
fileName = "/home/ethan/Programs/log/bookmarks.txt"
f = open(fileName, "a")
f.write(name + "\n")
f.close()
