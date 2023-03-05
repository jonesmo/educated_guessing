import os
import numpy as np
import soundfile as sf
from common.load_audio import load_audio_file
from common.grains import make_one_grain, make_one_repitched_grain, repeat_grain


def grain_hold(
    audio_dir, filename, tempo, length, write_out=False, output_file_name=None
):
    audio_data, sr, filelength = load_audio_file(audio_dir, filename)

    original_audio_data = audio_data.tolist()
    pulse_audio = []

    grain_length = (
        round(1 / tempo * sr) if filelength > round(1 / tempo * sr) else filelength
    )
    print(grain_length)
    grain_to_repeat = make_one_grain(grain_length, original_audio_data, sr)

    while len(pulse_audio) < length * sr:
        pulse_audio.extend(grain_to_repeat)

    if write_out:
        audio_output_path = os.path.join("generated", "held_grain", output_file_name)
        sf.write(audio_output_path, pulse_audio, sr, subtype="PCM_24")
        print("Saved held grain audio file to /pulse!")

    return pulse_audio, sr


def short_pulse(
    audio_dir, filename, tempo, length, write_out=False, output_file_name=None
):
    audio_data, sr, filelength = load_audio_file(audio_dir, filename)

    original_audio_data = audio_data.tolist()
    pulse_audio = []

    grain_length = (
        round(1 / tempo * sr * 60) if filelength > round(1 / tempo * sr) else filelength
    )
    grain_to_repeat = make_one_grain(grain_length, original_audio_data, sr)

    while len(pulse_audio) < length * sr:
        pulse_audio.extend(grain_to_repeat)

    if write_out:
        audio_output_path = os.path.join("generated", "pulse", output_file_name)
        sf.write(audio_output_path, pulse_audio, sr, subtype="PCM_24")
        print("Saved pulse audio file to /pulse!")

    return pulse_audio, sr
