import os
from pytube import YouTube
from moviepy.editor import *

def download_audio_from_youtube(url, output_format='wav'):
    # Fetch YouTube video
    yt = YouTube(url)

    # Get the highest quality audio stream
    audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").first()

    # Download the audio stream
    print(f"Downloading {yt.title}...")
    download_path = audio_stream.download(filename="temp_audio")
    
    # Load audio using moviepy and export in desired format
    audio = AudioFileClip(download_path)
    if output_format == 'wav':
        audio.write_audiofile("output.wav")
    elif output_format == 'mp3':
        audio.write_audiofile("output.mp3")
    else:
        print(f"Unsupported format: {output_format}")

    # Cleanup
    os.remove(download_path)
    print("Download and conversion completed!")

if __name__ == "__main__":
    link = input("Enter the YouTube link: ")
    format_choice = input("Enter desired format (wav/mp3): ").lower()
    download_audio_from_youtube(link, format_choice)
