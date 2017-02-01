# The hotword detector
import snowboydecoder
import signal
import time
# import our utilities
import utils
# import our google speech api listner
import google_speech_api_listener as google_listener

# For termination
interrupted = False

# Set up the detector, so it looks after "Hey, Jarvis"
detector = snowboydecoder.HotwordDetector(
	"./Hey__Jarvis.pmdl",
	sensitivity=0.5,
	audio_gain=1
)

# If we signal the program to stop
def signal_handler(signal, frame):
	global interrupted
	interrupted = True
	terminate()

# For termination
def interrupt_callback():
	global interrupted
	return interrupted

# What to do when you hear a word
def detected_callback():
	print "hotword detected"
	# Stop listening to free the Microphone
	global interrupted
	interrupted = True
	utils.query_handler(google_listener.start())
	interrupted = False


# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

def start():
	# Start listening. Every sleep_time seconds, the function checks if the
	# hotword was detected and calls the callback function, and if we
	# interrupted the program so it can terminate properly
	print "Hello there!"
	detector.start(
		detected_callback,
		interrupt_check=interrupt_callback,
		sleep_time=0.03
	)

	print "Goodbye."

# Detector, kill thyself
def terminate():
	detector.terminate()
