import os
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

def generate_filename(base_path, base_name):
    """
    Generate a new filename by checking existing files in the directory.

    Parameters:
    - base_path (str): The directory where the files are saved.
    - base_name (str): The base name for the file (without extension).

    Returns:
    - str: A new filename that doesn't clash with existing files.
    """
    index = 0
    new_name = os.path.join(base_path, f"{base_name}.wav")

    while os.path.exists(new_name):
        index += 1
        new_name = os.path.join(base_path, f"{base_name}({index}).wav")

    return new_name

# Recording parameters
DURATION = 20  # seconds
RATE = 96000  # 96kHz
CHANNELS = 2  # Stereo
DEVICE_INDEX = 22  # Using the Stereo Mix device

# Record audio
print("Recording...")
audio_data = sd.rec(int(DURATION * RATE), samplerate=RATE, channels=CHANNELS, dtype='float32', device=DEVICE_INDEX)
sd.wait()
print("Recording complete")

# Save audio to a WAV file
output_path = "D:/samples"
base_filename = "sample"
filename = generate_filename(output_path, base_filename)
print(f"trying to save as {filename}")
write(filename, RATE, audio_data)
print("saved")
