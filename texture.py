import os
import numpy as np
import librosa
import soundfile as sf

texture_file = "texture_2"
audio_file_name = "i_1_full_interpolation.wav"
path_to_audio = os.path.join("..", texture_file, audio_file_name)
audio_output_path = os.path(".")

audio_file, sr = librosa.load(path_to_audio)
filelength = len(audio_file)

# grab one grain
grain_length = 50
starting_sample = np.random.randint(0, filelength - grain_length)
ending_sample = starting_sample + grain_length
grain = audio_file[starting_sample:ending_sample]

sf.write(audio_output_path, grain, sr, subtype='PCM_24')

# create function that extends existing texture (texture_1)

# create function that generates repetitive, minimalist, slowly evolving texture (a la movement 1 breathy sounds)

# create function that generates accordion or percussion or white noise salad