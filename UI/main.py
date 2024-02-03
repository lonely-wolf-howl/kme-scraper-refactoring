import customtkinter as ctk
import openpyxl
import re

# Python Type Hint
from typing import List

# Provides the Selenium WebDriver API for browser automation.
from selenium import webdriver

# Offers various methods for identifying web elements in Selenium.
from selenium.webdriver.common.by import By

# ChromeOptions
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Chrome WebDriver
driver = webdriver.Chrome(options=options)
driver.get("https://www.amazon.com/")

import time


class MainUI:
    def __init__(self, font, font_size):
        self.font = font
        self.font_size = font_size
        self.manageVaribles = ManageVariables()
        self.excelCRUD = ExcelCRUD()

        self.UI = False  # flag
        self.id_entry = None
        self.password_entry = None
        self.url_entry = None
        self.url_scrollable_frame = None
        self.log_textbox = None

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
        self.id_entry = ctk.CTkEntry(
            entry_frame,
            placeholder_text=" Mobile phone number or email",
            font=self.font_style,
        )
        self.id_entry.pack(side="top", fill="x", expand=True, padx=20, pady=(10, 2.5))
        # Password = entry
        self.password_entry = ctk.CTkEntry(
            entry_frame, placeholder_text=" Password", font=self.font_style
        )
        self.password_entry.pack(
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
            command=self.images_and_ingredients,
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

        self.UI = True
        root.mainloop()

    def logger(self, message: str):
        if self.UI:
            self.log_textbox.delete("0.0", ctk.END)
            self.log_textbox.insert("0.0", message)

    def check_duplicates_and_add_URL(self):
        option: str = self.manageVaribles.get_amazon_iherb_option()

        url = self.url_entry.get().strip()

        products_urls_from_excel = self.excelCRUD.get_products_urls(option)

        if url in products_urls_from_excel:
            self.logger("[경고] 중복되는 제품 주소가 존재합니다!")
        else:
            self.logger("제품 주소가 추가되었습니다.")

            self.manageVaribles.append_url(url)

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
                command=lambda frame=url_frame, url=url: (
                    self.manageVaribles.remove_url(url),
                    self.logger("삭제 완료!"),
                    frame.destroy(),
                ),
            )
            delete_button.pack(side="left", padx=5, pady=5)

            if option == "amazon":
                asin_code = re.search(r"dp\/([A-Z0-9]{10})\/", url).group(1)
                # 제품 번호(asin_code) = button
                asin_code_button = ctk.CTkButton(
                    url_frame,
                    text=f"{asin_code}",
                    width=50,
                    font=self.font_style,
                )
                asin_code_button.pack(side="left", pady=5)
            else:
                product_id = url.rsplit("/", 1)[-1].replace("?rec=home", "")
                # 제품 번호(product_id) = button
                product_id_button = ctk.CTkButton(
                    url_frame, text=f"{product_id}", width=50, font=self.font_style
                )
                product_id_button.pack(side="left", pady=5)

            # 제품 주소 = label
            label = ctk.CTkLabel(url_frame, text=url, font=self.font_style)
            label.pack(side="left", padx=5, pady=5, anchor="center")

    def images_and_ingredients(self):
        option: str = self.manageVaribles.get_amazon_iherb_option()

        self.logger("처리 중입니다. 여유롭게 기다려주세요!")

        if option == "amazon":
            self.login_amazon(1, 0.3)

    def login_amazon(self, sleep_time, delay_time):
        driver.get(
            "https://www.amazon.com/-/ko/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Flanguage%3Dko_KR%26ref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"
        )

        time.sleep(sleep_time)
        input_string = self.id_entry.get()
        delay = delay_time
        input_field = driver.find_element(By.CSS_SELECTOR, "#ap_email")
        for character in input_string:
            input_field.send_keys(character)
            time.sleep(delay)
        time.sleep(sleep_time)
        driver.find_element(By.CSS_SELECTOR, "#continue").click()

        time.sleep(sleep_time)
        input_string = self.password_entry.get()
        delay = delay_time
        input_field = driver.find_element(By.CSS_SELECTOR, "#ap_password")
        for character in input_string:
            input_field.send_keys(character)
            time.sleep(delay)
        time.sleep(sleep_time)
        driver.find_element(By.CSS_SELECTOR, "#signInSubmit").click()


class ManageVariables:
    def __init__(
        self,
        amazon_iherb_option="amazon",
        thumbnail_border_color="white",
        amazon_urls=[],
        iherb_urls=[],
    ):
        self.amazon_iherb_option = amazon_iherb_option
        self.thumbnail_border_color = thumbnail_border_color
        self.amazon_urls: List[str] = amazon_urls
        self.iherb_urls: List[str] = iherb_urls

    def update_amazon_iherb_option(self, value: str):
        if value.strip() == "아마존":
            self.amazon_iherb_option = "amazon"
        else:
            self.amazon_iherb_option = "iherb"
        print("amazon/iherb =>", self.amazon_iherb_option)

    def get_amazon_iherb_option(self) -> str:
        return self.amazon_iherb_option

    def update_thumbnail_border_color(self, value: str):
        self.thumbnail_border_color = value.strip()
        print("thumbnail border color =>", self.thumbnail_border_color)

    def append_url(self, url: str):
        if self.amazon_iherb_option == "amazon":
            self.amazon_urls.append(url)
        else:
            self.iherb_urls.append(url)

    def remove_url(self, url: str):
        if self.amazon_iherb_option == "amazon":
            self.amazon_urls.remove(url)
        else:
            self.iherb_urls.remove(url)

    def get_urls(self) -> List[str]:
        if self.amazon_iherb_option == "amazon":
            return self.amazon_urls
        else:
            return self.iherb_urls


class ExcelCRUD:
    def __init__(self):
        self.excel_file = openpyxl.load_workbook(
            "products.xlsx", data_only=True
        )  # from app.py

    def get_products_urls(self, option: str) -> List[str]:
        sheet = self.excel_file[option]
        print(sheet)  # <Worksheet "...">

        products_urls = []
        for row in sheet.iter_rows(min_row=2, min_col=4, max_col=4):
            for cell in row:
                products_urls.append(cell.value)
        return products_urls
