class persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

class coleccion_de_objetos:
    lista_alumno= []
    lista_alumno.append(persona("Valentin", "Beron", "22"))

    def mostrar_lista(self):
        for x in self.lista:
            print(x.nombre, x.apellido, x.edad)

curso=coleccion_de_objetos()
curso.mostrar_lista()