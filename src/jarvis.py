# Recognize speach
import socket

import pyttsx
import speech_recognition

# Use sapi5 for windows or espeak for linux (espeak should work on windows as well)
speech_engine = pyttsx.init('espeak')  # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
speech_engine.setProperty('rate', 150)
recognizer = speech_recognition.Recognizer()

# stuff for the esp8266
UDP_IP = "192.168.0.47"
UDP_PORT = 2390

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def light(message):
	if "on" in message:
		return sock.sendto("on".encode(), (UDP_IP, UDP_PORT))
	if "off" in message:
		return sock.sendto("off".encode(), (UDP_IP, UDP_PORT))
	if "test" in message:
		return sock.sendto("test".encode(), (UDP_IP, UDP_PORT))


# Function to make the computer speak
def speak(text):
	speech_engine.say(text)
	speech_engine.runAndWait()
	print(text)


# Function to listen to the user.
def listen():
	with speech_recognition.Microphone() as source:
		recognizer.adjust_for_ambient_noise(source)
		print("Listening...")
		audio = recognizer.listen(source)
		print("Done listening")
	try:
		# use sphinx (offline) google or wit (online) to translate speech to text
		# resp = recognizer.recognize_sphinx(audio)
		# resp = recognizer.recognize_google(audio)
		resp = recognizer.recognize_wit(audio, "7L3D6I3ERDD7TESMBD54RMA4VWNLSSWI")
		light(resp)
		print(resp)
		return resp
	except speech_recognition.UnknownValueError:
		print("Could not understand audio")
	except speech_recognition.RequestError as e:
		print("Recog Error; {0}".format(e))

	return ""


while (True):
	speak("Say something!")
	speak("I heard you say " + listen())
