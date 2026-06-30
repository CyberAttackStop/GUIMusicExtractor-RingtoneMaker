import customtkinter as ctk


class StatusBar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, height=35)

        self.grid_propagate(False)

        self.label = ctk.CTkLabel(
            self,
            text="Ready",
            anchor="w"
        )

        self.label.pack(side="left", padx=10)

    def set_status(self, text):
        self.label.configure(text=text)