class Vector2D:
    _counter = 0

    def __init__(self, x=2, y=5):
        self._x = x
        self._y = y
        Vector2D._counter += 1

    @staticmethod
    def get_counter():
        return Vector2D._counter

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def to_string(self):
        return f"X = {self._x} and Y = {self._y}"

    def equals(self, other):
        return self._x == other.get_x() and self._y == other.get_y()

    def norm(self):
        return (self._x ** 2 + self._y ** 2) ** 0.5


class Vector3D(Vector2D):
    def __init__(self, x=2, y=5, z=1):
        super().__init__(x, y)
        self._z = z
        
    def get_z(self):
        return self._z

    def set_z(self, z):
        self._z = z

    def to_string(self):
        return f"{super().to_string()} and Z = {self._z}"

    def equals(self, other):
        return super().equals(other) and self._z == other.get_z()

    def norm(self):
        return (self.get_x() ** 2 + self.get_y() ** 2 + self._z ** 2) ** 0.5
