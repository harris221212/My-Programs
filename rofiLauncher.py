#!/usr/bin/env python3

from rofi import Rofi
import os
from subprocess import Popen
import subprocess
import sys

filePrograms = {
	"txt": "mousepad",
	"mp3": "mpv",
	"m4a": "mpv",
	"mp4": "mpv",
	"webm": "mpv",
	"mov": "mpv",
	"avi": "mpv",
	"png": "gthumb",
	"webp": "gthumb",
	"jpg": "gthumb",
	"jpeg": "gthumb",
	"inputrc": "mousepad",
	"xml": "mousepad",
	"css": "mousepad",
	"md": "mousepad",
	"rc": "mousepad",
	"json": "mousepad",
	"sh": "mousepad",
	"git": "mousepad",
	"conf": "mousepad",
	"py": "mousepad",
	"rasi": "mousepad",
	"mk": "mousepad",
	"h": "mousepad",
	"desktop": "mousepad",
	"AppImage": "binary",
	"crt": "mousepad",
	"bash": "mousepad",
	"config": "mousepad",
	"log": "mousepad",
	"tmp": "mousepad",
	"ini": "mousepad",
	"txt": "mousepad",
	"old": "mousepad",
	"code": "mousepad",
	"backup": "mousepad",
	"vscdb": "mousepad",
	"haskell": "mousepad",
	"c": "mousepad",
	"cnf": "mousepad",
	"hs": "mousepad",
	"groff": "mousepad",
	"java": "mousepad",
	"dat": "mousepad",
	"js": "mousepad",
	"gif": "gthumb",
	"html": "mousepad",
	"json~": "mousepad",
	"bak": "mousepad",
	"ico": "mousepad",
	"svg": "mousepad",
	"yml": "mousepad",
	"cache": "mousepad",
	"po": "mousepad",
	"ac": "mousepad",
	"m": "mousepad",
	"install": "mousepad",
	"x": "mousepad",
	"y": "mousepad",
	"cabal": "mousepad",
	"mdown": "mousepad",
	"markdown": "mousepad",
	"micro": "mousepad",
	"toml": "mousepad",
	"orig": "mousepad",
	"yaml": "mousepad",
	"README": "mousepad",
	"bat": "mousepad",
	"cpp": "mousepad",
	"pl": "mousepad",
	"dll": "mousepad",
	"app": "mousepad",
	"icns": "mousepad",
	"man": "mousepad",
	"fish": "mousepad",
	"rtf": "mousepad",
	"cc": "mousepad",
	"d": "mousepad",
	"vscode": "mousepad",
	"ghc": "mousepad",
	"sys": "mousepad",
	"ssh": "mousepad",
	"pub": "mousepad",
	"xinitrc": "mousepad",
	"srt": "mousepad",
	"kdenlive": "kdenlive",
	"aac": "mpv",
	"vtt": "mousepad",
	"wav": "mpv",
	"ma": "mousepad",
	"mkv": "mpv",
	"mozilla": "mousepad",
	"dmp": "mousepad",
	"co": "mousepad",
	"ghcup": "mousepad",
	"nanorc": "mousepad",
	"pki": "mousepad",
	"themes": "mousepad",
	"gpg": "mousepad",
	"tar": "mousepad",
	"gitconfig": "mousepad",
	"profile": "mousepad",
	"s": "mousepad",
	"dmrc": "mousepad",
	"nano": "mousepad",
	"bashrc": "mousepad",
	"lesshst": "mousepad",
	"xpm": "mousepad",
	"xbm": "mousepad",
	"styles": "mousepad",
	"layout": "mousepad",
	"menu": "mousepad",
	"doc": "mousepad",
	"htm": "mousepad",
	"ogg": "mpv",
	"bmp": "gthumb",
	"ods": "mousepad",
	"out": "mousepad",
	"ms": "mousepad",
}

keys = filePrograms.keys()


f = open("/home/ethan/Programs/log/files.txt", "r")
fullArray = f.readlines()
f.close()

r = Rofi()
index, key = r.select("Launcher", fullArray)

if key == -1:
	exit()

answer = fullArray[index]

def openFile(answer):
	extensionA = answer.split(".")
	extension = extensionA[len(extensionA)-1]
	#print(extension)
	extension = extension.rstrip("\n")
	programToUse = filePrograms[extension]
	os.system(programToUse + " " + answer)


if "/" in answer:
	openFile(answer)
else:
	answer = answer.rstrip("\n")
	Popen(answer)
