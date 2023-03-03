import os
import numpy as np
from scipy.io import wavfile
import librosa
from common.load_audio import load_audio_file, load_audio_dir
from common.grains import make_one_grain, make_one_repitched_grain, repeat_grain


def noise_salad(
    audio_dir, length=10, max_length=1, write_out=False, output_file_name=None
):
    num_audio_files, buffer_objs = load_audio_dir(audio_dir)
    initial_sample_rate = buffer_objs[0]["sample_rate"]

    salad_left = []
    salad_right = []

    while len(salad_left) < length * initial_sample_rate:
        selected_file = np.random.randint(num_audio_files)
        audio_data = buffer_objs[selected_file]["data"]
        sr = buffer_objs[selected_file]["sample_rate"]
        minimum_grain_length = (
            sr * 0.1 if len(audio_data) > sr * 0.1 else len(audio_data) * 0.5
        )

        grain_length_left = (
            np.random.randint(minimum_grain_length, sr * 1.5 * max_length)
            if len(audio_data) > sr * 1.5 * max_length
            else np.random.randint(minimum_grain_length, len(audio_data))
        )
        grain_length_right = (
            np.random.randint(minimum_grain_length, sr * 1.5 * max_length)
            if len(audio_data) > sr * 1.5 * max_length
            else np.random.randint(minimum_grain_length, len(audio_data))
        )

        grain1 = make_one_grain(grain_length_left, audio_data, sr)
        grain2 = make_one_grain(grain_length_right, audio_data, sr)
        salad_left.extend(grain1)
        salad_right.extend(grain2)
    
    # make salad_left and salad_right the same length
    left_length = len(salad_left)
    right_length = len(salad_right)
    if left_length != right_length:
        difference = abs(left_length - right_length)
        elements_to_pad = [0] * difference
        if left_length > right_length:
            salad_right.extend(elements_to_pad)
        elif right_length > left_length:
            salad_left.extend(elements_to_pad)

    salad = [salad_left, salad_right]
    salad_np = np.vstack((salad_left, salad_right))
    salad_stereo = salad_np.transpose()

    if write_out:
        audio_output_path = os.path.join("generated", "salad", output_file_name)
        wavfile.write(audio_output_path, sr, salad_stereo)
        print("Saved noise salad!")

    return salad


def accordion_salad(
    audio_dir, length=10, max_length=1, write_out=False, output_file_name=None
):
    num_audio_files, buffer_objs = load_audio_dir(audio_dir)
    initial_sample_rate = buffer_objs[0]["sample_rate"]

    salad_left = []
    salad_right = []

    while len(salad_left) < length * initial_sample_rate:
        selected_file = np.random.randint(num_audio_files)
        audio_data = buffer_objs[selected_file]["data"]
        sr = buffer_objs[selected_file]["sample_rate"]
        minimum_grain_length = (
            sr * 0.5 if len(audio_data) > sr * 0.5 else len(audio_data) * 0.5
        )

        grain_length_left = (
            np.random.randint(minimum_grain_length, sr * 1.5 * max_length)
            if len(audio_data) > sr * 1.5 * max_length
            else np.random.randint(minimum_grain_length, len(audio_data))
        )
        grain_length_right = (
            np.random.randint(minimum_grain_length, sr * 1.5 * max_length)
            if len(audio_data) > sr * 1.5 * max_length
            else np.random.randint(minimum_grain_length, len(audio_data))
        )

        grain1 = make_one_repitched_grain(grain_length_left, audio_data, sr)
        grain2 = make_one_repitched_grain(grain_length_right, audio_data, sr)

        # extract harmonic components of some of the grains
        if np.random.choice([0, 1], 1, p=[0.7, 0.3]) == 0:
            grain1_np = np.array(grain1)
            grain2_np = np.array(grain2)
            just_harmonic1 = librosa.effects.harmonic(grain1_np)
            just_harmonic2 = librosa.effects.harmonic(grain2_np)
            grain1_harmonic = just_harmonic1.tolist()
            grain2_harmonic = just_harmonic2.tolist()

            grain1 = grain1_harmonic
            grain2 = grain2_harmonic

        # reverse some of the grains
        if np.random.choice([0, 1], 1, p=[0.4, 0.6]) == 0:
            grain1 = grain1[::-1]
            grain2 = grain2[::-1]
    
        
        salad_left.extend(grain1)
        salad_right.extend(grain2)


    # make salad_left and salad_right the same length
    left_length = len(salad_left)
    right_length = len(salad_right)
    if left_length != right_length:
        difference = abs(left_length - right_length)
        elements_to_pad = [0] * difference
        if left_length > right_length:
            salad_right.extend(elements_to_pad)
        elif right_length > left_length:
            salad_left.extend(elements_to_pad)

    salad = [salad_left, salad_right]

    # turn salad into a stereo file
    salad_np = np.vstack((salad_left, salad_right))
    salad_stereo = salad_np.transpose()

    if write_out:
        audio_output_path = os.path.join("generated", "salad", output_file_name)
        wavfile.write(audio_output_path, sr, salad_stereo)
        print("Saved accordion salad!")

    return salad
