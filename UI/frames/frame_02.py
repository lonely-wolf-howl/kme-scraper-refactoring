import customtkinter as ctk


class ImageSizeOptionFrame(ctk.CTkFrame):
    def __init__(self, parent, font_style):
        super().__init__(parent)
        self.pack(side="top", fill="both", expand=True, padx=10, pady=(10, 2.5))

        # 네이버 = checkbox
        self.naver_checkbox = ctk.CTkCheckBox(
            self, text=" 네이버 (1000 , 860)", font=font_style
        )
        self.naver_checkbox.pack(expand=True, side="left", padx=(50, 10), pady=10)
        # 쿠팡 = checkbox
        self.coupang_checkbox = ctk.CTkCheckBox(
            self, text=" 쿠팡 (500 , 780)", font=font_style
        )
        self.coupang_checkbox.pack(expand=True, side="left", padx=(10, 50), pady=10)


class BorderColorOptionFrame(ctk.CTkFrame):
    def __init__(self, parent, font_style):
        super().__init__(parent)
        self.pack(side="top", fill="both", expand=True, padx=10, pady=(2.5, 10))

        # 색상 결정 = segmented button
        self.color_segmented_button = ctk.CTkSegmentedButton(
            self,
            font=font_style,
            values=[
                " White ",
                " Red ",
                " Orange ",
                " Yellow ",
                " Green ",
                " Blue ",
                " Purple ",
            ],
            command=self.get_border_color_input,
        )
        self.color_segmented_button.set(" White ")
        self.color_segmented_button.pack(expand=True, padx=10, pady=10)

    def get_border_color_input(self, value):
        global thumbnail_color
        print(value)
        thumbnail_color = value.strip()
