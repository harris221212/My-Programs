#!/usr/bin/env python3

from rofi import Rofi
import pyperclip3

launcher = "Super = Rofi Launcher"
alacritty = "Super+Return = Terminal"
firefox = "Super+W = Firefox"
youtube = "Super+O = YouTube Channel"
btop = "Super+B = btop"
htop = "Super+H = htop"
calculator = "Super+C = Calculator"
mousepad = "Super+N = Notepad"
bookmarksA = "Super+Shift+V = Add New Bookmark"
bookmarksB = "Super+V = Bookmarks"
findFiles = "Super+F = File Search"
dgg = "Super+L = dgg Chat"
thunar = "Super+E = File Browser"
screenshooter = "Super+` = Screenshot"
keyboardHelp = "Super+K = Show Keyboard Shortcuts"

settings = "Super+S = Settings"
wmSettings = "Super+M = Window Manager Settings"
wmTweaksSettings = "Super+T = Window Manager Tweaks"



logout = "Ctrl+Alt+Del = Logout"

desktop = "Super+D = Show Desktop"
altTab = "Alt+Tab = Cycle Windows"
altBacktick = "Alt+` = Cycle Windows of Current Application"
closeWindow = "Super+Shift+Q = Close Window/Logout"
maximise = "Super+Shift = Maximise"
resize = "Super+Shift+R = Resize Window"
previousWorkspace = "Super+, = Previous Workspace"
nextWorkspace = "Super+. = Next Workspace"
right = "Super+Right = Put Window on Right"
left = "Super+Left = Put Window on Left"
top = "Super+Top = Put Window on Top"
bottom = "Super+Down = Put Window on Bottom"
topRight = "Super+End = Put Window on Top Right"
bottomRight = "Super+PgDn= Put Window on Bottom Right"
topLeft = "Super+PgUp = Put Window on Top Left"
bottomLeft = "Super+Home = Put Window on Bottom Left"








shortcuts = [launcher, alacritty, firefox, youtube, btop, htop, calculator, mousepad, bookmarksA, bookmarksB, findFiles, dgg, thunar, screenshooter, keyboardHelp, settings, wmSettings, wmTweaksSettings, logout, desktop, altTab, altBacktick, closeWindow, maximise, resize, previousWorkspace, nextWorkspace, right, left, top, bottom, topRight, bottomRight, topLeft, bottomLeft]


r = Rofi()
index, key = r.select("All Keyboard Shortcuts", shortcuts)
