# Ejercicio 2.5 pagina 95

from tipoCuenta import tipoCuenta
class CuentaBancaria:
    def __init__(self, nombresTitular: str = None, apellTitular: str = None,
                 numCuenta:int = 0, tCuenta: tipoCuenta = None, pInteresMensual: float = 0):
        self.nombresTitular = nombresTitular
        self.apellTitular = apellTitular
        self.numCuenta = numCuenta
        self.tCuenta = tCuenta
        self.saldo = 0
        self.pInteresMensual = pInteresMensual

    def imprimir(self):
        print("Nombres del titular:", self.nombresTitular)
        print("Apellidos del titular:", self.apellTitular)
        print("Numero de cuenta:", self.numCuenta)
        print("Tipo de cuenta:", self.tCuenta.value)
        print("Saldo: $", self.saldo)
        print("El Interes mensual es del:", self.pInteresMensual, "%")

    def consultarSaldo(self):
        print("El saldo actual es:", self.saldo)

    def consignar(self, valor: int)->bool:
        if valor > 0:
            self.saldo = self.saldo + valor
            print("Se ha consignado: $", valor, " en la cuenta. El nuevo saldo es: $", self.saldo)
            return True
        else:
            print("El valor a consignr debe ser mayor que cero")
            return False
    def retirar(self, valor: int)->bool:
        if (valor>0) and (valor <= self.saldo):
            self.saldo = self.saldo - valor
            print("Se ha retirado: $", valor, " en la cuenta. El nuevo saldo es: $", self.saldo)
            return True
        else:
            print("El valor a retirar debe ser menor o igual al saldo actual")
            return False
    def calculoSaldoInteres(self)->float:
        self.saldo = ((self.pInteresMensual / 100) * self.saldo) + self.saldo
        print("Con un interes mensual del", self.pInteresMensual, "%, el nuevo saldo es de:", self.saldo)
        return self.saldo
        

def main():
    cuenta1 = CuentaBancaria("Pedro","Perez",123456789, tipoCuenta.ahorros, 1)
    cuenta1.imprimir()
    cuenta1.consignar(2000000)
    cuenta1.consignar(3000000)
    cuenta1.consignar(-20000)
    cuenta1.retirar(999999999)
    cuenta1.retirar(200000)
    cuenta1.retirar(4800000)
    cuenta1.calculoSaldoInteres()
    cuenta1.consignar(200000)
    cuenta1.calculoSaldoInteres()
    
if __name__ == "__main__":
    main()
                       