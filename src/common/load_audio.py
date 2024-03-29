import os
import librosa

# load single audio file
def load_audio_file(texture_folder, file_name):
    path_to_audio = os.path.join("..", texture_folder, file_name)

    audio_data, sr = librosa.load(path_to_audio, sr=None)
    filelength = len(audio_data)
    return audio_data, sr, filelength


# load all audio files in directory
def load_audio_dir(texture_folder):
    path_to_audio = os.path.join("..", texture_folder)

    files_in_folder = [
        file
        for file in os.listdir(path_to_audio)
        if (os.path.isfile(os.path.join(path_to_audio, file)) and file.endswith(".wav"))
    ]
    num_audio_files = len(files_in_folder)

    i = 0
    audio_buffers = {}
    for file_name in files_in_folder:
        audio_data, sr, filelength = load_audio_file(texture_folder, file_name)

        audio_buffers[i] = {
            "sample_rate": sr,
            "file_length": filelength,
            "data": audio_data,
        }
        i += 1

    return num_audio_files, audio_buffers
