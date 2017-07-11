class User:
    def __init__(self, email, password, name=None) -> None:
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
        bucket = self.get_bucket_from_name(bucket_name)
        if bucket:
            bucket[0].name = new_bucket_name
            bucket[0].description = new_bucket_description

    def get_buckets(self):
        """
        Returns list of all user's buckets 
        """
        return self.buckets

    def delete_bucket(self, bucket_name) -> None:
        """
        Deletes a user's bucket
        :param bucket_name:  
        """
        bucket = self.get_bucket_from_name(bucket_name)
        self.buckets.remove(bucket[0])

    def get_single_bucket(self, bucket_name):
        """
        Gets a single bucket with given name
        :param bucket_name:  
        """
        bucket = self.get_bucket_from_name(bucket_name)
        return bucket[0]

    def add_item(self, bucket_name, item):
        """
        Adds an item to a bucket
        :param bucket_name: 
        :param item:  
        """
        bucket = self.get_bucket_from_name(bucket_name)
        bucket[0].items.append(item)

    def edit_item(self, bucket_name, item_name, new_item_name):
        """
        Edit an item in a bucket
        :param bucket_name: 
        :param item_name: 
        :param new_item_name:  
        """
        bucket = self.get_bucket_from_name(bucket_name)
        item = [item for item in bucket[0].items
                if item.name == item_name]
        if item:
            item[0].name = new_item_name

    def get_items(self, bucket_name):
        pass

    def get_bucket_from_name(self, bucket_name):
        return [bucket for bucket in self.buckets
                if bucket.name == bucket_name]

