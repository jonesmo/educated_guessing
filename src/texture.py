import os
import numpy as np
import librosa
import soundfile as sf
from matplotlib import pyplot as plt
from load_audio import load_audio_file
from grains import make_one_grain

audio_file, sr, filelength = load_audio_file("texture_2", "i_1_full_interpolation.wav")

single_grain = make_one_grain(15000, "test_grain.wav", audio_file, filelength, sr, True)

# white noise salad

# create function that extends existing texture (texture_1)

# create function that generates repetitive, minimalist, slowly evolving texture (a la movement 1 breathy sounds)