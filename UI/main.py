import customtkinter as ctk
from frames.frame_01 import (
    AmazonIherbOptionFrame,
    AmazonIDPasswordInputFrame,
)
from frames.frame_02 import ImageSizeOptionFrame, BorderColorOptionFrame

font = "돋움"
font_size = 13

thumbnail_color = "white"


class MainUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("KME Scraper")

        # self.protocol("WM_DELETE_WINDOW", self.open_toplevel)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.font_style = ctk.CTkFont(font, size=font_size)

        """
        frame 01
        """
        frame_01 = ctk.CTkFrame(self)
        frame_01.grid(row=0, column=0, padx=(10, 5), pady=(10, 5), sticky="new")

        AmazonIherbOptionFrame(frame_01, self.font_style)
        AmazonIDPasswordInputFrame(frame_01, self.font_style)

        """
        frame 02
        """
        frame_02 = ctk.CTkFrame(self)
        frame_02.grid(row=1, column=0, padx=(10, 5), pady=5, sticky="new")

        ImageSizeOptionFrame(frame_02, self.font_style)
        BorderColorOptionFrame(frame_02, self.font_style)


mainUI = MainUI()
mainUI.mainloop()
