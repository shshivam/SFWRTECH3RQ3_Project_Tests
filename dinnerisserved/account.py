class Account:
    def __init__(self, name, username, password, profile):
        self.name = name
        self.username = username
        self.password = password
        self.profile = profile
        self.email = ''

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            return True
        return False

    def check_email(self, email):
        if '@' in email:
            return True
        return False

    def set_email(self, email):
        if self.check_email(email):
            self.email = email

    def delete_account(self):
        self.name = None
        self.username = None
        self.password = None
        self.profile = None
        self.email = None
