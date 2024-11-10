#Install.py uses cmd to install package dependencies needed to run GeneratorV2.1.py
import subprocess

subprocess.run(['pip', 'install', 'streamlit'])
subprocess.run(['pip', 'install', 'pyaudio'])
subprocess.run(['pip', 'install', 'trimesh'])
subprocess.run(['pip', 'install', 'openai-whisper'])
subprocess.run(['pip', 'install', 'ffmpeg'])