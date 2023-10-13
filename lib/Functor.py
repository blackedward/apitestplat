class Functor(object):
    def __init__(self, func, index=0, *args, **kwargs):
        self._Func = func
        self._Index = index
        self._Args = args
        self._Kwargs = kwargs

    def __call__(self, *args, **kwargs):
        args = args[:self._Index] + self._Args + args[self._Index:]
        kwargs = kwargs.copy()
        kwargs.update(self._Kwargs)
        return self._Func(*args, **kwargs)


def bind(func, index=0, *args, **kwargs):
    return Functor(func, index, *args, **kwargs)