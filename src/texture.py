import os
import numpy as np
import librosa
import soundfile as sf
from matplotlib import pyplot as plt
from common.load_audio import load_audio_file, load_audio_dir
from common.grains import make_one_grain, repeat_grain

# noise salad
def noise_salad(audio_dir, passes=1, write_out=False, output_file_name=None):
    num_audio_files, buffer_objs = load_audio_dir(audio_dir)
    num_iterations = num_audio_files * passes

    salad = []

    for buffer in range(num_iterations):
        selected_file = np.random.randint(num_audio_files)
        audio_data = buffer_objs[selected_file]['data']
        sr = buffer_objs[selected_file]['sample_rate']

        grain_length = np.random.randint(sr * 0.1, sr * 1.5) if len(audio_data) > sr * 1.5 else np.random.randint(sr * 0.1, len(audio_data))

        grain = make_one_grain(grain_length, audio_data, sr)
        salad.extend(grain)

    if write_out:
        audio_output_path = os.path.join("generated", "salad", output_file_name)
        sf.write(audio_output_path, salad, sr, subtype='PCM_24')
        print("Saved noise salad!")

    return salad

noise_salad("white_noise", 1, True, "test_salad.wav")

# create function that extends existing texture (texture_1)

# create function that generates repetitive, minimalist, slowly evolving texture (a la movement 1 breathy sounds)