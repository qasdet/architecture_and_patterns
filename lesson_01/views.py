from framework.templator import render


class Index:
    def __call__(self):
        return '200 OK', render('index.html')


class About:
    def __call__(self):
        return '200 OK', render('about.html')
