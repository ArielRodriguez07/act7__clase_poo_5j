print("Pogramacion POO")
# Definicion de clase
class perro:
    # funciones dentro de la clase
    nombre="boby"
    edad=4
    def morder(self):
        print("el perro me mordio")
    def Datos_perro(self,nombre,edad):
        print(f" nombre : {nombre} edad: {edad}")


# Zona de creacion de objeto
pitbull=perro()

# zona de uso de objetos
pitbull.Datos_perro("boby",4)
pitbull.morder()