import customtkinter as ctk


class FileInfo(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        title = ctk.CTkLabel(
            self,
            text="Selected File",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=20)

        self.info = ctk.CTkTextbox(self)

        self.info.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.clear()

    def clear(self):

        self.info.delete("1.0", "end")

        self.info.insert(
            "1.0",
            "No file selected."
        )

    def update_info(self, data):

        self.info.delete("1.0", "end")

        text = f"""
File Name :

{data['name']}

-------------------------------------------------

File Type :

{data['type']}

-------------------------------------------------

File Size :

{data['size']}

-------------------------------------------------

Location :

{data['path']}
"""

        self.info.insert("1.0", text)