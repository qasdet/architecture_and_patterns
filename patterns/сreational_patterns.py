from copy import deepcopy
from quopri import decodestring


# абстрактный пользователь
class User:
    pass


# цветок
class Flower(User):
    pass


class UserFactory:
    types = {
        'flower': Flower
    }

    # порождающий паттерн Фабричный метод
    @classmethod
    def create(cls, type_):
        return cls.types[type_]()


# порождающий паттерн Прототип
class BouquetPrototype:
    # прототип букетов

    def clone(self):
        return deepcopy(self)


class Bouquet(BouquetPrototype):

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.category.bouquets.append(self)


# интерактивный букет
class InteractiveBouquet(Bouquet):
    pass


# букет в записи
class RecordBouquet(Bouquet):
    pass


class BouquetFactory:
    types = {
        'interactive': InteractiveBouquet,
        'record': RecordBouquet
    }

    # порождающий паттерн Фабричный метод
    @classmethod
    def create(cls, type_, name, category):
        return cls.types[type_](name, category)


# категория
class Category:
    auto_id = 0

    def __init__(self, name, category):
        self.id = Category.auto_id
        Category.auto_id += 1
        self.name = name
        self.category = category
        self.bouquets = []

    def bouquet_count(self):
        result = len(self.bouquets)
        if self.category:
            result += self.category.bouquet_count()
        return result


# основной интерфейс проекта
class Engine:
    def __init__(self):
        self.flowers = []
        self.bouquets = []
        self.categories = []

    @staticmethod
    def create_user(type_):
        return UserFactory.create(type_)

    @staticmethod
    def create_category(name, category=None):
        return Category(name, category)

    def find_category_by_id(self, id):
        for item in self.categories:
            print('item', item.id)
            if item.id == id:
                return item
        raise Exception(f'Нет категории с id = {id}')

    @staticmethod
    def create_bouquet(type_, name, category):
        return BouquetFactory.create(type_, name, category)

    def get_bouquet(self, name):
        for item in self.bouquets:
            if item.name == name:
                return item
        return None

    @staticmethod
    def decode_value(val):
        val_b = bytes(val.replace('%', '=').replace("+", " "), 'UTF-8')
        val_decode_str = decodestring(val_b)
        return val_decode_str.decode('UTF-8')


# порождающий паттерн Синглтон
class SingletonByName(type):

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = {}

    def __call__(cls, *args, **kwargs):
        if args:
            name = args[0]
        if kwargs:
            name = kwargs['name']

        if name in cls.__instance:
            return cls.__instance[name]
        else:
            cls.__instance[name] = super().__call__(*args, **kwargs)
            return cls.__instance[name]


class Logger(metaclass=SingletonByName):

    def __init__(self, name):
        self.name = name

    @staticmethod
    def log(text):
        print('log--->', text)
