import sys
import getopt
import pyttsx3
from os import path
from pydub import AudioSegment
from gtts import gTTS

class TextToSpeech:
    engine: pyttsx3

    def __init__(self,voice, rate: int, volume: float):
        self.engine = pyttsx3.init()
        if voice:
            self.engine.setProperty('voice',voice)
        self.engine.setProperty('rate',rate)
        self.engine.setProperty('volume',volume)

    def list_available_voices(self):
        voices: list = [self.engine.getProperty('voices')]

        for i, voice in enumerate(voices[0]):
            print(f'({i + 1}) {voice.name} {voice.age}: {voice.languages[0]} ({voice.gender}) [ID: {voice.id}]')

    def text_to_speech(self, text: str, save: bool = False, file_name='output.mp3'):
        #self.engine.say(text)
        #print('I\'m speaking...')

        if save:
            # On linux make sure that 'espeak' and 'ffmpeg' are installed
            self.engine.save_to_file(text, file_name)

        self.engine.runAndWait()

