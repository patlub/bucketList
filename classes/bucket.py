class Bucket:
    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description
        self.items = []