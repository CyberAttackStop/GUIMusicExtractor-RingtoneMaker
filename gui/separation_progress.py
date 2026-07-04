import customtkinter as ctk
from datetime import datetime


class SeparationProgress(ctk.CTkToplevel):

    def __init__(self, master, filename, model):

        super().__init__(master)

        self.title("AI Music Separation")
        self.geometry("700x500")
        self.resizable(False, False)

        self.grab_set()

        # Progress value
        self.progress_value = 0.0

        title = ctk.CTkLabel(
            self,
            text="🎵 AI Music Separation",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=15)

        self.file_label = ctk.CTkLabel(
            self,
            text=f"File : {filename}"
        )
        self.file_label.pack(anchor="w", padx=20)

        self.model_label = ctk.CTkLabel(
            self,
            text=f"Model : {model}"
        )
        self.model_label.pack(anchor="w", padx=20)

        self.status_label = ctk.CTkLabel(
            self,
            text="Status : Preparing..."
        )
        self.status_label.pack(anchor="w", padx=20, pady=(10, 5))

        self.progress = ctk.CTkProgressBar(
            self,
            width=650
        )
        self.progress.pack(padx=20)
        self.progress.set(0)

        self.log_box = ctk.CTkTextbox(
            self,
            width=650,
            height=260
        )
        self.log_box.pack(
            padx=20,
            pady=15
        )

        self.cancel_btn = ctk.CTkButton(
            self,
            text="Cancel",
            command=self.destroy
        )
        self.cancel_btn.pack(pady=10)

    # -----------------------------
    # Add log
    # -----------------------------
    def log(self, message):

        timestamp = datetime.now().strftime("%H:%M:%S")

        self.log_box.insert(
            "end",
            f"[{timestamp}] {message}\n"
        )

        self.log_box.see("end")

        self.update_idletasks()

    # -----------------------------
    # Update status
    # -----------------------------
    def set_status(self, text):

        self.status_label.configure(
            text=f"Status : {text}"
        )

        self.update_idletasks()

    # -----------------------------
    # Update progress
    # -----------------------------
    def set_progress(self, value):

        value = max(0, min(value, 1))

        self.progress.set(value)

        self.progress_value = value

        self.update_idletasks()

    # -----------------------------
    # Add log + auto progress
    # -----------------------------
    def add_log(self, message):

        timestamp = datetime.now().strftime("%H:%M:%S")

        self.log_box.insert(
            "end",
            f"[{timestamp}] {message}\n"
        )

        self.log_box.see("end")

        # Auto increase progress
        if self.progress_value < 0.95:
            self.progress_value += 0.03
            self.progress.set(self.progress_value)

        self.update_idletasks()

    # -----------------------------
    # Finish
    # -----------------------------
    def finish(self):

        self.progress.set(1.0)

        self.status_label.configure(
            text="Status : Completed"
        )

        self.log("✔ Separation Finished.")

        self.update_idletasks()


    def close(self):
        self.destroy()