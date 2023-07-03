from time import time

routes = {}


# структурный паттерн - Декоратор
class AppRoute:
    def __init__(self, url):
        """
        Сохраняем значение переданного параметра
        """
        self.url = url

    def __call__(self, cls):
        """
        Сам декоратор
        """
        routes[self.url] = cls()
        pass


# структурный паттерн - Декоратор
class Debug:

    def __init__(self, name):

        self.name = name

    def __call__(self, cls):
        """
        Сам декоратор
        """

        # Это вспомогательная функция будет декорировать каждый отдельный метод класса, см. ниже
        def timeit(method):
            """
            Нужен для того, чтобы декоратор класса wrapper обернул в timeit
            каждый метод декорируемого класса
            """
            def timed(*args, **kw):
                ts = time()
                result = method(*args, **kw)
                te = time()
                delta = te - ts

                print(f'debug --> {self.name} выполнялся {delta:2.2f} ms')
                return result

            return timed

        return timeit(cls)
