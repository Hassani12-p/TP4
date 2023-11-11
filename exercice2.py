class Batiment:
    def __init__(self, adresse):
        self._adresse = adresse

    def get_adresse(self):
        return self._adresse

    def set_adresse(self, value):
        self._adresse = value

    def __str__(self):
        return f"Batiment - Adresse : {self.get_adresse()}"


class Maison(Batiment):
    def __init__(self, adresse, nbPieces):
        super().__init__(adresse)
        self._nbPieces = nbPieces

    def get_nbPieces(self):
        return self._nbPieces

    def set_nbPieces(self, value):
        self._nbPieces = value

    def __str__(self):
        return f"Maison - Adresse : {self.get_adresse()}, Nombre de pièces : {self.get_nbPieces()}"


class Immeuble(Batiment):
    def __init__(self, adresse, nbAppart):
        super().__init__(adresse)
        self._nbAppart = nbAppart

    def get_nbAppart(self):
        return self._nbAppart

    def set_nbAppart(self, value):
        self._nbAppart = value

    def __str__(self):
        return f"Immeuble - Adresse : {self.get_adresse()}, Nombre d'appartements : {self.get_nbAppart()}"



batiment = Batiment("QR 12 ,AIN EL ATY 2")
print(batiment)

maison = Maison("RUE TARGA ", 2)
print(maison)

immeuble = Immeuble("AIN EL ATY 2", 10)
print(immeuble)
