class User:
    def __init__(self, email, password, name = None) -> None:
        self.email = email
        self.password = password
        self.name = name
        self.buckets = []
        self.id = None

    def create_bucket(self, bucket):
        self.buckets.append(bucket)
