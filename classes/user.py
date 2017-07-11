class User:
    def __init__(self, email, password, name = None) -> None:
        self.email = email
        self.password = password
        self.name = name
        self.buckets = []
        self.id = None

    def create_bucket(self, bucket) -> bool:
        """
        Creates new bucket for user
        :param bucket: 
        """
        # Check if bucket_name_already exists
        if [existing_bucket for existing_bucket in self.buckets
            if existing_bucket.name == bucket.name]:
                return False
        self.buckets.append(bucket)
        return True
