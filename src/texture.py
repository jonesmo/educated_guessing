import os
import numpy as np
import librosa
import soundfile as sf
from scipy.io import wavfile
from matplotlib import pyplot as plt
from common.load_audio import load_audio_file, load_audio_dir
from common.grains import make_one_grain, repeat_grain
from salad import noise_salad, accordion_salad
from extend import extend, extend_from_data
from pulse import grain_hold, short_pulse
from overlay import total_overlay, gradual_linear_fade, gradual_log_fade

# ------ load audio ------
# audio_file_num, buffers = load_audio_dir("texture_2")
# print(audio_file_num)
# print(buffers)

# ------ grains ------
# audio_data, sr, filelength = load_audio_file("texture_2", "i_1_full_interpolation.wav")
# single_grain = make_one_grain(15000, audio_data, sr, True, "test_grain.wav")
# single_grain = make_one_grain(15000, audio_data, sr)
# repeat_grain(single_grain, 10, True, sr, "ten_in_a_row.wav")

# ------ noise salad ------
# noise_salad("percussion_salad", 20, 1, True, "test_salad.wav")
# accordion_salad("accordion_salad", 20, 4, True, "test_accordion_salad.wav")

# ------ extend ------
# extend("texture_3", "i_2_full_interpolation_trimmed_2.wav", 10, True, "test_extend.wav")
# extend("texture_6", "i_4_church_bells_trimmed.wav", 10, True, "test_extend.wav")

# ------ pulse -------
# grain_hold("texture_4", "p_7_diffusion.wav", 120, 10, True, "test_grain_hold.wav")
# short_pulse("texture_3", "p_8_diffusion.wav", 212, 10, True, "test_pulse.wav")
# short_pulse("white_noise", "p_19500_1.wav", 212, 10, True, "test_pulse.wav")
# short_pulse("nn_percussion", "p_199999_1sec_1.wav", 212, 10, True, "test_pulse.wav")

# ^ need to zero-pad any pulse grains that are shorter than the tempo calls for to make it the correct speed
# OR need to detect length and eighth-note any that are too short

# ------ total overlay of two textures ------
# texture1, sr1 = extend("texture_3", "i_2_full_interpolation_trimmed_2.wav", 10)
# texture2, sr2 = short_pulse("nn_percussion", "p_199999_1sec_1.wav", 212, 10)
# texture2, sr2 = accordion_salad("accordion_salad", 7, 4)

texture1, sr1 = extend("texture_3", "i_2_full_interpolation_trimmed_2.wav", 20)
texture2, sr2 = extend("texture_4", "i_6_full_interpolation_trimmed_1.wav", 4)

if sr1 != sr2:
    raise Exception("Sample rates do not match.")

overlay = total_overlay(texture1, texture2, sr1, True, "test_overlay.wav")

# ------ gradual linear fade between two textures ------
# texture1, sr1 = short_pulse("nn_percussion", "p_199999_1sec_1.wav", 212, 10)
# # texture2, sr2 = noise_salad("percussion_salad", 20, 1)
# texture2, sr2 = repeat_grain(single_grain, 10, sr)

# if sr1 != sr2:
#     raise Exception("Sample rates do not match.")

# fade = gradual_linear_fade(texture1, texture2, sr1, 10, 0.15, True, "test_fade.wav")

# ------ gradual logarithmic fade between two textures ------
# texture1, sr1 = short_pulse("nn_percussion", "p_199999_1sec_1.wav", 212, 10)
# texture2, sr2 = noise_salad("percussion_salad", 20, 1)
# # texture2, sr2 = repeat_grain(single_grain, 10, sr)

# if sr1 != sr2:
#     raise Exception("Sample rates do not match.")

# fade = gradual_log_fade(texture1, texture2, sr1, 10, 0.15, True, "test_fade.wav")

# create function that generates repetitive, minimalist, slowly evolving texture
