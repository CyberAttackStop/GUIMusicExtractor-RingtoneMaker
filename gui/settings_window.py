import customtkinter as ctk


class SettingsWindow(ctk.CTkToplevel):

    def __init__(self, master):

        super().__init__(master)

        self.title("Settings")
        self.geometry("700x500")
        self.resizable(False, False)

        self.grab_set()

        title = ctk.CTkLabel(
            self,
            text="⚙ Settings",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=20)

        ctk.CTkLabel(
            self,
            text="Settings panel is under development."
        ).pack(pady=20)

        ctk.CTkButton(
            self,
            text="Close",
            command=self.destroy
        ).pack(pady=20)