from abc import ABC, abstractmethod
import random


# Completar
class Persona(ABC):

    def __init__(self, nombre="", edad=0, contagiado=0):
        # No modificar
        self.nombre = nombre
        self.edad = edad
        self.contagiado = contagiado

    @abstractmethod
    def saludar(self):
        pass

# Completar
class Cliente(Persona):

    def __init__(self,nombre_local_favorito = "", dinero = 0 , **kwargs):
        # Completar
        super().__init__(**kwargs)
        self.nombre_local_favorito = nombre_local_favorito
        self.dinero = dinero
        pass

    def saludar(self):
        # No modificar
        print(f"Hola me llamo {self.nombre} y mi local favorito es {self.nombre_local_favorito}")


# Completar
class Trabajador(Persona):

    def __init__(self, sueldo = 0, nombre_local = "", **kwargs):
        # Completar
        super().__init__(**kwargs)
        self.sueldo = sueldo
        self.nombre_local = nombre_local
        ##llamar metodo saludar???
        pass

    def generar_posible_contagio(self):
        # No modificar
        probabilidad_contagio = random.uniform(0, 1)
        if probabilidad_contagio < 0.1:
            self.contagiado = True

    def saludar(self):
        # No modificar
        print((
            f"Hola me llamo {self.nombre}, trabajo en {self.nombre_local}"
            f" y mi sueldo es {self.sueldo}"
        ))
