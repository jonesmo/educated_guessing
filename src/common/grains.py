import os
import numpy as np
import soundfile as sf
import librosa
from common.load_audio import load_audio_file

# grab one grain
def make_one_grain(grain_length, audio_data, sample_rate, write_out=False, output_file_name=None):
    filelength = len(audio_data)
    starting_sample = np.random.randint(0, filelength - grain_length)
    ending_sample = starting_sample + grain_length
    grain = audio_data[starting_sample:ending_sample]

    if write_out:
        audio_output_path = os.path.join("generated", "grains", output_file_name)
        sf.write(audio_output_path, grain, sample_rate, subtype='PCM_24')
        print("Saved one grain to /grains!")
    return grain

# grab one grain and repitch it
def make_one_repitched_grain(grain_length, audio_data, sample_rate, write_out=False, output_file_name=None):
    filelength = len(audio_data)
    starting_sample = np.random.randint(0, filelength - grain_length)
    ending_sample = starting_sample + grain_length
    grain = audio_data[starting_sample:ending_sample]
    
    # repitch the grain
    grain_np = np.array(grain)
    steps_to_shift_pitch = np.random.randint(-36, 10)
    repitched_grain_np = librosa.effects.pitch_shift(grain_np, sr=sample_rate, n_steps=steps_to_shift_pitch)
    repitched_grain = repitched_grain_np.tolist()

    if write_out:
        audio_output_path = os.path.join("generated", "grains", output_file_name)
        sf.write(audio_output_path, repitched_grain, sample_rate, subtype='PCM_24')
        print("Saved one repitched grain to /grains!")
    return grain

# repeat grain multiple times in a row
def repeat_grain(grain, num_repeats, write_out, sample_rate, output_file_name):
    repeated_grains = []

    for i in range(num_repeats):
        repeated_grains = [*repeated_grains, *grain]

    audio_output_path = os.path.join("generated", "grains", output_file_name)
    
    if write_out:
        sf.write(audio_output_path, repeated_grains, sample_rate, subtype='PCM_24')
        print("Saved repeated grains to /grains!")
    return repeated_grains