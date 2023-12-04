class socio:
    def __init__(self, nombre, antiguedad):
        self.nombre = input("Ingrese el nombre del socio: ")
        self.antiguedad = int(input("Ingrese la antiguedad del socio: "))

class club_socios:
    lista_socios= []
    
    def agregar_socio(self): #metodo para agregar un nuevo socio
        nuevo_socio = socio()
        self.lista_socios.append(nuevo_socio)

    def mostrar_lista(self): #metodo para mostrar la lista de socios
        for x in self.lista_socios:
            print(f"Nombre: {x.nombre}, Años: {x.antiguedad}")

curso = club_socios()
curso.agregar_socio()
curso.mostrar_lista()

#un banco tiene 3 clientes que pueden hacer depositos y extracciones se requiere que el banco calcule 
# al finalizar el dia la cantidad de dinero que hay deposita y tambien la cantidad de dinero que posee cada cliente