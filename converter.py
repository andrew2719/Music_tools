import os
from pydub import AudioSegment
from tkinter import filedialog, Tk, simpledialog

def convert_audio(file_path, destination_format, output_directory):
    base_filename = os.path.basename(file_path)
    file_name_without_extension = os.path.splitext(base_filename)[0]
    output_file_name = f"{file_name_without_extension}.{destination_format}"

    # Read audio file
    audio = AudioSegment.from_file(file_path, format="mp3" if file_path.endswith('.mp3') else None)

    # Convert and export
    if destination_format == "mp3":
        audio.export(os.path.join(output_directory, output_file_name), format="mp3")
    else:
        audio.export(os.path.join(output_directory, output_file_name), format="wav")

def main():
    # Create a GUI window to select the file
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(title="Select the audio file", filetypes=[("All Files", "*.*")])

    if not file_path:
        print("No file selected. Exiting.")
        return

    # Ask the user for the conversion format
    format_choice = int(input(
        '''
[1] mp3
[2] wav'''
    ))

    # if format_choice not in ["mp3", "wav"]:
    #     print("Invalid format choice. Exiting.")
    #     return

    if format_choice==1:
        format_choice="mp3"
    elif format_choice==2:
        format_choice="wav"
    else:
        print("enter valid number")


    try:

    # You can change this to the directory where you want to save the converted files
        output_directory = "D:/samples/"
        print("converting started")
        # Convert the file
        convert_audio(file_path, format_choice, output_directory)
        print(f"File converted and saved to {output_directory}")
    except:
        print("error occured")

if __name__ == "__main__":
    main()
