import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master, width=220)

        self.master = master

        self.grid_propagate(False)

        # ==========================
        # Title
        # ==========================

        title = ctk.CTkLabel(
            self,
            text="MENU",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=20)

        # ==========================
        # Browse Button
        # ==========================

        self.browse_btn = ctk.CTkButton(
            self,
            text="Browse File",
            command=self.master.browse_file
        )

        self.browse_btn.pack(fill="x", padx=15, pady=8)

        # ==========================
        # Play Button
        # ==========================

        self.play_btn = ctk.CTkButton(
            self,
            text="Play",
            command=self.master.play_media
        )

        self.play_btn.pack(fill="x", padx=15, pady=8)

        # ==========================
        # Pause Button
        # ==========================

        self.pause_btn = ctk.CTkButton(
            self,
            text="Pause",
            command=self.master.pause_media
        )

        self.pause_btn.pack(fill="x", padx=15, pady=8)

        # ==========================
        # Stop Button
        # ==========================

        self.stop_btn = ctk.CTkButton(
            self,
            text="Stop",
            command=self.master.stop_media
        )

        self.stop_btn.pack(fill="x", padx=15, pady=8)

        # ==========================
        # Extract Audio
        # ==========================

        self.extract_btn = ctk.CTkButton(
            self,
            text="Extract Audio",
            command=self.master.extract_audio
        )

        self.extract_btn.pack(fill="x", padx=15, pady=8)

        # ==========================
        # Create Ringtone
        # ==========================

        self.ringtone_btn = ctk.CTkButton(
            self,
            text="Create Ringtone",
            command=self.master.create_ringtone
        )

        self.ringtone_btn.pack(fill="x", padx=15, pady=8)

        # ==========================
        # Settings
        # ==========================

        self.settings_btn = ctk.CTkButton(
            self,
            text="Settings",
            command=self.master.open_settings
        )

        self.settings_btn.pack(fill="x", padx=15, pady=8)


        self.play_btn = ctk.CTkButton(
        self,
        text="Play",
        command=self.master.play_media
    )
        self.play_btn.pack(fill="x", padx=15, pady=8)


        self.pause_btn = ctk.CTkButton(
            self,
            text="Pause",
            command=self.master.pause_media
        )
        self.pause_btn.pack(fill="x", padx=15, pady=8)


        self.stop_btn = ctk.CTkButton(
            self,
            text="Stop",
            command=self.master.stop_media
        )
        self.stop_btn.pack(fill="x", padx=15, pady=8)


        self.extract_btn = ctk.CTkButton(
            self,
            text="Extract Audio"
        )
        self.extract_btn.pack(fill="x", padx=15, pady=8)


        self.ringtone_btn = ctk.CTkButton(
            self,
            text="Create Ringtone"
        )
        self.ringtone_btn.pack(fill="x", padx=15, pady=8)


        self.settings_btn = ctk.CTkButton(
            self,
            text="Settings"
        )
        self.settings_btn.pack(fill="x", padx=15, pady=8)

    def disable_controls(self):

        self.browse_btn.configure(state="disabled")

        self.play_btn.configure(state="disabled")

        self.pause_btn.configure(state="disabled")

        self.stop_btn.configure(state="disabled")

        self.extract_btn.configure(state="disabled")

        self.ringtone_btn.configure(state="disabled")

        self.settings_btn.configure(state="disabled")


    def enable_controls(self):

        self.browse_btn.configure(state="normal")

        self.play_btn.configure(state="normal")

        self.pause_btn.configure(state="normal")

        self.stop_btn.configure(state="normal")

        self.extract_btn.configure(state="normal")

        self.ringtone_btn.configure(state="normal")

        self.settings_btn.configure(state="normal")