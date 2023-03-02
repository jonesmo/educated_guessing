import os
import numpy as np
from scipy.io import wavfile
from common.load_audio import load_audio_file, load_audio_dir
from common.grains import make_one_grain, repeat_grain

def noise_salad(audio_dir, length=10, max_length=1, write_out=False, output_file_name=None):
    num_audio_files, buffer_objs = load_audio_dir(audio_dir)
    sr = buffer_objs[0]['sample_rate']

    salad_left = []
    salad_right = []

    while len(salad_left) < length * sr:
        selected_file = np.random.randint(num_audio_files)
        audio_data = buffer_objs[selected_file]['data']
        sr = buffer_objs[selected_file]['sample_rate']

        grain_length = np.random.randint(sr * 0.1, sr * 1.5 * max_length) if len(audio_data) > sr * 1.5 * max_length else np.random.randint(sr * 0.1, len(audio_data))

        grain1 = make_one_grain(grain_length, audio_data, sr)
        grain2 = make_one_grain(grain_length, audio_data, sr)
        salad_left.extend(grain1)
        salad_right.extend(grain2)
    
    salad = [salad_left, salad_right]
    salad_np = np.vstack((salad_left, salad_right))
    salad_stereo = salad_np.transpose()

    if write_out:
        audio_output_path = os.path.join("generated", "salad", output_file_name)
        wavfile.write(audio_output_path, sr, salad_stereo)
        print("Saved noise salad!")

    return salad