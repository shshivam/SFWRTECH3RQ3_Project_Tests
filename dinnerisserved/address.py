class Address:
    def __init__(self, street, city, state, postal_code):
        self.street = street
        self.city = city
        self.state = state
        self.postalCode = postal_code

    def validate_address(self, address):
        if address.postalCode.startswith("L5M"):
            return True
        return False

