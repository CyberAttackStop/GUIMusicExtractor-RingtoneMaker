import customtkinter as ctk


class PlayerControls(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        # -------------------------
        # Buttons
        # -------------------------

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(fill="x", pady=10)

        self.play_btn = ctk.CTkButton(
            button_frame,
            text="▶ Play",
            width=100,
            command=self.master.play_media
        )

        self.play_btn.pack(side="left", padx=10)

        self.pause_btn = ctk.CTkButton(
            button_frame,
            text="⏸ Pause",
            width=100,
            command=self.master.pause_media
        )

        self.pause_btn.pack(side="left", padx=10)

        self.stop_btn = ctk.CTkButton(
            button_frame,
            text="⏹ Stop",
            width=100,
            command=self.master.stop_media
        )

        self.stop_btn.pack(side="left", padx=10)

        # -------------------------
        # Progress Slider
        # -------------------------

        self.progress = ctk.CTkSlider(
            self,
            from_=0,
            to=100,
            command=self.seek
        )

        self.progress.pack(fill="x", padx=20)

        # -------------------------
        # Time Labels
        # -------------------------

        time_frame = ctk.CTkFrame(self)

        time_frame.pack(fill="x", pady=5)

        self.current_time = ctk.CTkLabel(
            time_frame,
            text="00:00"
        )

        self.current_time.pack(side="left")

        self.total_time = ctk.CTkLabel(
            time_frame,
            text="00:00"
        )

        self.total_time.pack(side="right")

        # -------------------------
        # Volume
        # -------------------------

        volume_frame = ctk.CTkFrame(self)

        volume_frame.pack(fill="x", pady=15)

        volume_label = ctk.CTkLabel(
            volume_frame,
            text="🔊 Volume"
        )

        volume_label.pack(side="left")

        self.volume = ctk.CTkSlider(
            volume_frame,
            from_=0,
            to=100,
            command=self.change_volume
        )

        self.volume.set(100)

        self.volume.pack(
            side="left",
            fill="x",
            expand=True,
            padx=10
        )

    def change_volume(self, value):

        self.master.player.set_volume(int(value))


    def seek(self, value):

        self.master.player.set_position(value / 100)