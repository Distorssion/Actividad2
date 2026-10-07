
class Rectangulo:
    def __init__(self, base: int = 0, altura: int = 0):
        self.base = base
        self.altura = altura
    def calculoArea(self)-> float:
        return self.base * self.altura
    def calculoPerimetro(self)->float:
        return (2*self.base)+(2*self.altura)
