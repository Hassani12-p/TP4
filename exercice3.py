from abc import ABC, abstractmethod

class Employe(ABC):
    def __init__(self, nom, prenom):
        self._nom = nom
        self._prenom = prenom

    def get_nom(self):
        return self._nom

    def set_nom(self, nom):
        self._nom = nom

    def get_prenom(self):
        return self._prenom

    def set_prenom(self, prenom):
        self._prenom = prenom

    @abstractmethod
    def gains(self):
        pass

    def __str__(self):
        return f"{self._nom}, {self._prenom}"

class Patron(Employe):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom)
        self._salaire = salaire

    def get_salaire(self):
        return self._salaire

    def set_salaire(self, salaire):
        self._salaire = salaire

    def gains(self):
        return self._salaire

    def __str__(self):
        return f"Patron: {super().__str__()}, Salaire: {self._salaire}"

class TravailleurCommission(Employe):
    def __init__(self, nom, prenom, salaire, commission, quantite):
        super().__init__(nom, prenom)
        self._salaire = salaire
        self._commission = commission
        self._quantite = quantite

    def get_salaire(self):
        return self._salaire

    def set_salaire(self, salaire):
        self._salaire = salaire

    def get_commission(self):
        return self._commission

    def set_commission(self, commission):
        self._commission = commission

    def get_quantite(self):
        return self._quantite

    def set_quantite(self, quantite):
        self._quantite = quantite

    def gains(self):
        return self._salaire + (self._commission * self._quantite)

    def __str__(self):
        return f"Travailleur à la commission: {super().__str__()}, Salaire: {self._salaire}, Commission: {self._commission}, Quantité: {self._quantite}"

class TravailleurHoraire(Employe):
    def __init__(self, nom, prenom, retribution, heures):
        super().__init__(nom, prenom)
        self._retribution = retribution
        self._heures = heures

    def get_retribution(self):
        return self._retribution

    def set_retribution(self, retribution):
        self._retribution = retribution

    def get_heures(self):
        return self._heures

    def set_heures(self, heures):
        self._heures = heures

    def gains(self):
        return self._retribution * self._heures

    def __str__(self):
        return f"Travailleur horaire: {super().__str__()}, Rémunération horaire: {self._retribution}, Heures de travail: {self._heures}"


employes = [
    Patron("ahmed", "hassani", 20000),
    TravailleurCommission("kamal", "bnany", 6000, 0.1, 200),
    TravailleurHoraire("AMINE", "ALAMI", 50, 24)
]

for employe in employes:
    print(employe)
    print("Gains:", employe.gains())
    
