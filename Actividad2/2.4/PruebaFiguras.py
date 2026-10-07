# Ejercicio figuras pag. 86

from Cuadrado import Cuadrado
from TrianguloRectangulo import TrianguloRectangulo
from Circulo import Circulo
from Rectangulo import Rectangulo
from Rombo import Rombo
from Trapecio import Trapecio

class PruebaFiguras:
    def main():
        fig1 = Circulo(2)
        fig2 = Rectangulo(1,2)
        fig3 = Cuadrado(3)
        fig4 = TrianguloRectangulo(3,5)
        fig5 = Rombo(6,4,3.6)
        fig6 = Trapecio(8, 4, 3, 3.6, 3.6)


        print("El area del circulo es:", fig1.calculoArea())
        print("El perimetro del circulo es:", fig1.calculoPerimetro())
        print("-----")
        print("El area del rectangulo es:", fig2.calculoArea())
        print("El perimetro del rectangulo es:", fig2.calculoPerimetro())
        print("-----")
        print("El area del cuadrado es:", fig3.calculoArea())
        print("El perimetro del cuadrado es:", fig3.calculoPerimetro())
        print("-----")
        print("El area del triangulo es:",fig4.calculoArea())
        print("El perimetro del triangulo es:", fig4.calculoPerimetro())
        print("La hipotenusa del triangulo es:", fig4.calculoHipotenusa())
        fig4.detTipTriangulo()
        print("-----")
        print("El area del rombo es:", fig5.calculoArea())
        print("El perimetro del rombo es:", fig5.calculoPerimetro())
        print("-----")
        print("El area del trapecio es:", fig6.calculoArea())
        print("El perimetro del trapecio es:", fig6.calculoPerimetro())
        
    if __name__ == "__main__":
        main()



        