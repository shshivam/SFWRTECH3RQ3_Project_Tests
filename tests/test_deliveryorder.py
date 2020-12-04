from dinnerisserved.address import Address
from dinnerisserved.order import Order


# 3.2.1 Order type selection
def test_set_order_type():
    order = Order(100)
    order.set_order_type('delivery')

    assert order.order_type == 'delivery', "Should be able to set order type"


# 3.2.2 Address Verification
def test_valid_delivery_address_verification():
    address = Address('100 John Rd', 'Toronto', 'ON', 'L5M 7U6')
    assert address.validate_address(address), "Should be able to verify valid address"


# 3.2.2 Address Verification
def test_invalid_delivery_address_verification():
    address = Address('100 John Rd', 'Toronto', 'ON', 'L4M 7U6')
    assert address.validate_address(address) is False, "Should not be able to verify invalid address"


# 3.2.3 Minimum Order verification
def test_place_valid_delivery_order_amount():
    order = Order(100)
    order.set_order_type('delivery')
    assert order.place_delivery_order(order), "Should be able to place delivery order of amount 100"


# 3.2.3 Minimum Order verification
def test_place_invalid_delivery_order_amount():
    order = Order(5)
    order.set_order_type('delivery')
    assert order.place_delivery_order(order) is False, "Should not be able to place delivery order of amount 5"


# 3.2.5 Modify delivery order address
def test_valid_modify_delivery_address():
    address = Address('100 John Rd', 'Toronto', 'ON', 'L5M 7U6')
    order = Order(100)
    order.set_order_type('delivery')
    order.set_delivery_address(address)
    order.set_order_status('in-progress')

    new_address = Address('200 John Rd', 'Toronto', 'ON', 'L5M 7U6')
    assert order.modify_delivery_order(new_address), "Should be able to modify delivery order if " \
                                                     "status is not out for delivery"


# 3.2.5 Modify delivery order address
def test_invalid_modify_delivery_address():
    address = Address('100 John Rd', 'Toronto', 'ON', 'L5M 7U6')
    order = Order(100)
    order.set_order_type('delivery')
    order.set_delivery_address(address)
    order.set_order_status('out for delivery')

    new_address = Address('200 John Rd', 'Toronto', 'ON', 'L5M 7U6')
    assert order.modify_delivery_order(new_address) is False, "Should not be able to modify delivery order if " \
                                                              "status is out for delivery"

# 3.2.7 Payment on delivery
def test_valid_payment_on_delivery():
    order = Order(100)
    order.set_order_type('delivery')

    assert order.allow_payment_on_delivery(), "Payment on delivery should be allowed if order amount is more than 50"


# 3.2.7 Payment on delivery
def test_invalid_payment_on_delivery():
    order = Order(49)
    order.set_order_type('delivery')

    assert order.allow_payment_on_delivery() is False, "Payment on delivery should not be allowed if " \
                                                       "order amount is less than 50"
