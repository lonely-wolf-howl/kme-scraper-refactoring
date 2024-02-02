import customtkinter as ctk
import openpyxl
import re
from typing import List


class MainUI:
    def __init__(self, font, font_size):
        self.font = font
        self.font_size = font_size
        self.manageVaribles = ManageVariables()
        self.excelCRUD = ExcelCRUD()

        self.url_entry = None
        self.log_textbox = None
        self.url_scrollable_frame = None

    def start(self):
        root = ctk.CTk()
        root.title("KME Scraper")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.font_style = ctk.CTkFont(self.font, size=self.font_size)

        """
        frame 01
        """
        frame_01 = ctk.CTkFrame(root)
        frame_01.grid(row=0, column=0, padx=(10, 5), pady=(10, 5), sticky="new")

        option_frame = ctk.CTkFrame(frame_01)
        option_frame.pack(side="left", fill="both", expand=True, padx=(10, 5), pady=10)

        amazon_iherb_segemented_button = ctk.CTkSegmentedButton(
            option_frame,
            font=self.font_style,
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
            font=self.font_style,
        )
        id_entry.pack(side="top", fill="x", expand=True, padx=20, pady=(10, 2.5))
        # Password = entry
        password_entry = ctk.CTkEntry(
            entry_frame, placeholder_text=" Password", font=self.font_style
        )
        password_entry.pack(
            side="bottom", fill="x", expand=True, padx=20, pady=(2.5, 10)
        )

        """
        frame 02
        """
        frame_02 = ctk.CTkFrame(root)
        frame_02.grid(row=1, column=0, padx=(10, 5), pady=5, sticky="new")

        image_frame = ctk.CTkFrame(frame_02)
        image_frame.pack(side="top", fill="both", expand=True, padx=10, pady=(10, 2.5))

        # 네이버 = checkbox
        naver_checkbox = ctk.CTkCheckBox(
            image_frame, text=" 네이버 (1000 , 860)", font=self.font_style
        )
        naver_checkbox.pack(expand=True, side="left", padx=(50, 10), pady=10)
        # 쿠팡 = checkbox
        coupang_checkbox = ctk.CTkCheckBox(
            image_frame, text=" 쿠팡 (500 , 780)", font=self.font_style
        )
        coupang_checkbox.pack(expand=True, side="left", padx=(10, 50), pady=10)

        border_frame = ctk.CTkFrame(frame_02)
        border_frame.pack(side="top", fill="both", expand=True, padx=10, pady=(2.5, 10))

        # 색상 결정 = segemented button
        color_segemented_button = ctk.CTkSegmentedButton(
            border_frame,
            font=self.font_style,
            values=[
                " White ",
                " Red ",
                " Orange ",
                " Yellow ",
                " Green ",
                " Blue ",
                " Purple ",
            ],
            command=self.manageVaribles.update_thumbnail_border_color,
        )
        color_segemented_button.set(" White ")
        color_segemented_button.pack(expand=True, padx=10, pady=10)

        """
        frame 03
        """
        frame_03 = ctk.CTkFrame(root)
        frame_03.grid(
            row=0, rowspan=4, column=1, padx=(5, 10), pady=(10, 5), sticky="news"
        )
        # 제품 주소 = entry
        self.url_entry = ctk.CTkEntry(
            frame_03, placeholder_text=" 제품 주소", font=self.font_style
        )
        self.url_entry.pack(fill="x", padx=10, pady=(10, 2.5))

        self.url_scrollable_frame = ctk.CTkScrollableFrame(frame_03, width=500)
        self.url_scrollable_frame.pack(fill="both", expand=True, padx=10, pady=2.5)

        # 제품 주소(URL) 중복 검사 => 목록 추가 = button
        add_button = ctk.CTkButton(
            frame_03,
            width=200,
            text="제품 주소 중복 검사 => 목록 추가",
            font=self.font_style,
            command=self.check_duplicates_and_add_URL,
        )
        add_button.pack(fill="x", padx=10, pady=2.5)

        # 제품 사진 수집 => 금지 성분 조사 = button
        add_button = ctk.CTkButton(
            frame_03,
            width=200,
            text="제품 사진 수집 => 금지 성분 조사",
            font=self.font_style,
            # command=images_and_ingredients
        )
        add_button.pack(fill="x", padx=10, pady=(2.5, 10))

        """
        text frame
        """
        textbox_frame = ctk.CTkFrame(root)
        textbox_frame.grid(row=2, column=0, padx=(10, 5), pady=5, sticky="news")

        # 설명 출력창 = textbox
        self.log_textbox = ctk.CTkTextbox(
            textbox_frame, height=30, font=self.font_style
        )
        self.log_textbox.pack(fill="both", expand=True, padx=10, pady=10)

        root.mainloop()

    def check_duplicates_and_add_URL(self):
        amazon_iherb_value = self.manageVaribles.get_amazon_iherb_option()

        if amazon_iherb_value == "amazon":
            amazon_url = self.url_entry.get().strip()

            sheet = self.excelCRUD.choose_sheet("amazon")
            print(sheet)  # <Worksheet "amazon">

            products_amazon_urls = []

            for row in sheet.iter_rows(min_row=2, min_col=4, max_col=4):
                for cell in row:
                    products_amazon_urls.append(cell.value)

            self.log_textbox.delete("0.0", ctk.END)
            if amazon_url in products_amazon_urls:
                answer = "[경고] 중복되는 제품 주소가 존재합니다!"
                self.log_textbox.insert("0.0", answer)
            else:
                answer = "제품 주소가 추가되었습니다."
                self.log_textbox.insert("0.0", answer)

                self.manageVaribles.append_amazon_url(amazon_url)

                # 제품 주소 = frame
                url_frame = ctk.CTkFrame(self.url_scrollable_frame)
                url_frame.pack(fill="x", pady=(5, 0))

                # 삭제 = button
                delete_button = ctk.CTkButton(
                    url_frame,
                    text="삭제",
                    width=50,
                    fg_color="#CC3D3D",
                    hover_color="#960707",
                    font=self.font_style,
                    command=lambda frame=url_frame, url=amazon_url: (
                        self.manageVaribles.remove_amazon_url(url),
                        self.log_textbox.delete("0.0", ctk.END),
                        self.log_textbox.insert("0.0", "삭제 완료!"),
                        frame.destroy(),
                    ),
                )
                delete_button.pack(side="left", padx=5, pady=5)

                # 제품 번호(asin_code) = button
                asin_code = re.search(r"dp\/([A-Z0-9]{10})\/", amazon_url).group(1)
                asin_code_button = ctk.CTkButton(
                    url_frame,
                    text=f"{asin_code}",
                    width=50,
                    font=self.font_style,
                )
                asin_code_button.pack(side="left", pady=5)

                # 제품 주소 = label
                label = ctk.CTkLabel(url_frame, text=amazon_url, font=self.font_style)
                label.pack(side="left", padx=5, pady=5, anchor="center")


