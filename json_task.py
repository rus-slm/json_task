import json

file_json = """{
    "title": "python",
    "price": 1,
    "location": {
        "address": "город Москва, Лесная, 7", "metro_stations": ["Белорусская"]
    }
}"""

file_json2 = """{
"title": "Вельш-корги", 
"price": 1000, 
"class": "dogs", 
"location": {
    "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
  }
}"""

file_to_work = json.loads(file_json)
file_to_work2 = json.loads(file_json2)
# print(file)


class ColorizeMixin:

    """
    Change the color of console output
    """

    def __init__(self, code):
        self.code = code
        print(f'\033[1;{self.code};40m')


class Location:

    """
    Works with location-attribute
    """

    def __init__(self, file):
        self.file = file
        for key in self.file:
            if key == 'location':
                for k in self.file['location']:
                    self.__setattr__(k, self.file['location'][k])


class Advert(ColorizeMixin):

    """
    Works with json-file, return attributes, including location-attribute
    """

    __repr_color_code__ = 33
    color = ColorizeMixin(__repr_color_code__)

    def __init__(self, file):
        self.file = file
        for key in self.file:
            if key == 'class':
                self.__setattr__('class_', self.file[key])
            elif key != 'price':
                self.__setattr__(key, self.file[key])
        self.location = Location(file)  # композиция

        self.price = 0
        if 'price' in self.file:
            if self.file['price'] < 0:
                print('ValueError: must be >= 0')
            else:
                self.price = self.file['price']

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


# ниже идут тесты вывода

ad = Advert(file_to_work)
# print(ad.title)
# print(ad)  # возвращает return из __repr__
# print(ad.location.address)  # печатает атрибуты location (address, metro_stations)

corgi = Advert(file_to_work2)
print(corgi.class_)
print(corgi)
