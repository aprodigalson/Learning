

'''
    用python实现一个简单的对象模型
    a simple object model
    linked :https://manjusaka.itscoder.com/2016/12/15/A-Simple-Object-Model/

'''


def _is_bindable(method):
    return hasattr(method, "__get__")
    # return callable(method)


def _make_boundmethod(method, self):
    return method.__get__(self, None)


class Map(object):
    def __init__(self, attrs):
        self.attrs = attrs
        self.next_maps = {}

    def get_index(self, field_name):
        return self.attrs.get(field_name, -1)

    def next_map(self, field_name):
        assert field_name not in self.attrs
        if field_name in self.next_maps:
            return self.next_maps[field_name]
        attrs = self.attrs.copy()
        attrs[field_name] = len(attrs)
        result = self.next_maps[field_name] = Map(attrs)
        return result


EMPTY_MAP = Map({})


class Base(object):
    def __init__(self, cls, fields):
        self.cls = cls
        self._fields = fields

    def read_attr(self, field_name):
        result = self._read_dict(field_name)
        if result is not MISSING:
            return result
        result = self.cls._read_from_class(field_name)
        if _is_bindable(result):
            return _make_boundmethod(result, self)
        if result is not MISSING:
            return result
        method = self.cls._read_from_class("__getattr__")
        if method is not MISSING:
            return method(self, field_name)
        raise AttributeError(field_name)

    def write_attr(self, field_name, value):
        # self._write_dict(field_name, value)
        method = self.cls._read_from_class("__setattr__")
        return method(self, field_name, value)

    def isinstance(self, cls):
        return self.cls.issubclass(cls)

    def callmethod(self, method_name, *args):
        method = self.cls._read_from_class(method_name)
        return method(self, *args)

    def _read_dict(self, field_name):
        return self._fields.get(field_name, MISSING)

    def _write_dict(self, field_name, value):
        self._fields[field_name] = value


MISSING = object()


class Class(Base):
    def __init__(self, name, base_class, fields, metaclass):
        Base.__init__(self, metaclass, fields)
        self.base_class = base_class

    def method_resolution_order(self):
        if self.base_class is None:
            return [self]
        else:
            return [self] + self.base_class.method_resolution_order()

    def issubclass(self, cls):
        return cls in self.method_resolution_order()

    def _read_from_class(self, method_name):
        for cls in self.method_resolution_order():
            if method_name in cls._fields:
                return cls._fields[method_name]
        return MISSING


class Instance(Base):
    def __init__(self, cls):
        assert isinstance(cls, Class)
        Base.__init__(self, cls, None)
        self.map = EMPTY_MAP
        self.storage = []

    def _read_dict(self, field_name):
        index = self.map.get_index(field_name)
        if index == -1:
            return MISSING
        return self.storage[index]

    def _write_dict(self, field_name, value):
        index = self.map.get_index(field_name)
        if index != -1:
            self.storage[index] = value
        else:
            new_map = self.map.next_map(field_name)
            self.storage.append(value)
            self.map = new_map


def OBJECT__setattr__(self, field_name, value):
    self._write_dict(field_name, value)


OBJECT = Class(name="object", base_class=None, fields={"__setattr__": OBJECT__setattr__}, metaclass=None)
TYPE = Class(name="type", base_class=OBJECT, fields={}, metaclass=None)
TYPE.cls = TYPE
OBJECT.cls = TYPE


def test_get():
    # Python code
    class FahrenheitGetter(object):
        def __get__(self, inst, cls):
            return inst.celsius * 9 / 5 + 32

    class A(object):
        fahrenheit = FahrenheitGetter()

    obj = A()
    obj.celsius = 30
    assert obj.fahrenheit == 86

    # Object model code
    class FahrenheitGetter(object):
        def __get__(self, inst, cls):
            return inst.read_attr("celsius") * 9 / 5 + 32

    A = Class(name="A", base_class=OBJECT,
              fields={"fahrenheit": FahrenheitGetter()},
              metaclass=TYPE)
    obj = Instance(A)
    obj.write_attr("celsius", 30)
    assert obj.read_attr("fahrenheit") == 86


def test_getattr():
    class A(object):
        def __getattr__(self, item):
            if item == "fahrenheit":
                return self.celsius * 9 / 5 + 32
            return AttributeError(item)

        def __setattr__(self, name, value):
            if name == "fahrenheit":
                self.celsius = (value - 32) * 5 / 9
            else:
                object.__setattr__(self, name, value)

    obj = A()
    obj.celsius = 30
    assert obj.fahrenheit == 86
    obj.celsius = 40
    assert obj.fahrenheit == 104

    obj.fahrenheit = 86
    assert obj.celsius == 30
    assert obj.fahrenheit == 86

    def __getattr__(self, name):
        if name == "fahrenheit":
            return self.read_attr("celsius") * 9 / 5 + 32
        return AttributeError(name)

    def __setattr__(self, name, value):
        if name == "fahrenheit":
            self.write_attr("celsius", (value - 32) * 5 / 9)
        else:
            OBJECT.read_attr("__setattr__")(self, name, value)

    A = Class(name="A", base_class=OBJECT, fields={"__getattr__": __getattr__, "__setattr__": __setattr__},
              metaclass=TYPE)
    obj = Instance(A)
    obj.write_attr("celsius", 30)
    assert obj.read_attr("fahrenheit") == 86
    obj.write_attr("celsius", 40)
    assert obj.read_attr("fahrenheit") == 104
    obj.write_attr("fahrenheit", 86)
    assert obj.read_attr("celsius") == 30
    assert obj.read_attr("fahrenheit") == 86


