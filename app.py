from mac.checker import MACAddressChecker
from ui.warning import WarningUI

default_set_date = "2024-02-01"
days = 30
default_mac_address = "40-B0-76-42-8F-**"

warning_message_access_denied = "인증된 사용자가 아닙니다."
warning_message_expired = "사용 기간이 만료되었습니다."


class App:
    def __init__(self):
        self.macAddressChecker = MACAddressChecker(
            default_set_date, days, default_mac_address
        )
        self.access_denied = WarningUI(warning_message_access_denied)
        self.expired = WarningUI(warning_message_expired)

    def start(self):
        if self.macAddressChecker.is_default_mac_address():
            if self.macAddressChecker.is_expired():
                return "..."
            else:
                self.expired.show_warning()
        else:
            self.access_denied.show_warning()


app = App()
app.start()
