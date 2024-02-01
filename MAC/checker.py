import psutil
import datetime


class MACAddressChecker:
    def __init__(self, default_set_date, days, default_mac_address):
        self.default_set_date = default_set_date
        self.days = days
        self.expiration_date = datetime.datetime.strptime(
            self.default_set_date, "%Y-%m-%d"
        ).date() + datetime.timedelta(days=self.days)
        self.default_mac_address=default_mac_address

    @staticmethod
    def get_mac_address():
        interfaces = psutil.net_if_addrs()
        for interface in interfaces.values():
            for addr in interface:
                if addr.family == psutil.AF_LINK:
                    return addr.address
        return None

    def is_default_mac_address(self):
        current_user_mac_address = self.get_mac_address()
        return current_user_mac_address == self.default_mac_address

    def is_expired(self):
        current_date = datetime.datetime.now().date()
        return current_date > self.expiration_date
