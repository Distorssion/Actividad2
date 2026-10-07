import math

class TrianguloRectangulo:
    def __init__(self, base: int = 0, altura: int = 0):
        self.base = base
        self.altura = altura
    
    def calculoArea(self)->float:
        return(self.base*self.altura)/2
    
    def calculoHipotenusa(self)->float:
        return math.pow(self.base*self.base+self.altura*self.altura, 0.5)
    
    def calculoPerimetro(self)->float:
        return self.base+self.altura+self.calculoHipotenusa()

    def detTipTriangulo(self):
        if self.base == self.altura and self.base == self.calculoHipotenusa() and self.altura == self.calculoHipotenusa():
            print("El triangulo es equilatero")
        elif self.base != self.altura and self.base != self.calculoHipotenusa() and self.altura != self.calculoHipotenusa():
            print("El triangulo es escaleno")
        else:
            print("El triangulo es isosceles")