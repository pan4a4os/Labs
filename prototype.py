from copy import copy
from typing import Any


class Prototype:
    __slots__ = ("_type", "_value")

    @property
    def type(self) -> str | None:
        return self._type

    @property
    def value(self) -> Any:
        return self._value

    def clone(self):
        raise NotImplementedError()


class Circle(Prototype):
    __slots__ = ("_type", "_value")

    def __init__(self, diameter: int):
        self._type: str = self.__class__.__name__
        self._value: int = diameter

    def clone(self):
        return copy(x=self)


class Square(Prototype):
    __slots__ = ("_type", "_value")

    def __init__(self, area: str):
        self._type: str = self.__class__.__name__
        self._value: str = area

    def clone(self):
        return copy(x=self)


class ShapeFactory:
    __slots__ = ("__circle", "__square")

    @staticmethod
    def initialize():
        ShapeFactory.__circle = Circle(diameter=10)
        ShapeFactory.__square = Square(area="25 centimeters")

    @staticmethod
    def get_circle() -> Circle:
        return ShapeFactory.__circle.clone()

    @staticmethod
    def get_square() -> Square:
        return ShapeFactory.__square.clone()


def main() -> None:
    ShapeFactory.initialize()

    circle_shape: Circle = ShapeFactory.get_circle()
    square_shape: Square = ShapeFactory.get_square()
    print(f"{circle_shape.type = }, {circle_shape.value = }")
    print(f"{square_shape.type = }, {square_shape.value = }")


if __name__ == "__main__":
    main()
