# Eejercicio 2.3 automovil pag. 73

from tipoCom import tipoCom
from tipoA import tipoA
from tipoColor import tipoColor

class Automovil:
    def __init__(self, marca: str = None, modelo: int = 0, motor: int = 0,
                 combustibleTipo: tipoCom = None, tipoAutomovil: tipoA = None, 
                 nPuertas: int = 0, nAsientos: int = 0, velMax: int = 0,
                 color: tipoColor =  None, automatico: bool = False):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.combustibleTipo = combustibleTipo
        self.tipoAutomovil = tipoAutomovil
        self.nPuertas = nPuertas
        self.nAsientos = nAsientos
        self.velMax = velMax
        self.color = color
        self.vActual = 0
        self.automatico = automatico
        self.multas = 0
    #getters
    def getMarca(self)->str:
        return self.marca
    def getModelo(self)->int:
            return self.modelo
    def getMotor(self)->int:
            return self.motor
    def getCombustibletipo(self)->tipoCom:
            return self.combustibleTipo
    def getTipoAutomovil(self)->tipoA:
            return self.tipoAutomovil
    def getnPuertas(self)->int:
            return self.nPuertas
    def getnAsientos(self)->int:
            return self.nAsientos
    def getvMax(self)->int:
            return self.velMax
    def getColor(self)->tipoColor:
            return self.color
    def getvActual(self)->int:
           return self.vActual
    def getAutom(self)->bool:
          return self.automatico
    def getMultas(self)->int:
          return self.multas

    #setters
    def setAutom(self, automatico:bool):
          self.automatico = automatico
    def setMarca(self, marca:str):
           self.marca = marca
    def setModelo(self, modelo:int):
           self.modelo = modelo
    def setMotor(self, motor: int):
           self.motor = motor
    def setCombustibleTipo(self, combustibleTipo: tipoCom):
           self.combustibleTipo = combustibleTipo
    def settipoAutomovil (self, tipoAutomovil: tipoA):
           self.tipoAutomovil = tipoAutomovil
    def setnPuertas (self, nPuertas: int):
           self.nPuertas = nPuertas
    def setnAsientos (self, nAsientos: int):
           self.nAsientos = nAsientos
    def setvMax (self, vMax: int):
           self.velMax = vMax
    def setColor (self, color: tipoColor):
           self.color = color
    def setvActual (self, vActual: int):
           self.vActual = vActual


    def acelerar(self, incrementoVelocidad: int):
           if self.vActual + incrementoVelocidad <= self.velMax:
                  self.vActual = self.vActual + incrementoVelocidad 
           else:
            print("No se puede incrementar a una velocidad superior a la máxima del automóvil," \
            " se ha generado una multa")
            self.multas = self.multas + 1

    def desacelerar (self, decrementoVelocidad: int):
           if self.vActual  - decrementoVelocidad >=0:
                  self.vActual = self.vActual - decrementoVelocidad
           else:
            print ("No se puede decrementar a una velocidad negativa")

    def frenar(self):
           self.vActual = 0

    def calculartLlegada(self, distancia: int) -> float:
        return distancia / self.vActual
    
    def tieneMultas(self)->bool:
          return self.multas > 0

    def imprimir(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Motor:", self.motor)
        print("Tipo de combustible:", self.combustibleTipo.value)
        print("Tipo de automovil:", self.tipoAutomovil.value)
        print("Numero de puertas:", self.nPuertas)
        print("Cantidad de asientos:", self.nAsientos)
        print("Velocidad maxima:", self.velMax)
        print("Color:", self.color.value)
        print("Es automatico:", self.automatico)


def main():
    auto1 = Automovil("Ford", 2018, 3, tipoCom.diesel, tipoA.ejecutivo,
                      5, 6, 250, tipoColor.negro,True)
    auto1.imprimir()

    auto1.setvActual(100)
    print("Velocidad actual:", auto1.getvActual())
    auto1.acelerar(20)
    print("Velocidad actual:", auto1.getvActual())
    auto1.desacelerar(50)
    print("Velocidad actual:", auto1.getvActual())
    auto1.frenar()
    print("Velocidad actual:", auto1.getvActual())
    auto1.desacelerar(20)  
    print("Tiene multas?", auto1.tieneMultas())
    print("Cantidad de multas:", auto1.getMultas())
    #caso 2 con nuevos parametros

    auto1.setvActual(150)
    print("Velocidad actual:", auto1.getvActual())
    auto1.acelerar(101)
    print("Velocidad actual:", auto1.getvActual())
    print("Tiene multas?", auto1.tieneMultas())
    print("Cantidad de multas:", auto1.getMultas())

    auto1.acelerar(120)
    print("Velocidad actual:", auto1.getvActual())
    print("Tiene multas?", auto1.tieneMultas())
    print("Cantidad de multas:", auto1.getMultas())


if __name__ == "__main__":
    main()
                       
            
               