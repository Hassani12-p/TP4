class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

    def __str__(self):
        return f"Point({self._x}, {self._y})"


class Rectangle(Point):
    def __init__(self, x, y, longueur, largeur):
        super().__init__(x, y)
        self._longueur = longueur
        self._largeur = largeur

    def get_longueur(self):
        return self._longueur

    def set_longueur(self, longueur):
        self._longueur = longueur

    def get_largeur(self):
        return self._largeur

    def set_largeur(self, largeur):
        self._largeur = largeur

    def aire(self):
        return self._longueur * self._largeur

    def __str__(self):
        return f"Rectangle({super().get_x()}, {super().get_y()}, {self._longueur}, {self._largeur})"


class Parallelepipede(Rectangle):
    def __init__(self, x, y, longueur, largeur, hauteur):
        super().__init__(x, y, longueur, largeur)
        self._hauteur = hauteur

    def get_hauteur(self):
        return self._hauteur

    def set_hauteur(self, hauteur):
        self._hauteur = hauteur

    def aire(self):
        return 2 * (self._longueur * self._largeur + self._longueur * self._hauteur + self._largeur * self._hauteur)

    def volume(self):
        return self._longueur * self._largeur * self._hauteur

    def __str__(self):
        return f"Parallelepipede({super().get_x()}, {super().get_y()}, {self._longueur}, {self._largeur}, {self._hauteur})"


point = Point(4, 2)
print(point)

rectangle = Rectangle(4, 7, 3, 5)
print(rectangle)
print("Aire du rectangle:", rectangle.aire())

parallelepipede = Parallelepipede(2, 2, 8, 4, 1)
print(parallelepipede)
print("Aire du parallelepipede:", parallelepipede.aire())
print("Volume du parallelepipede:", parallelepipede.volume())
