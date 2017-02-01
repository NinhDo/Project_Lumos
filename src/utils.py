# for bash commands
import subprocess

# Wakes up the mangostation by sending a magic packet
def wake_up():
	subprocess.call(["wakeonlan", "-f /home/pi/mangostation"]);
