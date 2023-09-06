import time
import pygame
import soundfile as sf
from plyer import notification


# Create a Function for Checking Length of Audio
def get_audio_length(filename):
    with sf.SoundFile(filename) as f:
        return len(f) / f.samplerate
