class Foo:
    def __init__(self, x= None) :
        self._x = x

    @property
    def x (self):
        return self._x or 0
    
    @x.setter
    def x (self,valor):
        _x = self._x or 0
        _valor = valor or 0
        self._x = _x + _valor

    @x.deleter
    def x (self):
        self._x = -1

f = Foo(50)
print(f.x)
f.x = 10
print(f.x)
del f.x
print(f.x)