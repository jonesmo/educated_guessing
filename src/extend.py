import os
import numpy as np
import soundfile as sf
from common.load_audio import load_audio_file


def extend(audio_dir, filename, num_chunks, write_out=False, output_file_name=None):
    audio_data, sr, filelength = load_audio_file(audio_dir, filename)

    original_audio_data = audio_data.tolist()
    new_audio = original_audio_data

    for chunk in range(num_chunks):
        chunk_length = (
            int(filelength * 0.5)
            if filelength < sr * 3
            else np.random.randint(sr * 1, sr * 3)
        )
        starting_sample = np.random.randint(0, filelength - chunk_length)
        ending_sample = starting_sample + chunk_length

        # find zero-crossing to start and end chunk
        for i in range(4000):
            if original_audio_data[starting_sample + i] == 0.0:
                starting_sample = starting_sample + i
        for j in range(4000):
            if original_audio_data[ending_sample - i] == 0.0:
                ending_sample = ending_sample - i
        interpolation_chunk = original_audio_data[starting_sample:ending_sample]

        wedge_location = np.random.randint(len(new_audio) * 0.8, len(new_audio))
        part_one = new_audio[0:wedge_location]
        part_two = interpolation_chunk
        part_three = new_audio[wedge_location : len(new_audio)]

        # make stereo
        new_audio = part_one + part_two + part_three

    if write_out:
        audio_output_path = os.path.join("generated", "extended", output_file_name)
        sf.write(audio_output_path, new_audio, sr, subtype="PCM_24")
        print("Saved extended audio file to /extended!")

    return new_audio, sr


def extend_from_data(
    audio_data, sr, num_chunks, write_out=False, output_file_name=None
):
    filelength = len(audio_data)

    original_audio_data = audio_data.tolist()
    new_audio = original_audio_data

    for chunk in range(num_chunks):
        chunk_length = (
            int(filelength * 0.5)
            if filelength < sr * 3
            else np.random.randint(sr * 1, sr * 3)
        )
        starting_sample = np.random.randint(0, filelength - chunk_length)
        ending_sample = starting_sample + chunk_length

        # find zero-crossing to start and end chunk
        for i in range(4000):
            if original_audio_data[starting_sample + i] == 0.0:
                starting_sample = starting_sample + i
        for j in range(4000):
            if original_audio_data[ending_sample - i] == 0.0:
                ending_sample = ending_sample - i
        interpolation_chunk = original_audio_data[starting_sample:ending_sample]

        wedge_location = np.random.randint(len(new_audio) * 0.8, len(new_audio))
        part_one = new_audio[0:wedge_location]
        part_two = interpolation_chunk
        part_three = new_audio[wedge_location : len(new_audio)]

        # make stereo
        new_audio = part_one + part_two + part_three

    if write_out:
        audio_output_path = os.path.join("generated", "extended", output_file_name)
        sf.write(audio_output_path, new_audio, sr, subtype="PCM_24")
        print("Saved extended audio file to /extended!")

    return new_audio, sr
