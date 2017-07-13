class App:
    def __init__(self) -> None:
        super().__init__()
        self.all_users = []

    def sign_up(self, user) -> int:
        """
        Signs up a user to the app
        :param user: 
        """

        if [existing_user for existing_user in self.all_users
            if existing_user.email == user.email]:
            return False

        if self.all_users:
            id = self.all_users[len(self.all_users) - 1].id + 1
            user.id = id
        else:
            user.id = 1
        self.all_users.append(user)
        return user.id

    def sign_in(self, user):
        """
        signs in a user to the app
        :param user: 
        """

        for existing_user in self.all_users:
            if existing_user.email == user.email and existing_user.password == user.password:
                return existing_user.id
        return False


    def sign_out(self) -> None:
        """Signs out a user"""
        self.name = None
        self.email = None
        self.password = None

