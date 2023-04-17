from pongapp.figura_class import Pelota,Raqueta

#objetoRaqueta = Raqueta(0,500)
"""
print("arriba",objetoRaqueta.arriba)
print("abajo",objetoRaqueta.abajo)
print("izquierda",objetoRaqueta.izquierda)
print("derecha",objetoRaqueta.derecha)
"""
"""
def datosPersonales(*paramentros):
    for datos in paramentros:
        print(datos)

datosPersonales("Jose","Perez",25,[1,2,3,4],True,False)
"""
"""
def mover_mano()->str:
    #return "izquierda"
    return "derecha"
valor = mover_mano()

if valor == "izquierda":
    print("Es zurdo")
else:
    print("Es derecho")
"""

"""
def nombres(apellido):
    return "Jose Carlos " + apellido 


def apellidos(apellidos):
    return apellidos


nombre_apellido = nombres(apellidos("Perez Chavez"))
print(nombre_apellido)
"""
"""
class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    def getNombreApellido(self):
        return self.nombre + self.apellido


class Alumno:
    def __init__(self,matricula):
        self.matricula = matricula
        self.nombreApellido=""
        
    def cargarNombreApellido(self,nombreApellido):
        self.nombreApellido = nombreApellido
        print(self.nombreApellido + self.matricula)

persona = Persona("Ramon","Llanes")

alumno = Alumno("X2124545V")
alumno.cargarNombreApellido(persona.getNombreApellido())
"""

lista_coches=["alfa","mercedes","bmw","kia"]

for i in lista_coches:
    print(i)

for i in range(0,len(lista_coches)):
    if i < len(lista_coches)-1:
        if lista_coches[i] != lista_coches[i+1]:
            print("son distintos")   







