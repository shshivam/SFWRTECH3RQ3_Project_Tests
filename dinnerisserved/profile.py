from datetime import date


class Profile:
    def __init__(self):
        self.addresses = []
        self.order_history = []
        self.discount_coupon = []
        self.payment_info = None

    def validate_coupon(self, coupon):
        if coupon.validity.date() < date.today():
            return False
        return True

    def add_discount_coupon(self, coupon):
        if self.validate_coupon(coupon):
            self.discount_coupon.append(coupon)

    def add_address(self, address):
        self.address.append(address)

    def add_order_history(self, order_history):
        self.order_history.append(order_history)

    def add_payment_info(self, payment_info):
        self.payment_info = payment_info

    def add_adresses(self, addresses):
        for address in addresses:
            self.addresses.append(address)
