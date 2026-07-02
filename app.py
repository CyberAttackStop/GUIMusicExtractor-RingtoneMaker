import customtkinter as ctk
from gui.main_window import MainWindow

from core.path_manager import PathManager

PathManager.create_folders()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()