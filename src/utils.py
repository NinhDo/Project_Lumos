# for bash commands
import subprocess

# Wakes up the mangostation by sending a magic packet
def wake_up():
	subprocess.call(["wakeonlan", "-f /home/pi/mangostation"]);

#Goes through the query
def query_handler(query):
    if "on" in query and "computer" in query:
        wake_up
    else:
        print query
