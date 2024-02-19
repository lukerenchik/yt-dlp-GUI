import tkinter as tk
from tkinter import filedialog
import os
import subprocess


def select_folder_and_convert():
    folder_path = filedialog.askdirectory(title="Select Folder Containing .m4a Files")
    if not folder_path:
        return

    for filename in os.listdir(folder_path):
        if filename.endswith(".m4a"):
            full_path = os.path.join(folder_path, filename)
            new_filename = filename[:-4] + ".mp3"
            new_full_path = os.path.join(folder_path, new_filename)

            # Construct ffmpeg command for conversion
            command = [
                "ffmpeg",
                "-i", full_path,
                "-acodec", "libmp3lame",
                "-q:a", "2",  # High quality: a lower number means higher quality. 2 is quite high.
                new_full_path
            ]

            try:
                subprocess.run(command, check=True)
                print(f"Converted {filename} to {new_filename}.")
            except subprocess.CalledProcessError as e:
                print(f"Failed to convert {filename}. Error: {e}")

    print("Conversion process completed.")


# Setup the GUI
root = tk.Tk()
root.title("M4A to MP3 Converter")

# Button to select folder and start conversion
convert_button = tk.Button(root, text="Select Folder and Convert .m4a to .mp3", command=select_folder_and_convert)
convert_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
