# A script to toggle monitor output. I use this with i3wm so that I can
# bind one keyboard shortcut turning off the laptop display and activating
# the external monitor, and then again to turn off the external monitor
# and activate the laptop display.

# Import os so we can use os.system to execute commands
# Import subprocess so we can capture the output of a command
# and assign it to a variable

import os
import subprocess

# Check to see if the external monitor is connected

queryMonitor = "xrandr | grep HDMI1"

# Turn on the external monitor and turn off laptop display

extMonOn = "xrandr --output HDMI1 --auto --output LVDS1 --off"

# Turn off the external monitor and turn on laptop display

extMonOff = "xrandr --output LVDS1 --auto --output HDMI1 --off"

# Instantiate an object of the output of the queryMonitor command and 
# assign the command output and errors to variables.

monitorState = subprocess.Popen(queryMonitor, stdout=subprocess.PIPE, shell=True)
monitorStateOutput, monitorStateError = monitorState.communicate()

# Test the output of the queryMonitor command to see if the 
# external monitor is connected. If so, activate it. If not, 
# activate the laptop display.

if monitorStateOutput.split()[1] == "connected":
    os.system(extMonOn)
else:
    os.system(extMonOff)
