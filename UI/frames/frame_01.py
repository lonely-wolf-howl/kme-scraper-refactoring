import customtkinter as ctk


class OptionFrame(ctk.CTkFrame):
    def __init__(self, parent, font_style):
        super().__init__(parent)
        self.pack(side="left", fill="both", expand=True, padx=(10, 5), pady=10)

        # 아마존 / 아이허브 = radiobutton
        amazon_iherb_option_var = ctk.StringVar(value="amazon")

        amazon_radiobutton = ctk.CTkRadioButton(
            self,
            text=" 아마존",
            fg_color="#EDD200",
            variable=amazon_iherb_option_var,
            value="amazon",
            font=font_style,
        )
        amazon_radiobutton.pack(
            side="top", fill="x", expand=True, padx=10, pady=(10, 2.5)
        )

        iherb_radiobutton = ctk.CTkRadioButton(
            self,
            text=" 아이허브",
            fg_color="#22741C",
            variable=amazon_iherb_option_var,
            value="iherb",
            font=font_style,
        )
        iherb_radiobutton.pack(
            side="bottom", fill="x", expand=True, padx=10, pady=(2.5, 10)
        )


class EntryFrame(ctk.CTkFrame):
    def __init__(self, parent, font_style):
        super().__init__(parent)
        self.pack(side="right", fill="both", expand=True, padx=(5, 10), pady=10)

        # Mobile phone number or email = entry
        self.id_entry = ctk.CTkEntry(
            self,
            placeholder_text=" Mobile phone number or email",
            font=font_style,
        )
        self.id_entry.pack(side="top", fill="x", expand=True, padx=20, pady=(10, 2.5))

        # Password = entry
        self.password_entry = ctk.CTkEntry(
            self, placeholder_text=" Password", font=font_style
        )
        self.password_entry.pack(
            side="bottom", fill="x", expand=True, padx=20, pady=(2.5, 10)
        )
