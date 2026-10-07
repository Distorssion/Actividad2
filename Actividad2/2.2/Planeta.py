# Ejercicio 2.2 página 66 planetas

from tipoPlaneta import TipoPlaneta


class Planeta:

    def __init__(self, nombre: str = None, cantidad_satelites: int = 0,
                 masa: float = 0, volumen: float = 0, diametro: int = 0,
                 distanciaSol: int = 0, tipo: TipoPlaneta = None,
                 esObservable: bool = False, periodoOrbital: float = 0, periodoRot: float = 0):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distanciaSol = distanciaSol
        self.tipo = tipo
        self.esObservable = esObservable
        self.periodoOrbital = periodoOrbital
        self.periodoRot = periodoRot

    def imprimir(self):
        print("Nombre del planeta:", self.nombre)
        print("Cantidad de satélites:", self.cantidad_satelites)
        print("Masa del planeta:", self.masa)
        print("Volumen del planeta:", self.volumen)
        print("Diametro del planeta:", self.diametro)
        print("Distancia al sol:", self.distanciaSol)
        print("Tipo de planeta:", self.tipo.value)
        print("Es observable:", self.esObservable)
        print("Periodo orbital:", self.periodoOrbital, "años")
        print("Periodo de rotacion:", self.periodoRot, "dias")

    def calcularDensidadp(self) -> float:
        return self.masa/self.volumen

    def esPlanetaexterior(self) -> bool:
        limite = 149597870*3.4
        if (self.distanciaSol>limite):
            return True
        else:
            return False


def main():
    p1 = Planeta("Tierra", 1, 5.9736E24, 1.08321E12, 12742,
                 150000000, TipoPlaneta.TERRESTRE, True, 1, 1)
    p1.imprimir()
    print("Densidad del planeta:", p1.calcularDensidadp())
    print("Es planeta exterior:", p1.esPlanetaexterior())
    print("-------")

    p2 = Planeta("Júpiter", 79, 1.899E27, 1.4313E15, 139820,
                 750000000, TipoPlaneta.GASEOSO, True, 11.86, 0.41)
    p2.imprimir()
    print("Densidad del planeta:", p2.calcularDensidadp())
    print("Es planeta exterior:", p2.esPlanetaexterior())


if __name__ == "__main__":
    main()