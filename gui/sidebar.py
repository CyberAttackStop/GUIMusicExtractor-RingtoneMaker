import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master, width=220)

        self.master = master

        self.grid_propagate(False)

        title = ctk.CTkLabel(
            self,
            text="MENU",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=20)

        self.browse_btn = ctk.CTkButton(
            self,
            text="Browse File",
            command=self.master.browse_file
        )

        self.browse_btn.pack(fill="x", padx=15, pady=8)

        buttons = [
            "Play",
            "Pause",
            "Stop",
            "Extract Audio",
            "Create Ringtone",
            "Settings"
        ]

        for text in buttons:

            btn = ctk.CTkButton(
                self,
                text=text
            )

            btn.pack(fill="x", padx=15, pady=8)