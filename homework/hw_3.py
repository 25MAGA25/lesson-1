""" Домашнее задание №3 """
from abc import ABC, abstractmethod


class Room(ABC):
    def __init__(self, features, price) -> None:
        self._features = features
        self.__price = price

    @abstractmethod
    def get_price(self):
        return f'Цена комнаты за сутки {self.__price}'

    @abstractmethod
    def get_features(self):
        return f'Особенности этой комнаты {self._features}'


class WifiService:

    def get_wifi_description(self):
        return 'Free WiFe'


class BreakfastService:

    def get_breakfast_description(self):
        return 'Free breakfast'


class StandardRoom(Room):
    def __init__(self, features, price) -> None:
        super().__init__(features, price)

    def get_price(self):
        return super().get_price()

    def get_features(self):
        return super().get_features()


class LuxuryRoom(Room, WifiService, BreakfastService):
    def __init__(self, features, price) -> None:
        super().__init__(features, price)

    def get_price(self):
        return super().get_price()

    def get_features(self):
        features = self._features.copy()
        features.append(self.get_wifi_description())
        features.append(self.get_breakfast_description())
        return features


class FamilyRoom(Room, BreakfastService):
    def __init__(self, features, price) -> None:
        super().__init__(features, price)

    def get_price(self):
        return super().get_price()

    def get_features(self):
        features = self._features.copy
        features.append(self.get_breakfast_description())
        return features


a = StandardRoom(['Телевизор, душ'], 1500)
b = LuxuryRoom(['Телевизор, душ, джакузи, баня'], 4500)
c = FamilyRoom(['Телевизор, душ, детская кровать, детская площадка'], 2700)

print(a.get_features())
print(a.get_price())
print(b.get_features())
print(b.get_price())
print(c.get_features())
print(c.get_price())



























