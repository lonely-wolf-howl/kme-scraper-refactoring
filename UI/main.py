import customtkinter as ctk


class MainUI:
    def __init__(
        self,
        font,
        font_size,
    ):
        self.font = font
        self.font_size = font_size
        self.manageVaribles = ManageVariables()

    def start(self):
        root = ctk.CTk()
        root.title("KME Scraper")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        font_style = ctk.CTkFont(self.font, size=self.font_size)

        """
        frame 01
        """
        frame_01 = ctk.CTkFrame(root)
        frame_01.grid(row=0, column=0, padx=(10, 5), pady=(10, 5), sticky="new")

        option_frame = ctk.CTkFrame(frame_01)
        option_frame.pack(side="left", fill="both", expand=True, padx=(10, 5), pady=10)

        amazon_iherb_segemented_button = ctk.CTkSegmentedButton(
            option_frame,
            font=font_style,
            values=[
                " 아마존 ",
                " 아이허브 ",
            ],
            command=self.manageVaribles.update_amazon_iherb_option,
        )
        amazon_iherb_segemented_button.set(" 아마존 ")
        amazon_iherb_segemented_button.pack(expand=True, padx=10, pady=10)

        entry_frame = ctk.CTkFrame(frame_01)
        entry_frame.pack(fill="both", side="right", expand=True, padx=(5, 10), pady=10)

        # Mobile phone number or email = entry
        id_entry = ctk.CTkEntry(
            entry_frame,
            placeholder_text=" Mobile phone number or email",
            font=font_style,
        )
        id_entry.pack(side="top", fill="x", expand=True, padx=20, pady=(10, 2.5))
        # Password = entry
        password_entry = ctk.CTkEntry(
            entry_frame, placeholder_text=" Password", font=font_style
        )
        password_entry.pack(
            side="bottom", fill="x", expand=True, padx=20, pady=(2.5, 10)
        )

        root.mainloop()


class ManageVariables:
    def __init__(self, amazon_iherb_option="amazon", thumbnail_border_color="white"):
        self.amazon_iherb_option = amazon_iherb_option
        self.thumbnail_border_color = thumbnail_border_color

    def update_amazon_iherb_option(self, value: str):
        if value.strip() == "아마존":
            amazon_iherb_option = "amazon"
        else:
            amazon_iherb_option = "iherb"
        print(amazon_iherb_option)

    def get_amazon_iherb_option(self):
        return self.amazon_iherb_option
