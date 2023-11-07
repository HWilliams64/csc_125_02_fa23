import math
from typing import Optional


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

    def __init__(self, phone_number: str, minutes: int, messages: int, data: int, network:"Network"):
        self.__minutes_left = minutes
        self.__minutes_cap = minutes

        self.__messages_left = messages
        self.__messages_cap = messages

        self.__data_left = data
        self.__data_cap = data
        self.__phone_number = phone_number
        self.__network = network

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

    @property
    def network(self):
        return self.__network

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
        self.__received_messages = []

    def __str__(self):
        return f"{self.__make} {self.__model} {self.__phone_plan.phone_number}"

    @property
    def phone_plan(self):
        return self.__phone_plan

    def receive_message(self, message: str, phone_number: str):
        self.__received_messages.append({"message":message, "phone_number":phone_number})

    def message_received(self):
        return self.__received_messages

    def send_text(self, message: str, phone_number: str) -> bool:
        
        # Can we send a text?
        if self.__phone_plan.can_text():
            print(f"{self.__phone_plan.phone_number} can text")
            # get the other device
            other_device = self.__phone_plan.network.get_device(phone_number)
            print(f"Network used: {self.__phone_plan.network.name}")
            print(f"{phone_number} device: {other_device}")
            # does the other device exists and can it receive text messages
            if other_device and other_device.phone_plan.can_text():
                other_device.phone_plan.text()
                self.__phone_plan.text()

                other_device.receive_message(message, self.__phone_plan.phone_number)
                return True

        print("Send message failed")
        return False

    def register(self):
        self.phone_plan.network.register_number(self.__phone_plan.phone_number, self)
        


class Network:

    def __init__(self, name, sub_networks=[]):
        self.__name = name
        self.__number_db = {}
        self.__sub_networks = sub_networks
        self.__global_network:Optional[Network] = None

        for sub_network in self.__sub_networks:
            sub_network.__global_network = self

    @property
    def name(self):
        return self.__name

    def register_number(self, number: str, device: SmartPhone):
        self.__number_db[number] = device

    def get_device(self, number: str):
        # Get te device from our network db
        to_return = self.__number_db.get(number, None)

        # If the number is not in the db, try to get it from the global network
        if not to_return and self.__global_network:

            all_numbers = {}

            # for all sub network in the global try to get the device
            for sub_network in self.__global_network.__sub_networks:
                all_numbers.update(sub_network.__number_db)

            return all_numbers.get(number, None)
                

        return to_return

verizon = Network("verizon")
att = Network("at&t")
t_mobile = Network("T-Mobile")

us_network = Network("US", [verizon, att, t_mobile])

size = Size(100, 100, 100, 10)
v_phone_plan = PhonePlan("+1-123-456-7890", 10, 10, 10, verizon)
a_phone_plan = PhonePlan("+1-333-455-7990", 10, 10, 10, att)

android = SmartPhone(size, "Android", "Samsung", "Galaxy S9", "Black", v_phone_plan)

iphone = SmartPhone(size, "iOS", "Apple",
                    "iPhone 16", "Black", a_phone_plan)

android.register()
iphone.register()

print(android.send_text("Hello friend", "+1-333-455-7990"))
print(f"iPhone Received messages: {iphone.message_received()}")