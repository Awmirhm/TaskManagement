class Task:
    def __init__(self, id, title, description, start_time, end_time, status, user_id):
        self.id = id
        self.title = title
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.status = status
        self.user_id = user_id

    @classmethod
    def create_with_list(cls, data: list):
        return cls(data[0], data[1], data[2], data[3], data[4], data[5], data[6])

    @classmethod
    def create_with_tuple(cls, data: tuple):
        return cls(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
