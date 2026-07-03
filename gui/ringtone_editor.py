import os
import tkinter as tk
import numpy as np
from datetime import datetime
from core.path_manager import PathManager
from core.ringtone.audio_converter import AudioConverter
from core.ringtone.waveform import WaveformGenerator
from core.ringtone.waveform_reader import WaveformReader
from core.ffmpeg_engine import FFmpegEngine
from core.player import MediaPlayer

from tkinter import filedialog, messagebox
from pydub import AudioSegment

import customtkinter as ctk
from PIL import Image

class RingtoneEditor(ctk.CTkToplevel):

    def __init__(self, master, media_file):

        super().__init__(master)

        self.media_file = media_file

        self.player = MediaPlayer()

        self.title("Professional Ringtone Studio")

        self.geometry("900x600")

        self.grab_set()

        self.transient(master)

        self.lift()

        title = ctk.CTkLabel(
            self,
            text="🎵 Professional Ringtone Studio",
            font=("Arial", 26, "bold")
        )



        title.pack(pady=20)
        
        file_name = os.path.basename(self.media_file)

        self.file_label = ctk.CTkLabel(
            self,
            text=f"Selected File: {file_name}",
            font=("Arial", 16)
        )

        self.file_label.pack(pady=10)

        # # Create temporary WAV file
        # self.wav_file = self.prepare_audio()

        # print("Temporary WAV created:")
        # print(self.wav_file)

        # # Generate waveform image
        # self.waveform_image = self.prepare_waveform()

        # print("Waveform image created:")
        # print(self.waveform_image)


        self.waveform = ctk.CTkFrame(
            self,
            height=220
        )

        self.waveform.pack(
            fill="x",
            padx=20,
            pady=20
        )

        self.wave_canvas = tk.Canvas(
            self.waveform,
            width=820,
            height=180,
            bg="#1A1A1A",
            highlightthickness=0
        )

        self.wave_canvas.pack(
            padx=10,
            pady=10
        )

        self.time_frame = ctk.CTkFrame(self)
        self.time_frame.pack(fill="x", padx=20, pady=(5, 10))

        self.start_time_label = ctk.CTkLabel(
            self.time_frame,
            text="Start: 00:00.00"
        )

        self.start_time_label.pack(side="left", padx=10)

        self.end_time_label = ctk.CTkLabel(
            self.time_frame,
            text="End: 00:00.00"
        )

        self.end_time_label.pack(side="right", padx=10)

        # image = Image.open(self.waveform_image)

        # self.wave_image = ctk.CTkImage(
        #     light_image=image,
        #     dark_image=image,
        #     size=(820, 180)
        # )

        # self.wave_label = ctk.CTkLabel(
        #     self.waveform,
        #     image=self.wave_image,
        #     text=""
        # )

        # self.wave_label.pack_forget()

   
        # self.start_slider = ctk.CTkSlider(
        #     self,
        #     from_=0,
        #     to=100
        # )

        # self.start_slider.pack(
        #     fill="x",
        #     padx=25
        # )

        # self.end_slider = ctk.CTkSlider(
        #     self,
        #     from_=0,
        #     to=100
        # )

        # self.end_slider.set(100)

        # self.end_slider.pack(
        #     fill="x",
        #     padx=25,
        #     pady=15
        # )

        self.start_position = 0.10
        self.end_position = 0.90

        self.dragging_start = False
        self.dragging_end = False

        self.preview_btn = ctk.CTkButton(
        self,
        text="▶ Preview Selection",
        command=self.preview_selection
        )


        self.export_btn = ctk.CTkButton(
        self,
        text="💾 Export Ringtone",
        command=self.export_ringtone
        )
        


        self.preview_btn.pack(pady=10)

        self.export_btn.pack(
            pady=20
        )

        
        waveform = WaveformReader.get_waveform(
            self.media_file
        )

        self.draw_waveform(
            waveform
        )

        self.wave_canvas.bind(
            "<Button-1>",
            self.mouse_down
        )

        self.wave_canvas.bind(
            "<B1-Motion>",
            self.mouse_drag
        )

        self.wave_canvas.bind(
            "<ButtonRelease-1>",
            self.mouse_up
        )

        self.media_duration = FFmpegEngine.get_media_info(
        self.media_file
        )["duration_seconds"]
        
        

        self.update_time_labels()

    def prepare_waveform(self):

        wav_file = os.path.join(
            PathManager.TEMP_DIR,
            "preview.wav"
        )

        image_file = os.path.join(
            PathManager.TEMP_DIR,
            "waveform.png"
        )

        AudioConverter.convert_to_wav(
            self.media_file,
            wav_file
        )

        WaveformGenerator.generate(
            wav_file,
            image_file
        )

        return image_file
    
    
    def prepare_audio(self):

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        wav_file = os.path.join(
            PathManager.TEMP_DIR,
            f"preview_{timestamp}.wav"
        )

        AudioConverter.convert_to_wav(
            self.media_file,
            wav_file
        )

        return wav_file
    


    # def draw_waveform(self, waveform):

    #     self.wave_canvas.delete("all")

    #     if len(waveform) == 0:
    #         return

    #     width = 820

    #     height = 180

    #     center = height // 2

    #     x_scale = width / len(waveform)

    #     max_amp = max(abs(waveform))

    #     if max_amp == 0:
    #         max_amp = 1

    #     for i, sample in enumerate(waveform):

    #         x = i * x_scale

    #         y = (sample / max_amp) * 70

    #         self.wave_canvas.create_line(

    #             x,

    #             center - y,

    #             x,

    #             center + y,

    #             fill="#1F6AA5"

    #         )

    def draw_waveform(self, waveform):

        self.wave_canvas.delete("all")

        if len(waveform) == 0:
            return

        width = 820
        height = 180

        center = height / 2

        maximum = np.max(np.abs(waveform))

        if maximum == 0:
            maximum = 1

        x_step = width / len(waveform)

        for i, sample in enumerate(waveform):

            amplitude = (sample / maximum) * 70

            x = i * x_step

            self.wave_canvas.create_line(
                x,
                center - amplitude,
                x,
                center + amplitude,
                fill="#4CC2FF",
                width=1
            )
        self.draw_markers()

    def draw_markers(self):

        width = 820

        height = 180

        x1 = self.start_position * width

        x2 = self.end_position * width

        self.wave_canvas.create_rectangle(
            x1,
            0,
            x2,
            height,
            fill="#2A6F97",
            outline=""
        )

        width = 820
        height = 180

        x1 = self.start_position * width
        x2 = self.end_position * width

        # Start Marker
        self.wave_canvas.create_line(
            x1,
            0,
            x1,
            height,
            fill="#00FF00",
            width=3,
            tags="start"
        )

        # End Marker
        self.wave_canvas.create_line(
            x2,
            0,
            x2,
            height,
            fill="#FF5555",
            width=3,
            tags="end"
        )

    def mouse_down(self, event):

        width = 820

        start_x = self.start_position * width
        end_x = self.end_position * width

        if abs(event.x - start_x) < 10:
            self.dragging_start = True

        elif abs(event.x - end_x) < 10:
            self.dragging_end = True
        
    def mouse_drag(self, event):

        width = 820

        position = max(
            0,
            min(
                event.x / width,
                1
            )
        )

        if self.dragging_start:

            self.start_position = min(
                position,
                self.end_position - 0.01
            )

        elif self.dragging_end:

            self.end_position = max(
                position,
                self.start_position + 0.01
            )

        self.waveform_data = WaveformReader.get_waveform(self.media_file)

        self.draw_waveform(self.waveform_data)

        self.update_time_labels()
      
            
    def mouse_up(self, event):

        self.dragging_start = False
        self.dragging_end = False

    def format_time(self, seconds):

        minutes = int(seconds // 60)

        seconds = seconds % 60

        return f"{minutes:02}:{seconds:05.2f}"
    
    def update_time_labels(self):

        start = self.start_position * self.media_duration

        end = self.end_position * self.media_duration

        self.start_time_label.configure(
            text=f"Starting: {self.format_time(start)}"
        )

        self.end_time_label.configure(
            text=f"Ending: {self.format_time(end)}"
        )

    def preview_selection(self):

        self.player.stop()

        start_ms = int(
            self.start_position * self.media_duration * 1000
        )

        self.preview_end = int(
            self.end_position * self.media_duration * 1000
        )

        self.preview_start = start_ms

        self.player.load(self.media_file)

        self.player.play()

        self.after(100, self.wait_until_playing)

    def monitor_preview(self):

        current = self.player.get_time()

        if current >= self.preview_end:

            self.player.stop()

            return

        self.after(
            100,
            self.monitor_preview
        )

    def wait_until_playing(self):

        if self.player.player.is_playing():

            self.player.player.set_time(self.preview_start)

            self.monitor_preview()

        else:

            self.after(100, self.wait_until_playing)


    def export_ringtone(self):

        try:

            start_ms = int(
                self.start_position * self.media_duration * 1000
            )

            end_ms = int(
                self.end_position * self.media_duration * 1000
            )

            audio = AudioSegment.from_file(self.media_file)

            ringtone = audio[start_ms:end_ms]

            output_file = filedialog.asksaveasfilename(

                defaultextension=".mp3",

                filetypes=[
                    ("MP3 File", "*.mp3"),
                    ("WAV File", "*.wav")
                ]
            )

            if not output_file:
                return

            if output_file.lower().endswith(".wav"):

                ringtone.export(
                    output_file,
                    format="wav"
                )

            else:

                ringtone.export(
                    output_file,
                    format="mp3"
                )

            messagebox.showinfo(

                "Success",

                "Ringtone exported successfully."

            )

        except Exception as e:

            messagebox.showerror(

                "Export Error",

                str(e)

            )