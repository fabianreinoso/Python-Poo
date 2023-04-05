class Persona:
    
    def __init__(self, nom):
        self.nombre = nom 
    
    def mostrar(self):
        print("Nombre  : " + self.nombre)

class Alumno(Persona):
    
    def __init__(self, nom, nota):
        super().__init__(nom)
        self.nota = nota 

    def mostrar(self):
        print("=======================")
        print(""" Datos del Alumno """)
        print("=======================")
        super().mostrar()
        print("Nota : " + str(self.nota))
        print("=======================")


class Profesor(Persona):
    pass


alumno1 = Alumno('Fabian Ramirez', 20)
alumno1.mostrar()
profesor1 = Profesor('Alfredo Saire')
profesor1.mostrar()