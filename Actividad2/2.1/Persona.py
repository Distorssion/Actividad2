# ejercicio 2.1 pag 63 personas

class Persona:

    def __init__(self, nombre: str, apellidos: str, doc_id: str, nac_year, nacimientopais:str, genero:str):
        self.nombre = nombre                                          
        self.apellidos = apellidos                                    
        self.doc_id = doc_id
        self.nac_year = nac_year      
        self.nacimientopais = nacimientopais     

        # genero estricamente H o M
        genero_correcto = str(genero).upper()
        if genero_correcto in ['H', 'M']:
            self.genero = genero_correcto
        else:
            raise ValueError("El genero tiene que ser H o M")

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Apellidos:",self.apellidos)
        print("Documento de identidad:", self.doc_id)
        print("Año de nacimiento:", self.nac_year)
        print("Genero:", self.genero)
        print("Pais de nacimiento:", self.nacimientopais)

def main():
    p1 = Persona("Juan Pablo", "Muñoz", "1020485532", 2000, "Colombia", "H")
    p2 = Persona("Valentina", "Narbatez", "1053223344", 2001, "Chile", "M")

    p1.imprimir()
    print("---")
    p2.imprimir()


if __name__ == "__main__":
    main()