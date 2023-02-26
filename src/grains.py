import os
import numpy as np
import soundfile as sf
from load_audio import load_audio_file

# grab one grain
def make_one_grain(grain_length, output_file_name, audio_file, filelength, sample_rate, write_out):
    starting_sample = np.random.randint(0, filelength - grain_length)
    ending_sample = starting_sample + grain_length
    grain = audio_file[starting_sample:ending_sample]

    audio_output_path = os.path.join("..", "generated", "grains", output_file_name)

    if write_out:
        sf.write(audio_output_path, grain, sample_rate, subtype='PCM_24')
        print("Saved one grain to /grains!")
    return grain

audio_file, sr, filelength = load_audio_file("texture_2", "i_1_full_interpolation.wav")
single_grain = make_one_grain(15000, "test_grain.wav", audio_file, filelength, sr, True)