class User:
    def __init__(self, email, password, name = None) -> None:
        """
        Initiates class User
        :param email: 
        :param password: 
        :param name: 
        """
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

    def edit_bucket(self, bucket_name, new_bucket_name,
                    new_bucket_description) -> None:
        """
        Edits bucket name and description
        :param bucket_name: 
        :param new_bucket_name: 
        :param new_bucket_description:  
        """
        bucket =  [existing_bucket for existing_bucket in self.buckets
                    if existing_bucket.name == bucket_name]
        if bucket:
            bucket[0].name = new_bucket_name
            bucket[0].description = new_bucket_description

    def get_buckets(self):
        return self.buckets