class ManageVariables:
    def __init__(
        self,
        amazon_iherb_option="amazon",
        thumbnail_border_color="white",
        amazon_urls=[],
    ):
        self.amazon_iherb_option = amazon_iherb_option
        self.thumbnail_border_color = thumbnail_border_color
        self.amazon_urls: List[str] = amazon_urls

    def update_amazon_iherb_option(self, value: str):
        if value.strip() == "아마존":
            self.amazon_iherb_option = "amazon"
        else:
            self.amazon_iherb_option = "iherb"
        print(self.amazon_iherb_option)

    def get_amazon_iherb_option(self) -> str:
        return self.amazon_iherb_option

    def update_thumbnail_border_color(self, value: str):
        self.thumbnail_border_color = value.strip()
        print(self.thumbnail_border_color)

    def append_amazon_url(self, amazon_url: str):
        self.amazon_urls.append(amazon_url)
        print(self.amazon_urls)

    def remove_amazon_url(self, amazon_url: str):
        self.amazon_urls.remove(amazon_url)
        print(self.amazon_urls)

    def get_amazon_urls(self) -> List[str]:
        return self.amazon_urls


class ExcelCRUD:
    def __init__(self):
        self.excel_file = openpyxl.load_workbook(
            "products.xlsx", data_only=True
        )  # from app.py

    def choose_sheet(self, value: str):
        sheet = self.excel_file[value]
        return sheet
