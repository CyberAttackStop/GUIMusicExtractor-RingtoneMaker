import customtkinter as ctk


class ProgressDialog(ctk.CTkToplevel):

    def __init__(self, master):

        super().__init__(master)

        self.title("Extracting Audio")

        self.geometry("500x230")

        self.resizable(False, False)

        self.grab_set()
        self.transient(master)
        self.lift()
        self.focus_force()
        self.attributes("-topmost", True)

        # Remove topmost after a short delay
        self.after(200, lambda: self.attributes("-topmost", False))

        self.label = ctk.CTkLabel(
            self,
            text="🎵 Extracting Audio...",
            font=("Arial", 20, "bold")
        )

        self.label.pack(pady=(20, 10))

        self.file_label = ctk.CTkLabel(
            self,
            text=""
        )

        self.file_label.pack()

        self.progress = ctk.CTkProgressBar(
            self,
            width=420
        )

        self.progress.pack(pady=20)

        self.progress.set(0)

        self.percent = ctk.CTkLabel(
            self,
            text="0%"
        )

        self.percent.pack()

        self.cancel_btn = ctk.CTkButton(
            self,
            text="Cancel"
        )

        self.cancel_btn.pack(pady=20)

    def set_progress(self, value):

        self.progress.set(value)

        self.percent.configure(
            text=f"{int(value*100)}%"
        )

        self.elapsed = ctk.CTkLabel(
            self,
            text="Elapsed : 00:00"
        )

        self.elapsed.pack()

        self.speed = ctk.CTkLabel(
            self,
            text="Speed : --"
        )

        self.speed.pack()

    def set_file(self, filename):

        self.file_label.configure(
            text=filename
        )