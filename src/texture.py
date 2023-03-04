import os
import numpy as np
import librosa
import soundfile as sf
from scipy.io import wavfile
from matplotlib import pyplot as plt
from common.load_audio import load_audio_file, load_audio_dir
from common.grains import make_one_grain, repeat_grain
from salad import noise_salad, accordion_salad
from extend import extend
from pulse import grain_hold, short_pulse

# ------ load audio ------
# audio_file_num, buffers = load_audio_dir("texture_2")
# print(audio_file_num)
# print(buffers)

# ------ grains ------
# audio_data, sr, filelength = load_audio_file("texture_2", "i_1_full_interpolation.wav")
# single_grain = make_one_grain(15000, audio_data, sr, True, "test_grain.wav")
# repeat_grain(single_grain, 10, True, sr, "ten_in_a_row.wav")

# ------ noise salad ------
# noise_salad("percussion_salad", 20, 1, True, "test_salad.wav")
# accordion_salad("accordion_salad", 20, 4, True, "test_accordion_salad.wav")

# create function that extends existing texture (texture_1)
# extend("texture_3", "i_2_full_interpolation_trimmed_2.wav", 10, True, "test_extend.wav")

# create short ha-ha-ha texture
# grain_hold("texture_4", "p_7_diffusion.wav", 120, 10, True, "test_grain_hold.wav")
# short_pulse("texture_3", "p_8_diffusion.wav", 212, 10, True, "test_pulse.wav")
# short_pulse("white_noise", "p_19500_1.wav", 212, 10, True, "test_pulse.wav")
short_pulse("nn_percussion", "p_199999_1sec_1.wav", 212, 10, True, "test_pulse.wav")
# need to zero-pad any pulse grains that are shorter than the tempo calls for to make it the correct speed

# create gradual fade between one texture and another

# create function that generates repetitive, minimalist, slowly evolving texture

# create gradual fade between two pulses
