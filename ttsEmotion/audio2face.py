# speech to Audio2Face module utilizing the gRPC protocal from audio2face_streaming_utils

import io
from pydub import AudioSegment
from scipy.io.wavfile import read
import numpy as np
import time
from audio2face_streaming_utils import push_audio_track
from gtts import gTTS

class Audio2FaceService:
    def __init__(self, sample_rate=44100):
        """
        :param sample_rate: sample rate
        """
        #self.a2f_url = 'localhost:50051' 
        self.a2f_url = '127.0.0.1:50051'   # Set it to the port of your local host 
        self.sample_rate = 22050
        self.avatar_instance = '/World/audio2face/PlayerStreaming'   # Set it to the name of your Audio2Face Streaming Instance

    def get_tts_data(self,text):
        tts_result = io.BytesIO()
        tts = gTTS(text=text, lang='en', slow=False)
        tts.write_to_fp(tts_result)
        tts_result.seek(0)
        return tts_result.read()

    def tts_to_wav(self,tts_byte, framerate=22050):
        seg=AudioSegment.from_mp3(io.BytesIO(tts_byte))
        seg=seg.set_frame_rate(framerate)
        seg=seg.set_channels(1)
        wavIO=io.BytesIO()
        seg.export(wavIO, format="wav")
        rate, wav = read(io.BytesIO(wavIO.getvalue()))
        return wav

    def wav_to_numpy_float32(self, wav_byte) -> float:
        """
        :param wav_byte: wav byte
        :return: float32
        """
        return wav_byte.astype(np.float32, order='C') / 32768.0

    def get_tts_numpy_audio(self, text) -> float:
        """
        :param audio: audio from tts_to_wav
        :return: float32 of the audio
        """
        mp3_byte = self.get_tts_data(text)
        wav_byte = self.tts_to_wav(mp3_byte)
        return self.wav_to_numpy_float32(wav_byte)

    def make_avatar_speaks(self, text) -> None:
        """
        :param audio: tts audio
        :return: None
        """
        sleep_time = 1
        
        audio_data = self.get_tts_numpy_audio(text)
        print(f"Sleeping for {sleep_time} seconds")
        time.sleep(sleep_time)
        push_audio_track(self.a2f_url, audio_data, self.sample_rate, self.avatar_instance)