def test_read_write_field():
    class A(object):
        pass

    obj = A()
    obj.a = 1
    assert obj.a == 1
    obj.b = 5
    assert obj.a == 1
    assert obj.b == 5
    obj.a = 2
    assert obj.a == 2
    assert obj.b == 5

    A = Class(name="A", base_class=OBJECT, fields={}, metaclass=TYPE)
    obj = Instance(A)
    obj.write_attr("a", 1)
    assert obj.read_attr("a") == 1
    obj.write_attr("b", 5)
    assert obj.read_attr("a") == 1
    assert obj.read_attr("b") == 5
    obj.write_attr("a", 2)
    assert obj.read_attr("a") == 2
    assert obj.read_attr("b") == 5


def test_read_write_field_class():
    class A(object):
        pass

    A.a = 1
    assert A.a == 1
    A.a = 6
    assert A.a == 6

    A = Class(name="A", base_class=OBJECT, fields={"a": 1}, metaclass=TYPE)
    assert A.read_attr("a") == 1
    A.write_attr("a", 5)
    assert A.read_attr("a") == 5


def test_isinstance():
    class A(object):
        pass

    class B(A):
        pass

    b = B()
    assert isinstance(b, B)
    assert isinstance(b, A)
    assert isinstance(b, object)
    assert not isinstance(b, type)

    A = Class(name="A", base_class=OBJECT, fields={}, metaclass=TYPE)
    B = Class(name="B", base_class=A, fields={}, metaclass=TYPE)
    b = Instance(B)
    assert b.isinstance(B)
    assert b.isinstance(A)
    assert b.isinstance(OBJECT)
    assert not b.isinstance(TYPE)


def test_callmethod_simple():
    class A(object):
        def f(self):
            return self.x + 1

    obj = A()
    obj.x = 1
    assert obj.f() == 2

    class B(A):
        pass

    obj = B()
    obj.x = 1
    assert obj.f() == 2

    def f_A(self):
        return self.read_attr("x") + 1

    A = Class(name="A", base_class=OBJECT, fields={"f": f_A}, metaclass=TYPE)
    obj = Instance(A)
    obj.write_attr("x", 1)
    assert obj.callmethod("f") == 2

    B = Class(name="B", base_class=A, fields={}, metaclass=TYPE)
    obj = Instance(B)
    obj.write_attr("x", 2)
    assert obj.callmethod("f") == 3


def test_callmethod_subclassing_and_arguments():
    class A(object):
        def g(self, arg):
            return self.x + arg

    obj = A()
    obj.x = 1
    assert obj.g(4) == 5

    class B(A):
        def g(self, arg):
            return self.x + arg * 2

    obj = B()
    obj.x = 4
    assert obj.g(4) == 12

    def g_A(self, arg):
        return self.read_attr("x") + arg

    A = Class(name="A", base_class=OBJECT, fields={"g": g_A}, metaclass=TYPE)
    obj = Instance(A)
    obj.write_attr("x", 1)
    assert obj.callmethod("g", 4) == 5

    def g_B(self, arg):
        return self.read_attr("x") + arg * 2

    B = Class(name="B", base_class=A, fields={"g": g_B}, metaclass=TYPE)
    obj = Instance(B)
    obj.write_attr("x", 4)
    assert obj.callmethod("g", 4) == 12


def test_bound_method():
    # Python code
    class A(object):
        def f(self, a):
            return self.x + a + 1

    obj = A()
    obj.x = 2
    m = obj.f
    assert m(4) == 7

    class B(A):
        pass

    obj = B()
    obj.x = 1
    m = obj.f
    assert m(10) == 12  # works on subclass too

    # Object model code
    def f_A(self, a):
        return self.read_attr("x") + a + 1

    A = Class(name="A", base_class=OBJECT, fields={"f": f_A}, metaclass=TYPE)
    obj = Instance(A)
    obj.write_attr("x", 2)
    m = obj.read_attr("f")
    assert m(4) == 7

    B = Class(name="B", base_class=A, fields={}, metaclass=TYPE)
    obj = Instance(B)
    obj.write_attr("x", 1)
    m = obj.read_attr("f")
    assert m(10) == 12


def test_maps():
    # white box test inspecting the implementation
    Point = Class(name="Point", base_class=OBJECT, fields={}, metaclass=TYPE)
    p1 = Instance(Point)
    p1.write_attr("x", 1)
    p1.write_attr("y", 2)
    assert p1.storage == [1, 2]
    assert p1.map.attrs == {"x": 0, "y": 1}

    p2 = Instance(Point)
    p2.write_attr("x", 5)
    p2.write_attr("y", 6)
    assert p1.map is p2.map
    assert p2.storage == [5, 6]

    p1.write_attr("x", -1)
    p1.write_attr("y", -2)
    assert p1.map is p2.map
    assert p1.storage == [-1, -2]

    p3 = Instance(Point)
    p3.write_attr("x", 100)
    p3.write_attr("z", -343)
    assert p3.map is not p1.map
    assert p3.map.attrs == {"x": 0, "z": 1}


test_read_write_field()
test_read_write_field_class()
test_isinstance()
test_callmethod_simple()
test_callmethod_subclassing_and_arguments()
test_bound_method()
test_getattr()
test_get()
