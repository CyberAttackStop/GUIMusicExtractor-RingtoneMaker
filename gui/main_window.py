import customtkinter as ctk
from tkinter import filedialog, messagebox

from gui.sidebar import Sidebar
from gui.file_info import FileInfo
from gui.status_bar import StatusBar

from core.ffmpeg_engine import FFmpegEngine

from PIL import Image
from core.thumbnail_engine import ThumbnailEngine

from core.player import MediaPlayer

from gui.player_controls import PlayerControls

import time

from core.audio_extractor import AudioExtractor

class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("GUI Music Extractor + Ringtone Maker")
        self.geometry("1200x700")
        self.minsize(1100, 650)

        # Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = Sidebar(self)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        # File Information
        self.file_info = FileInfo(self)
        self.file_info.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=15,
            pady=15
        )

        # Status Bar
        self.status = StatusBar(self)
        self.status.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="ew"
        )

        self.file_info = FileInfo(self)
        self.file_info.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=15,
            pady=15
        )

        self.player_controls = PlayerControls(self)

        self.player_controls.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=15,
            pady=(0, 10)
        )

        self.player = MediaPlayer()
        self.current_file = None
        self.after(500, self.update_player)

    # ===============================
    # Browse File
    # ===============================
    def browse_file(self):

        file_path = filedialog.askopenfilename(
            filetypes=[
                (
                    "Media Files",
                    "*.mp3 *.wav *.aac *.flac *.m4a *.mp4 *.avi *.mkv *.mov"
                )
            ]
        )

        if not file_path:
            return
        self.current_file = file_path


        try:
            info = FFmpegEngine.get_media_info(file_path)

            if file_path.lower().endswith((".mp4", ".avi", ".mkv", ".mov")):

                thumb = ThumbnailEngine.create_thumbnail(file_path)

                image = Image.open(thumb)

                self.file_info.set_thumbnail(image)

            self.file_info.update_info(info)
            
            self.current_file = file_path
            self.player.load(file_path)

            self.status.set_status("Media Loaded Successfully")

        except Exception as e:
            messagebox.showerror(
                "FFprobe Error",
                str(e)
            )


    # ===============================
    # Media Controls
    # ===============================

    def play_media(self):

        if not self.current_file:
            self.status.set_status("No file selected")
            return

        self.player.play()
        self.status.set_status("Playing")

    def pause_media(self):

        self.player.pause()
        self.status.set_status("Paused")

    def stop_media(self):

        self.player.stop()

        self.player_controls.progress.set(0)

        self.player_controls.current_time.configure(
            text="00:00"
        )

        total = self.player.get_length()

        self.player_controls.total_time.configure(
            text=self.format_time(total)
        )

        self.status.set_status("Stopped")

    # --------------------------
    # ADD HERE
    # --------------------------

    def update_player(self):

        if self.player.is_playing():

            current = self.player.get_time()

            total = self.player.get_length()

            position = self.player.get_position()

            self.player_controls.current_time.configure(
                text=self.format_time(current)
            )

            self.player_controls.total_time.configure(
                text=self.format_time(total)
            )

            self.player_controls.progress.set(position * 100)

        self.after(500, self.update_player)


    def format_time(self, ms):

        if ms <= 0:
            return "00:00"

        seconds = ms // 1000

        minutes = seconds // 60

        seconds = seconds % 60

        return f"{minutes:02}:{seconds:02}"

    # ===============================
    # Placeholder Features
    # ===============================

    def extract_audio(self):

        if not self.current_file:
            messagebox.showwarning(
                "No File",
                "Please select a media file first."
            )
            return

        output_file = filedialog.asksaveasfilename(

            defaultextension=".mp3",

            filetypes=[
                ("MP3 Audio", "*.mp3")
            ]
        )

        if not output_file:
            return

        try:

            AudioExtractor.extract(
                self.current_file,
                output_file
            )

            self.status.set_status(
                "Audio Extracted Successfully"
            )

            messagebox.showinfo(
                "Success",
                "Audio extraction completed."
            )

        except Exception as e:

            messagebox.showerror(
                "Extraction Error",
                str(e)
            )

    def create_ringtone(self):
        self.status.set_status("Create Ringtone - Coming Soon")

    def open_settings(self):
        self.status.set_status("Settings - Coming Soon")


   
   
    

