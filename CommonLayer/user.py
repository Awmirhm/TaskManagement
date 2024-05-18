from .descriptor import LengthDescriptor
from .mixin import JsonMixin


class User(JsonMixin):
    firstname = LengthDescriptor(3)
    lastname = LengthDescriptor(4)

    def __init__(self, id, firstname, lastname, username, password, meter):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.meter = meter

    @classmethod
    def create_with_tuple(cls, data: tuple):
        return cls(data[0], data[1], data[2], data[3], data[4], data[5])
