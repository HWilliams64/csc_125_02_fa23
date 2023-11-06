import math


class Size:

    def __init__(self, length, width, weight, thickness):
        self.__length = length
        self.__width = width
        self.__weight = weight
        self.__thickness = thickness

    @property
    def screen_size(self):
        return math.sqrt((self.__length ** 2) + (self.__width ** 2))

    @property
    def volume(self):
        return self.__length * self.__width * self.__thickness

    @property
    def density(self):
        return self.__weight / self.volume

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @property
    def thickness(self):
        return self.__thickness


class PhonePlan:

    def __init__(self, phone_number: str, minutes: int, messages: int, data: int, ):
        self.__minutes_left = minutes
        self.__minutes_cap = minutes

        self.__messages_left = messages
        self.__messages_cap = messages

        self.__data_left = data
        self.__data_cap = data
        self.__phone_number = phone_number

    def call(self, call_duration: int):
        self.__minutes_left -= call_duration
        self.__minutes_left = max(self.__minutes_left, 0)

    def can_call(self, call_duration: int):
        return self.__minutes_left >= call_duration

    def text(self):
        self.__messages_left -= 1
        self.__messages_left = max(self.__messages_left, 0)

    def can_text(self):
        return self.__messages_left >= 1

    def surf(self, bytes: int):
        self.__data_left -= bytes
        self.__data_left = max(self.__data_left, 0)

    def can_surf(self, bytes: int):
        return self.__data_left >= bytes

    @property
    def phone_number(self):
        return self.__phone_number

    def __str__(self):
        return f"{self.__phone_number} Minutes left: {self.__minutes_left}, Messages left: {self.__messages_left} Data Left: {self.__data_left}"


class SmartPhone():
    # Characteristics:
    # Size: length, width, weight, thickness
    # OS
    # Make Model
    # Color
    # Carrier

    # Functionalities:
    # text
    # calling
    # web
    # apps / Location
    # Take a picture

    def __init__(
            self, size: Size, os: str, make: str, model: str, color: str,
            phone_plan: PhonePlan):
        self.__size = size
        self.__phone_plan = phone_plan
        self.__os = os
        self.__make = make
        self.__model = model

    def __str__(self):
        return f"{self.__make} {self.__model} {self.__phone_plan.phone_number}"


size = Size(100, 100, 100, 10)
phone_plan = PhonePlan("+1-123-456-7890", 10, 10, 10)

phone = SmartPhone(size, "Android", "Samsung", "Galaxy S9", "Black", phone_plan)

print(phone)
