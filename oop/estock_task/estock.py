from abc import ABC, abstractmethod
import random
import pprint


class Product(ABC):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        self._id = self.__id()
        self.price_with_vat = self.vat_price()

    def __id(self) -> str:
        return f'{str(random.random()).split(".")[1]}_({self.name})'

    def vat_price(self):
        return f'{self.price * 1.21: .2f}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 2:
            self.__name = name
        else:
            print('Invalid name provided, placeholder will be used')
            self.__name = 'product'

    @name.deleter
    def name(self):
        self.__name = None

    @abstractmethod
    def product_view(self):
        pass


class Game(Product):
    def __init__(self, name: str, price: float, genre: str):
        super().__init__(name, price)
        self.genre = genre

    def product_view(self):
        print(f"Game: {self.name} ({self.genre})")


class Console(Product):
    def __init__(self, name: str, price: float, brand: str):
        super().__init__(name, price)
        self.brand = brand

    def product_view(self):
        print(f"Console: {self.name} ({self.brand})")


class Merchandise(Product):
    def __init__(self, name: str, price: float, category: list):
        super().__init__(name, price)
        self.category = category

    def product_view(self):
        print(f"Merchandise: {self.name} ({self.category})")


def view(*products):
    for product in products:
        product.product_view()
        pprint.pprint(vars(product))
        print('*' * 80)


view(
    Console('PS3', 200.00, 'Sony Play Station'),
    Console('XBOX360', 230.99, 'Microsoft XBOX'),
    Game('Final Fantasy X', 23.00, 'JRPG'),
    Game('Need For Speed Most Wanted', 34.99, 'Racing'),
    Merchandise('Marvel Avengers', 10.45, ['cup', 'dishes']),
    Merchandise('Silent Hill', 12.99, ['poster', 'decorations', 'design'])
)
