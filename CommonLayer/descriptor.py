class LengthDescriptor:
    def __init__(self, min_char):
        self.__min_char = min_char

    def __set_name__(self, owner, name):
        self.__attribute_name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__attribute_name]

    def __set__(self, instance, value):
        if not isinstance(value, str) or len(value) < self.__min_char:
            raise ValueError(f"Invalid {self.__attribute_name}")
        if any(char.isdigit() for char in value):
            raise ValueError(f"Invalid {self.__attribute_name}, Have Number")
        else:
            instance.__dict__[self.__attribute_name] = value
