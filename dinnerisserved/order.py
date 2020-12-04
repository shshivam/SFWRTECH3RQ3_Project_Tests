class Order:

    def __init__(self, cost):
        self.order_type = None
        self.status = None
        self.cost = cost
        self.delivery_address = None

    def set_order_status(self, status):
        self.status = status

    def set_delivery_address(self, address):
        self.delivery_address = address

    def set_order_type (self, order_type):
        self.order_type = order_type

    def place_delivery_order (self, order):
        if order.order_type == 'delivery' and order.cost > 10:
            return True
        return False

    def modify_delivery_order(self, new_address):
        if self.order_type == 'delivery' and self.status != 'out for delivery':
            self.delivery_address = new_address
            return True
        return False

    def allow_payment_on_delivery(self):
        if self.cost > 50:
            return True
        return False

    def cancel_order(self):
        if self.status != 'in-progress':
            return True
        return False
