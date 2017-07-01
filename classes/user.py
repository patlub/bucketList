from gettext import find


class User:
    def __init__(self) -> None:
        self.name = None
        self.email = None
        self.password = None

    def sign_up(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def sign_in(self, email, password) -> bool:
        existing_email = 'Patrick@gmail.com'
        existing_password = 'patrick'

        if email == existing_email and password == existing_password:
            self.email = email
            self.password = password
            self.name = existing_email[:existing_email.find('@')]
            return True
        return False

    def sign_out(self):
        self.name = None
        self.email = None
        self.password = None
