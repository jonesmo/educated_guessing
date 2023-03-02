import os
import numpy as np
import librosa
import soundfile as sf
from matplotlib import pyplot as plt
from common.load_audio import load_audio_file, load_audio_dir
from common.grains import make_one_grain, repeat_grain
from salad import noise_salad

# ------ load audio ------
# audio_file_num, buffers = load_audio_dir("texture_2")
# print(audio_file_num)
# print(buffers)

# ------ grains ------
# audio_data, sr, filelength = load_audio_file("texture_2", "i_1_full_interpolation.wav")
# single_grain = make_one_grain(15000, audio_data, sr, True, "test_grain.wav")
# repeat_grain(single_grain, 10, True, sr, "ten_in_a_row.wav")

# ------ noise salad ------
noise_salad("white_noise", 20, 0.5, True, "test_salad.wav")

# create function that extends existing texture (texture_1)

# create function that generates repetitive, minimalist, slowly evolving texture (a la movement 1 breathy sounds)