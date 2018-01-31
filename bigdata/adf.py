import pygame
import sys
import time
import subprocess


# import soundfile as sf
# import soundcard as sc

# default_speaker = sc.default_speaker()
# samples, samplerate = sf.read('C:\\Users\\lee\\Downloads\\Red Velvet.mp3')
#
# default_speaker.play(samples, samplerate=samplerate)

import pygame

# pygame.init()

# pygame.mixer.music.load("C:\\Users\\lee\\Downloads\\beep-05.wav")

# pygame.mixer.music.play()

# pygame.mixer.init()
# pygame.mixer.music.load("C:\\Users\\lee\\Downloads\\beep-05.wav")
# pygame.mixer.music.play()

# from playsound import playsound
#
# playsound('C:\\Users\\lee\\Downloads\\Red Velvet.mp3')
# playsound('C:\\Users\\lee\\Downloads\\beep-05.wav')

# import vlc
# p = vlc.MediaPlayer("C:\\Users\\lee\\Downloads\\Red Velvet 피카부.mp3")
# p.play()



# import webbrowser
# webbrowser.open("C:\\Users\\lee\\Downloads\\Red Velvet 피카부.mp3")

# import os
#
# os.system('C:\\Users\\lee\\Downloads\\Red Velvet 피카부.mp3')


import vlc

# p = vlc.MediaPlayer("C:\\Users\\lee\\Downloads\\21bt.net-NHDTA955.mp4")
# p.play()
# p.stop()
# while True:
#    pass

# import subprocess
#
# subprocess.Popen(r'vlc --rate 5 C:\\Users\\lee\\Downloads\\Red Velvet 피카부.mp3',shell = True)

# import os
# os.startfile('C:\\Users\\lee\\Downloads\\Red Velvet 피카부.mp3')

from subprocess import call
from gtts import gTTS
# import os
blabla = input('Type IN: ')
tts = gTTS(text=blabla, lang='ko')
tts.save("test.mp3")
# call(["vlc", "test.mp3"])

import pyglet
song = pyglet.media.load('test.mp3')
song.play()
# time.sleep(5)
pyglet.app.run()

