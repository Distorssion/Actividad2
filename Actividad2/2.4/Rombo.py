class Rombo:
    def __init__(self, diagMay: float = 0, diagMen: float = 0, lado: float = 0):
        self.lado = lado
        self.diagMay = diagMay
        self.diagMen = diagMen
    def calculoArea(self)->float:
        return (self.diagMay * self.diagMen)/2
    def calculoPerimetro(self)->float:
        return self.lado*4