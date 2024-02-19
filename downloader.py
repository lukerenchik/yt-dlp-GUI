import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess
import os

# Initialize a variable to hold the output directory
output_dir = os.path.join(os.getcwd(), "downloads")

def download_video():
    url = url_entry.get()  # Get URL from the entry widget
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return
    try:
        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)
        command = [
            "yt-dlp",
            "-f", "bestaudio",
            "--extract-audio",
            "--audio-format", "m4a",
            "--output", os.path.join(output_dir, "%(title)s.%(ext)s"),
            url
        ]
        subprocess.run(command, check=True)
        messagebox.showinfo("Success", "Downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download: {e}")

def select_output_folder():
    global output_dir
    selected_folder = filedialog.askdirectory()
    if selected_folder:  # If a folder was selected
        output_dir = selected_folder
        folder_path_label.config(text=output_dir)

# Create the main window
root = tk.Tk()
root.title("YouTube to MP3 Downloader")

# Create a frame for the URL entry and button
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# URL entry widget
url_label = tk.Label(frame, text="YouTube URL:")
url_label.pack(side=tk.LEFT)
url_entry = tk.Entry(frame, width=50)
url_entry.pack(side=tk.LEFT, padx=5)

# Download button
download_button = tk.Button(root, text="Download MP3", command=download_video)
download_button.pack(pady=5)

# Output folder selection
folder_selection_button = tk.Button(root, text="Select Output Folder", command=select_output_folder)
folder_selection_button.pack(pady=5)

# Display the current output path
folder_path_label = tk.Label(root, text=output_dir)
folder_path_label.pack(pady=5)

# Start the GUI event loop
root.mainloop()
