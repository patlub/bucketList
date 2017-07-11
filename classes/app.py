class App:
    def __init__(self) -> None:
        super().__init__()
        self.all_users = []

    def sign_up(self, user) -> int:
        """
        Signs up a user to the app
        Args:
            user: user object
        """
        if self.all_users:
            id = self.all_users[len(self.all_users) - 1].id + 1
            user.id = id
        else:
            user.id = 1
        self.all_users.append(user)
        return user.id

    def sign_in(self, user) -> bool:
        """
        signs in a user to the app
        Args:
            user: user object
        """
        for existing_user in self.all_users:
            if existing_user.name == user.name and existing_user.email == user.email:
                return existing_user.id
        return False


    def sign_out(self) -> None:
        """Signs out a user"""
        self.name = None
        self.email = None
        self.password = None

