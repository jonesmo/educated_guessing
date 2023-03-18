import os
import math
import soundfile as sf
import numpy as np
from extend import extend_from_data


def total_overlay(texture1, texture2, sr, write_out=False, output_file_name=None):
    # ensure all textures have same length and zero-pad
    texture1_length = len(texture1)
    texture2_length = len(texture2)
    if texture1_length != texture2_length:
        difference = abs(texture1_length - texture2_length)
        elements_to_pad = [0] * difference
        if texture1_length > texture2_length:
            texture2.extend(elements_to_pad)
        elif texture2_length > texture1_length:
            texture1.extend(elements_to_pad)

    new_audio = [sum(x) / 2 for x in zip(texture1, texture2)]

    if write_out:
        audio_output_path = os.path.join("generated", "overlays", output_file_name)
        sf.write(audio_output_path, new_audio, sr, subtype="PCM_24")
        print("Saved overlay audio file to /overlays!")

    return new_audio, sr


def gradual_linear_fade(
    texture1,
    texture2,
    sr,
    chunks_to_extend,
    how_far_in_to_fade,
    write_out=False,
    output_file_name=None,
):
    extended_texture1, sr_unused1 = extend_from_data(texture1, sr, chunks_to_extend)
    extended_texture2, sr_unused2 = extend_from_data(texture2, sr, chunks_to_extend)

    fade_start_index = int(len(extended_texture1) * how_far_in_to_fade)
    length_of_overlap = len(extended_texture1) - fade_start_index
    overlap_region_of_texture1 = extended_texture1[-length_of_overlap:]
    overlap_region_of_texture2 = extended_texture2[0:length_of_overlap]

    new_audio = extended_texture1[0:fade_start_index]

    for j in range(length_of_overlap):
        volume_increment = 1 / length_of_overlap
        texture1_at_volume = overlap_region_of_texture1[j] * (1 - j * volume_increment)
        texture2_at_volume = overlap_region_of_texture2[j] * (j * volume_increment)
        audio_sample = texture1_at_volume + texture2_at_volume
        new_audio.extend([audio_sample])

    new_audio.extend(extended_texture2[length_of_overlap:])

    if write_out:
        audio_output_path = os.path.join("generated", "fades", output_file_name)
        sf.write(audio_output_path, new_audio, sr, subtype="PCM_24")
        print("Saved fade audio file to /fades!")

    return new_audio, sr


def gradual_log_fade(
    texture1,
    texture2,
    sr,
    chunks_to_extend,
    how_far_in_to_fade,
    write_out=False,
    output_file_name=None,
):
    extended_texture1, sr_unused1 = extend_from_data(texture1, sr, chunks_to_extend)
    extended_texture2, sr_unused2 = extend_from_data(texture2, sr, chunks_to_extend)

    fade_start_index = int(len(extended_texture1) * how_far_in_to_fade)
    length_to_end = len(extended_texture1) - fade_start_index
    length_of_overlap = (
        length_to_end
        if len(extended_texture2) > length_to_end
        else len(extended_texture2)
    )
    overlap_region_of_texture1 = extended_texture1[-length_of_overlap:]
    overlap_region_of_texture2 = (
        extended_texture2[0:length_of_overlap]
        if len(extended_texture2) > length_of_overlap
        else extended_texture2
    )

    new_audio = extended_texture1[0:fade_start_index]

    for j in range(length_of_overlap):
        volume_increment = 1 / length_of_overlap
        texture1_at_volume = overlap_region_of_texture1[j] * (
            math.e ** (-j * volume_increment)
        )
        texture2_at_volume = overlap_region_of_texture2[j] * (j * volume_increment)
        audio_sample = texture1_at_volume + texture2_at_volume
        new_audio.extend([audio_sample])

    new_audio.extend(extended_texture2[length_of_overlap:])

    if write_out:
        audio_output_path = os.path.join("generated", "fades", output_file_name)
        sf.write(audio_output_path, new_audio, sr, subtype="PCM_24")
        print("Saved fade audio file to /fades!")

    return new_audio, sr


def gradual_log_fade_without_extend(
    texture1,
    texture2,
    sr,
    how_far_in_to_fade,
    write_out=False,
    output_file_name=None,
):
    if isinstance(texture1, np.ndarray):
        texture1_data = texture1.tolist()
    else:
        texture1_data = texture1

    if isinstance(texture2, np.ndarray):
        texture2_data = texture2.tolist()
    else:
        texture2_data = texture2

    fade_start_index = int(len(texture1_data) * how_far_in_to_fade)
    length_to_end = len(texture1_data) - fade_start_index
    length_of_overlap = (
        length_to_end if len(texture2_data) > length_to_end else len(texture2_data)
    )
    overlap_region_of_texture1 = texture1_data[-length_of_overlap:]
    overlap_region_of_texture2 = (
        texture2_data[0:length_of_overlap]
        if len(texture2_data) > length_of_overlap
        else texture2_data
    )

    new_audio = texture1_data[0:fade_start_index]

    for j in range(length_of_overlap):
        volume_increment = 1 / length_of_overlap
        texture1_at_volume = overlap_region_of_texture1[j] * (
            math.e ** (-j * volume_increment)
        )
        texture2_at_volume = overlap_region_of_texture2[j] * (j * volume_increment)
        audio_sample = texture1_at_volume + texture2_at_volume
        new_audio.extend([audio_sample])

    new_audio.extend(texture2_data[length_of_overlap:])

    if write_out:
        audio_output_path = os.path.join("generated", "fades", output_file_name)
        sf.write(audio_output_path, new_audio, sr, subtype="PCM_24")
        print("Saved fade audio file to /fades!")

    return new_audio, sr
