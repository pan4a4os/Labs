import abc


class Building(abc.ABC):
    __slots__ = ("_area",)

    @property
    def area(self) -> int | float:
        return self._area


class Penthouse(Building):
    def __init__(self) -> None:
        self._area = 250


class Hostel(Building):
    def __init__(self) -> None:
        self._area = 745


class PrivateHouse(Building):
    def __init__(self) -> None:
        self._area = 225.5


class CarFactory:
    @staticmethod
    def create(building_name: str) -> Building:
        match building_name:
            case "Penthouse":
                return Penthouse()
            case "Hostel":
                return Hostel()
            case "PrivateHouse":
                return PrivateHouse()
            case _:
                raise Exception("The building with that name does not exist.")


if __name__ == "__main__":
    for build in ("Penthouse", "Hostel", "PrivateHouse"):
        building: Building = CarFactory.create(building_name=build)
        print(f"Area of {building.__class__.__name__} is {building.area}")
