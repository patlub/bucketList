class User:
    def __init__(self) -> None:
        super().__init__()

    def sign_up(self, name, email, password) -> None:
        """
        Signs up a user to the app
        Args:
            name: user's name
            email: user's email
            password: user's password
        """
        self.name = name
        self.email = email
        self.password = password

    def sign_in(self, email, password) -> bool:
        """
        signs in a user to the app
        Args:
            email: user's email 
            password: user's password
        """
        existing_email = 'Patrick@gmail.com'
        existing_password = 'patrick'

        if email == existing_email and password == existing_password:
            self.email = email
            self.password = password
            self.name = existing_email[:existing_email.find('@')]
            return True
        return False

    def sign_out(self) -> None:
        """Signs out a user"""
        self.name = None
        self.email = None
        self.password = None
