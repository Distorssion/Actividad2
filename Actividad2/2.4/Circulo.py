import math
class Circulo:
    def __init__(self, radio: int = 0):
        self.radio = radio
    def calculoArea(self)->float:
        return math.pi * math.pow(self.radio,2)
    def calculoPerimetro(self)->float:
        return 2*math.pi*self.radio