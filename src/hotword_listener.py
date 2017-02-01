# The hotword detector
import snowboydecoder
import signal
# import our utilities
import utils

# For termination
interrupted = False

# If we signal the program to stop
def signal_handler(signal, frame):
	global interrupted
	interrupted = True

# For termination
def interrupt_callback():
	global interrupted
	return interrupted

# What to do when you hear a word
def detected_callback():
	utils.wake_up()
	print "hotword detected"

# Set up the detector, so it looks after "Hey, Jarvis"
detector = snowboydecoder.HotwordDetector(
	"./Hey__Jarvis.pmdl",
	sensitivity=0.5,
	audio_gain=1
)

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

def start():
	# Start listening. Every sleep_time seconds, the function checks if the
	# hotword was detected and calls the callback function, and if we
	# interrupted the program so it can terminate properly
	detector.start(
		detected_callback,
		interrupt_check=interrupt_callback,
		sleep_time=0.03
	)
	detector.terminate()
