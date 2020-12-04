import datetime

from dinnerisserved.account import Account
from dinnerisserved.address import Address
from dinnerisserved.discountcoupon import DiscountCoupon
from dinnerisserved.history import History
from dinnerisserved.order import Order
from dinnerisserved.paymentinfo import PaymentInfo
from dinnerisserved.profile import Profile


# 3.1.1 Profile Creation
def test_profile_creation():
    profile = Profile()
    account = Account('Shivam', 'shars48', 'password', profile)
    account.set_email('shivam@xyz.com')

    assert account.name == 'Shivam' and account.email == 'shivam@xyz.com' and account.password == 'password' and account.username == 'shars48', "Account should be created"


# 3.1.2 Email Verification
def test_valid_email_verification():
    profile = Profile()
    account = Account('Shivam', 'shars48', 'password', profile)
    account.set_email('shivam@xyz.com')
    assert account.email == 'shivam@xyz.com', "Valid email should be added"


# 3.1.2 Email Verification
def test_invalid_email_verification():
    profile = Profile()
    account = Account('Shivam', 'shars48', 'password', profile)
    account.set_email('shivam-xyz.com')
    assert account.email != 'shivam-xyz.com', "Invalid email should not be added"


# 3.1.3 Login for existing users
def test_valid_login():
    profile = Profile()
    account = Account('Shivam', 'shars48', 'password', profile)
    assert account.authenticate('shars48', 'password'), "Valid credentials should allow login"


# 3.1.3 Login for existing users
def test_invalid_login():
    profile = Profile()
    account = Account('Shivam', 'shars48', 'password', profile)
    assert account.authenticate('shars48', 'pass') is False, "Valid credentials should allow login"


# 3.1.4 Check order status
def test_check_order_status():
    history = History('Salad', 'delivered', datetime.datetime(2020, 5, 17))
    profile = Profile()
    profile.add_order_history(history)
    assert profile.order_history[0].order_status == 'delivered', "Should be able to check order status from history"


# 3.1.5 Order History
def test_add_order_history():
    profile = Profile()
    assert len(profile.order_history) == 0, "Order history should be empty"

    history1 = History('Salad', 'delivered', datetime.datetime(2020, 5, 17))
    history2 = History('Burger', 'cancelled', datetime.datetime(2020, 5, 18))

    profile.add_order_history(history1)
    profile.add_order_history(history2)

    assert len(profile.order_history) == 2, "Order history should contain the items that were ordered"


# 3.1.7 Save payment information
def test_add_payment_info_to_account():
    profile = Profile()
    payment_info = PaymentInfo('VISA', '0000-1111-2222-3333')
    profile.add_payment_info(payment_info)

    assert profile.payment_info.details == '0000-1111-2222-3333', "The saved payment info should be correct"


# 3.1.8 Save delivery information
def test_save_multiple_delivery_address():
    profile = Profile()
    addresses = [Address('100 John Rd', 'Toronto', 'ON', 'M5R 7U6'),
                 Address('200 Mark Blvd', 'Mississauga', 'ON', 'L5M 1Y1')]
    profile.add_adresses(addresses)

    assert len(profile.addresses) == 2, "The profile should now have two addresses"


# 3.1.9 Cancel finalized order
def test_cancel_order():
    order = Order('100')
    order.set_order_type('confirmed')
    assert order.cancel_order(), "Should be able to cancel order if not in-progress"


# 3.1.9 Cancel finalized order
def test_cancel_order_in_progress():
    delivery_address = Address('100 John Rd', 'Toronto', 'ON', 'M5R 7U6')
    order = Order('100')
    order.set_order_status('in-progress')
    assert order.cancel_order() is False, "Should not be able to cancel order if in-progress"


# 3.1.10 Modify User Profile
def test_modify_profile():
    profile = Profile()
    account = Account('Shivam', 'shars48', 'password', profile)
    account.set_email('shivam@xyz.com')
    assert account.email == 'shivam@xyz.com', "The current email should be returned"
    account.set_email('shivam@abc.com')
    assert account.email == "shivam@abc.com", "The updated email should be returned"


# 3.1.11 Delete account
def test_delete_account():
    profile = Profile()
    account = Account('Shivam', 'shars48', 'password', profile)
    account.delete_account()
    assert account.authenticate('shars48', 'password') is False, "Should not be able to authenticate after account " \
                                                                 "has been deleted"


# 3.1.12 Apply Discount Coupon
def test_apply_valid_discount_coupon():
    coupon = DiscountCoupon('15% off', datetime.datetime(2020, 12, 30))
    profile = Profile()
    profile.add_discount_coupon(coupon)
    assert len(profile.discount_coupon) == 1, "Should be able to add valid coupon"


# 3.1.12 Apply Discount Coupon
def test_apply_invalid_discount_coupon():
    coupon = DiscountCoupon('15% off', datetime.datetime(2020, 10, 30))
    profile = Profile()
    profile.add_discount_coupon(coupon)
    assert len(profile.discount_coupon) == 0, "Should not be able to add invalid coupon"
