# The hotword detector
import snowboydecoder

# What to do when you hear a word
def detected_callback():
    print "hotword detected"


detector = snowboydecoder.HotwordDetector("Hey__Jarvis.pmdl", sensitivity=0.5, audio_gain=1)
detector.start(detected_callback)
