class Trapecio:
    def __init__(self, baseMayor: float = 0, baseMenor: float = 0, altura: float = 0,
                 lado1: float = 0, lado2: float =0):
        self.baseMayor = baseMayor
        self.baseMenor = baseMenor
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def calculoArea(self) -> float:
        return ((self.baseMayor +self.baseMenor) * self.altura) / 2

    def calculoPerimetro(self) -> float:
        return self.baseMayor + self.baseMenor + self.lado1 + self.lado2