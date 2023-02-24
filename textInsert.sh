#!/bin/sh
windowid=$(xdotool getwindowfocus)
#sleep 0.5 && xdotool windowactivate --sync $windowid type 'text'
sleep 0.5 & xdotool keyup super+shift+e type "things mad init"
