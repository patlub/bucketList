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

    def create_bucket(self, bucket):
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

    def get_single_bucket(self, bucket_name):
        """
        Gets a single bucket with given name
        :param bucket_name:  
        """
        bucket = self.get_bucket_from_name(bucket_name)
        return bucket[0]

    def delete_bucket(self, bucket_name) -> None:
        """
        Deletes a user's bucket
        :param bucket_name:  
        """
        bucket = self.get_bucket_from_name(bucket_name)
        self.buckets.remove(bucket[0])

    def add_item(self, bucket_name, item):
        """
        Adds an item to a bucket
        :param bucket_name: 
        :param item:  
        """
        bucket = self.get_bucket_from_name(bucket_name)
        bucket[0].items.append(item)

    def edit_item(self, bucket_name, item_name, new_item_name, status):
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
            item[0].status = status

    def get_items(self, bucket_name):
        """
        Returns a list of items from a bucket
        :param bucket_name:  
        """
        bucket = self.get_bucket_from_name(bucket_name)
        return bucket[0].items

    def get_single_item(self, bucket_name, item_name):
        bucket = self.get_bucket_from_name(bucket_name)
        item = [item for item in bucket[0].items if item.name == item_name]
        return item[0]

    def get_bucket_from_name(self, bucket_name):
        """
        gets bucket object using bucket name
        :param bucket_name:  
        """
        return [bucket for bucket in self.buckets
                if bucket.name == bucket_name]

    def delete_item(self, bucket_name, item_name):
        """
        Deletes an item from a bucket
        :param bucket_name: 
        :param item_name:  
        """
        bucket = self.get_bucket_from_name(bucket_name)
        item = [item for item in bucket[0].items if item.name == item_name]
        bucket[0].items.remove(item[0])
