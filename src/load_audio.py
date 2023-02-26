import os
import librosa

# load single audio file
def load_audio_file(texture_folder, file_name):
    path_to_audio = os.path.join("..", texture_folder, file_name)

    audio_file, sr = librosa.load(path_to_audio)
    filelength = len(audio_file)
    return audio_file, sr, filelength

# load all audio files in directory