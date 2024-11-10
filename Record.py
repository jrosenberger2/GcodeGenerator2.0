import pyaudio
import wave
#import streamlit as st
CHUNK = 1024
FORMAT = pyaudio.paInt32
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
p = pyaudio.PyAudio()

with wave.open('output.wave', 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)

    stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True)

    #print("Recording...")
    for i in range(0,RATE // CHUNK * RECORD_SECONDS):
        wf.writeframes(stream.read(CHUNK))
    #print("Done!")

    stream.close()
    p.terminate