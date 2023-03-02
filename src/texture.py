import os
import numpy as np
import librosa
import soundfile as sf
from matplotlib import pyplot as plt
from common.load_audio import load_audio_file, load_audio_dir
from common.grains import make_one_grain, repeat_grain
from salad import noise_salad

# noise salad
noise_salad("white_noise", 3, 0.5, True, "test_salad.wav")

# create function that extends existing texture (texture_1)

# create function that generates repetitive, minimalist, slowly evolving texture (a la movement 1 breathy sounds)