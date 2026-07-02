import customtkinter as ctk
from PIL import Image, ImageTk


class FileInfo(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        title = ctk.CTkLabel(
            self,
            text="Selected File",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=20)

        # ==========================
        # Main Content Frame
        # ==========================

        self.content = ctk.CTkFrame(self)
        self.content.pack(fill="both", expand=True, padx=20, pady=10)

        self.content.grid_columnconfigure(0, weight=0)
        self.content.grid_columnconfigure(1, weight=1)
        self.content.grid_rowconfigure(0, weight=1)

        # ==========================
        # Thumbnail
        # ==========================

        self.thumbnail_label = ctk.CTkLabel(
            self.content,
            text="No Preview",
            width=320,
            height=180
        )

        self.thumbnail_label.grid(
            row=0,
            column=0,
            padx=15,
            pady=15,
            sticky="n"
        )

        # ==========================
        # Metadata
        # ==========================

        self.info = ctk.CTkTextbox(self.content)

        self.info.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=10,
            pady=10
        )

        self.clear()

    def clear(self):

        self.info.delete("1.0", "end")

        self.info.insert(
            "1.0",
            "No file selected."
        )

        self.thumbnail_label.configure(
            image=None,
            text="No Preview"
        )

    def set_thumbnail(self, image):

        image = ctk.CTkImage(
            light_image=image,
            dark_image=image,
            size=(320, 180)
        )

        self.thumbnail_label.configure(
            image=image,
            text=""
        )

        self.thumbnail_label.image = image

    def update_info(self, data):

        self.info.delete("1.0", "end")

        text = f"""
🎵 File Name

{data['name']}

────────────────────────────

⏱ Duration

{data['duration']}

────────────────────────────

📺 Resolution

{data['resolution']}

────────────────────────────

🎥 Video Codec

{data['video_codec']}

────────────────────────────

🎧 Audio Codec

{data['audio_codec']}

────────────────────────────

🎼 Bitrate

{data['bitrate']}

────────────────────────────

📊 FPS

{data['fps']}

────────────────────────────

🔊 Channels

{data['channels']}

────────────────────────────

🎚 Sample Rate

{data['sample_rate']}

────────────────────────────

💾 File Size

{data['size']} MB

────────────────────────────

📁 Location

{data['path']}
"""

        self.info.insert("1.0", text)