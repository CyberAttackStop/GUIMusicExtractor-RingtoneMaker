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

import os

from core.audio_extractor import AudioExtractor

from core.thread_worker import Worker

from gui.progress_dialog import ProgressDialog

from gui.ringtone_editor import RingtoneEditor

from core.uvr_engine import UVREngine
import threading

from core.uvr_engine import SeparationLogHandler
from gui.settings_window import SettingsWindow

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

        self.progress_dialog = ProgressDialog(self)
        self.sidebar.disable_controls()
        self.progress_dialog.update()

        self.progress_dialog.lift()

        self.progress_dialog.focus_force()
        

        import os

        self.progress_dialog.set_file(
            os.path.basename(self.current_file)
        )
        
        worker = Worker(
            target=self.start_audio_extraction
        )

        worker.start()
    
    def start_audio_extraction(self):

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
                output_file,
                progress_callback=self.update_progress
            )

            self.status.set_status(
                "Audio Extracted Successfully"
            )

            messagebox.showinfo(
                "Success",
                "Audio extraction completed."
                
            )

            self.after(0, self.sidebar.enable_controls)
        
        except Exception as e:

            messagebox.showerror(
                "Extraction Error",
                str(e)
            )

        self.after(0,self.sidebar.enable_controls)

        self.progress_dialog.destroy()



    def create_ringtone(self):

        if not self.current_file:

            messagebox.showwarning(
                "No File",
                "Please load a media file first."
            )

            return

        self.open_ringtone_editor()


    def open_settings(self):

        try:

            # Prevent multiple Settings windows
            if hasattr(self, "settings_window") and self.settings_window.winfo_exists():
                self.settings_window.focus()
                return

            self.settings_window = SettingsWindow(self)

            self.status.set_status("Settings")

        except Exception as e:

            from tkinter import messagebox

            messagebox.showerror(
                "Settings",
                str(e)
            )

    
    def update_progress(self, value):

        self.after(
            0,
            lambda: self.progress_dialog.set_progress(value)
        )


    def open_ringtone_editor(self):

        if not self.current_file:

            messagebox.showwarning(
                "No File",
                "Please load a media file first."
            )

            return

        RingtoneEditor(self, self.current_file)

    def separate_audio(self):

        if not self.current_file:
            self.status.set_status("Select a media file first.")
            return

        try:

            self.status.set_status("Preparing audio...")

            # If it's a video, extract audio first
            if self.current_file.lower().endswith(
                (".mp4", ".avi", ".mkv", ".mov")
            ):

                os.makedirs("output/extracted", exist_ok=True)

                filename = os.path.splitext(
                    os.path.basename(self.current_file)
                )[0]

                extracted = os.path.join(
                    "output",
                    "extracted",
                    filename + ".mp3"
                )

                FFmpegEngine.extract_audio(
                    self.current_file,
                    extracted
                )

                input_audio = extracted

            else:

                input_audio = self.current_file

            self.status.set_status("Running AI Separation...")

            from gui.separation_progress import SeparationProgress

            self.progress_window = SeparationProgress(
                self,
                os.path.basename(input_audio),
                "BS-RoFormer"
            )

            print("Current File:", self.current_file)
            print("Input Audio:", input_audio)

            self.current_file = input_audio

            import threading

            threading.Thread(
                target=self.run_ai_separation,
                daemon=True
            ).start()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

            self.status.set_status("Failed")
   
    # def run_ai_separation(self):

    #     try:

    #         self.status.set_status("Running AI Separation...")

    #         output_folder = UVREngine.separate(self.current_file)

    #         self.after(
    #             0,
    #             lambda: self.ai_finished(output_folder)
    #         )

    #     except Exception as e:

    #         self.after(
    #             0,
    #             lambda: messagebox.showerror("Error", str(e))
    #         )

    def run_ai_separation(self):

        try:

            self.status.set_status("Running AI Separation...")

            self.after(
                0,
                lambda: self.progress_window.log("Loading AI model...")
            )

            from core.uvr_engine import SeparationLogHandler

            def update_log(msg):

                self.progress_window.log(msg)

                text = msg.lower()

                # --------------------------
                # Loading model
                # --------------------------
                if "loading model" in text:
                    self.progress_window.set_status("Loading model...")
                    self.progress_window.set_progress(0.05)

                # --------------------------
                # Reading audio
                # --------------------------
                elif "audio duration" in text:
                    self.progress_window.set_status("Reading audio...")
                    self.progress_window.set_progress(0.12)

                # --------------------------
                # Preparing chunks
                # --------------------------
                elif "processing" in text:
                    self.progress_window.set_status("Preparing chunks...")
                    self.progress_window.set_progress(0.25)

                # --------------------------
                # Separating
                # --------------------------
                elif (
                    "separator" in text
                    or "inference" in text
                    or "chunk" in text
                    or "segment" in text
                ):

                    current = self.progress_window.progress.get()

                    if current < 0.38:
                        self.progress_window.set_progress(0.38)

                    elif current < 0.45:
                        self.progress_window.set_progress(0.45)

                    elif current < 0.52:
                        self.progress_window.set_progress(0.52)

                    elif current < 0.67:
                        self.progress_window.set_progress(0.67)

                    self.progress_window.set_status("Separating...")

                # --------------------------
                # Saving
                # --------------------------
                elif "saving" in text:
                    self.progress_window.set_status("Saving vocals...")
                    self.progress_window.set_progress(0.83)

                # --------------------------
                # Writing WAV
                # --------------------------
                elif "writing output" in text:
                    self.progress_window.set_status("Writing WAV...")
                    self.progress_window.set_progress(0.95)

                # --------------------------
                # Finished
                # --------------------------
                elif "separation duration" in text:
                    self.progress_window.set_status("Finished")
                    self.progress_window.set_progress(1.00)

            # -------------------------------------------------
            # Register callback BEFORE starting separation
            # -------------------------------------------------

            SeparationLogHandler.callback = lambda msg: self.after(
                0,
                lambda: update_log(msg)
            )

            # -------------------------------------------------
            # Start AI Separation
            # -------------------------------------------------

            output_folder = UVREngine.separate(self.current_file)

            self.after(
                0,
                lambda: self.progress_window.finish()
            )

            self.after(
                0,
                lambda: self.ai_finished(output_folder)
            )

        except Exception as e:

            self.after(
                0,
                lambda: self.progress_window.log(f"ERROR: {e}")
            )

            self.after(
                0,
                lambda: messagebox.showerror("Error", str(e))
            )

    def ai_finished(self, output_folder):

        if hasattr(self, "progress_window"):
            # self.progress_window.close()

            self.status.set_status("Finished!")

        messagebox.showinfo(
            "Success",
            f"Files saved in\n\n{output_folder}"
        )
