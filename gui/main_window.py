import customtkinter as ctk
from tkinter import filedialog

from gui.sidebar import Sidebar
from gui.file_info import FileInfo
from gui.status_bar import StatusBar
from core.file_manager import FileManager


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
            row=1,
            column=0,
            columnspan=2,
            sticky="ew"
        )

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

        info = FileManager.get_file_info(file_path)

        self.file_info.update_info(info)

        self.status.set_status("File Loaded Successfully")