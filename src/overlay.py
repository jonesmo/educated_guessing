import os
import soundfile as sf


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
