from abc import ABC, abstractmethod


class ComputerColor(ABC):
    @classmethod
    @abstractmethod
    def __repr__(self):
        pass

    @classmethod
    @abstractmethod
    def __mul__(self, other):
        pass

    @classmethod
    @abstractmethod
    def __rmul__(self, other):
        pass


class Color(ComputerColor):
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, red_level, green_level, blue_level):
        self.red_level = red_level
        self.green_level = green_level
        self.blue_level = blue_level

    def __str__(self):
        return (f'{self.START};{self.red_level};{self.green_level};{self.blue_level}{self.MOD}●{self.END}{self.MOD}')

    __repr__ = __str__

    def __eq__(self, other):
        if not isinstance(other, Color):
            return False
        else:
            return self.red_level == other.red_level and \
                self.green_level == other.green_level and \
                self.blue_level == other.blue_level

    def __add__(self, other):
        if not isinstance(other, Color):
            raise ValueError('Складываем только цвета')
        return Color(min(self.red_level + other.red_level, 255),
                     min(self.green_level + other.green_level, 255),
                     min(self.blue_level + other.blue_level, 255))

    def __mul__(self, c):
        if c < 0 or c > 1:
            raise ValueError('Число от 0 до 1')
        cl = -256*(1-c)
        F = (259*(cl+255))/(255*(259-cl))
        return Color(int(F*(self.red_level - 128) + 128),
                     int(F*(self.blue_level - 128) + 128),
                     int(F*(self.blue_level - 128) + 128))

    __rmul__ = __mul__

    def __hash__(self):
        return hash((self.red_level, self.green_level, self.blue_level))


if __name__ == '__main__':
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    green1 = Color(0, 255, 0)
    aa = [red, green]
    print(0.5*red)
    print(set(aa))
