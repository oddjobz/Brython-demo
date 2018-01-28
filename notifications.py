from browser import window


class Notifications:

    def __init__(self, title=None, text=None, theme='bootstrap3', styling='fontawesome'):
        window.PNotify.prototype.options.styling = theme
        window.PNotify.prototype.options.styling = styling
        window.PNotify.new({
            'title': title,
            'text': text,
            'type': self.__class__.__name__.lower()
        })


class Notice(Notifications):
    pass


class Info(Notifications):
    pass


class Success(Notifications):
    pass


class Error(Notifications):
    pass

