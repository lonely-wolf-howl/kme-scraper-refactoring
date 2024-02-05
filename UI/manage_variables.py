from typing import List


class ManageVariables:
    def __init__(self):
        self._amazon_iherb_option = "amazon"
        self._thumbnail_border_color = "white"
        self._amazon_urls: List[str] = []
        self._iherb_urls: List[str] = []
        self._suspicious_ingredients = ""

    def update_amazon_iherb_option(self, value: str) -> None:
        if value.strip() == "아마존":
            self._amazon_iherb_option = "amazon"
        else:
            self._amazon_iherb_option = "iherb"
        print("amazon/iherb =>", self._amazon_iherb_option)

    def get_amazon_iherb_option(self) -> str:
        return self._amazon_iherb_option

    def update_thumbnail_border_color(self, value: str) -> None:
        self._thumbnail_border_color = value.strip()
        print("thumbnail border color =>", self._thumbnail_border_color)

    def get_thumbnail_border_color(self) -> str:
        return self._thumbnail_border_color

    def append_url(self, url: str) -> None:
        if self._amazon_iherb_option == "amazon":
            self._amazon_urls.append(url)
        else:
            self._iherb_urls.append(url)

    def remove_url(self, url: str) -> None:
        if self._amazon_iherb_option == "amazon":
            self._amazon_urls.remove(url)
        else:
            self._iherb_urls.remove(url)

    def get_urls(self) -> List[str]:
        if self._amazon_iherb_option == "amazon":
            return self._amazon_urls
        else:
            return self._iherb_urls

    def update_suspicious_ingredients(self, value: str) -> None:
        self._suspicious_ingredients = value
        print("suspicious ingredients =>", self._suspicious_ingredients)

    def get_suspicious_ingredients(self) -> str:
        return self._suspicious_ingredients
