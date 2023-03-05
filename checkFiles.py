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


programs = ["code", "discord", "alacritty", "dmenu", "electron", "firefox", "gimp", "gnumeric", "google-chrome-stable", "gparted", "gthumb", "imagemagick", "kdenlive", "mpv", "opera", "pavucontrol", "pulseaudio", "pulseaudio-alssa", "qbittorrent", "ristretto", "rofi", "steam", "thunar", "xfce4-appfinder", "xfce4-power-manager", "xfce4-pulseaudio-plugin", "xfce4-screenshooter", "xfce4-settings-manager", "xfce4-keyboard-settings", "xfce4-taskmanager", "xfce4-terminal", "xfwm4-settings", "xfwm4-tweaks-settings", "zathura"]

output1 = subprocess.run(["find", "/home/ethan"], stdout=subprocess.PIPE).stdout.decode('utf-8')
filesArray = output1.split("\n")
filesArray.pop(0)
filesArray.pop(len(filesArray)-1)
#print(filesArray)
finalArray = []
extensionsA = []
for x in filesArray:
	aa = x.split(".")
	if len(aa) > 1:
		extension = aa[len(aa)-1]
		if extension in keys:
			if not ".local/lib/python3.10/" in x and not ".local/share/icons/hicolor/" in x and not ".local/share/Steam" in x and not ".ghcup/ghc" in x and not ".vscode-oss/" in x and not ".cargo/" in x and not ".wine/drive_c" in x and not ".local/share/lutris" in x and "ethan/.cache/" not in x:
				finalArray.append(x)


fullArray = programs + finalArray

indexA = 0
for x in fullArray:
	toReplace = x.replace("/home/ethan/", "~/")
	fullArray[indexA] = toReplace
	indexA = indexA + 1

with open('/home/ethan/Programs/log/files.txt', 'w') as f:
    for line in fullArray:
        f.write(f"{line}\n")
