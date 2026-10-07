class Cuadrado:
    def __init__(self, lado: int = 0):
        self.lado = lado
    def calculoArea(self)->int:
        return self.lado*self.lado
    def calculoPerimetro(self)->float:
        return 4*self.lado