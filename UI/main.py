import customtkinter as ctk
from frames.frame_01 import (
    OptionFrame as Frame_01_OptionFrame,
    EntryFrame as Frame_01_EntryFrame,
)

font = "돋움"
font_size = 13


class MainUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("KME Scraper")

        ctk.set_appearance_mode("dark")  # system, dark, light
        ctk.set_default_color_theme("blue")  # blue(standard), green, dark-blue

        self.font_style = ctk.CTkFont(font, size=font_size)

        frame_01 = ctk.CTkFrame(self)
        frame_01.grid(row=0, column=0, padx=(10, 5), pady=(10, 5), sticky="new")

        Frame_01_OptionFrame(frame_01, self.font_style)
        Frame_01_EntryFrame(frame_01, self.font_style)


mainUI = MainUI()
mainUI.mainloop()
