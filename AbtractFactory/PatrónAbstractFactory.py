from abc import ABC, abstractmethod  # Importa clases para crear interfaces abstractas


# Abstract Product

class Institucion(ABC):  # Clase abstracta que define una institución
    def __init__(self, nombre, presupuesto):
        self.nombre = nombre  # Nombre de la institución
        self.presupuesto = presupuesto  # Presupuesto de la institución

    @abstractmethod
    def describir(self):  # Método que debe ser implementado por las subclases
        pass


# Concrete Products

class InstitucionPublica(Institucion):  # Implementación concreta de una institución pública
    def describir(self):
        # Devuelve una descripción específica para instituciones públicas
        return f"[PÚBLICA] {self.nombre} - Presupuesto estatal: ${self.presupuesto} millones"

class InstitucionPrivada(Institucion):  # Implementación concreta de una institución privada
    def describir(self):
        # Devuelve una descripción específica para instituciones privadas
        return f"[PRIVADA] {self.nombre} - Presupuesto propio: ${self.presupuesto} millones"


# Abstract Factory

class FabricaInstitucion(ABC):  # Interfaz abstracta para la fábrica de instituciones
    @abstractmethod
    def crear_institucion(self, nombre, presupuesto):  # Método a implementar por cada fábrica concreta
        pass


# Concrete Factories

class FabricaPublica(FabricaInstitucion):  # Fábrica concreta para instituciones públicas
    def crear_institucion(self, nombre, presupuesto):
        return InstitucionPublica(nombre, presupuesto)  # Crea y retorna una institución pública

class FabricaPrivada(FabricaInstitucion):  # Fábrica concreta para instituciones privadas
    def crear_institucion(self, nombre, presupuesto):
        return InstitucionPrivada(nombre, presupuesto)  # Crea y retorna una institución privada


# Menú Interactivo

def menu():
    instituciones = []  # Lista para almacenar las instituciones creadas

    while True:
        # Muestra el menú de opciones
        print("\n--- Registro de Instituciones ---")
        print("1. Crear institución pública")
        print("2. Crear institución privada")
        print("3. Ver instituciones registradas")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")  # Captura la opción del usuario

        if opcion == "1":
            # Crear institución pública
            nombre = input("Nombre de la institución pública: ")
            presupuesto = input("Presupuesto en millones: ")
            fabrica = FabricaPublica()  # Usa la fábrica pública
            institucion = fabrica.crear_institucion(nombre, presupuesto)  # Crea la instancia
            instituciones.append(institucion)  # Agrega a la lista
            print("✅ Institución pública creada con éxito.")

        elif opcion == "2":
            # Crear institución privada
            nombre = input("Nombre de la institución privada: ")
            presupuesto = input("Presupuesto en millones: ")
            fabrica = FabricaPrivada()  # Usa la fábrica privada
            institucion = fabrica.crear_institucion(nombre, presupuesto)  # Crea la instancia
            instituciones.append(institucion)  # Agrega a la lista
            print("✅ Institución privada creada con éxito.")

        elif opcion == "3":
            # Mostrar instituciones registradas
            print("\n📋 Instituciones registradas:")
            if not instituciones:
                print("No hay instituciones aún.")
            else:
                for i, inst in enumerate(instituciones, 1):  # Muestra todas con su descripción
                    print(f"{i}. {inst.describir()}")

        elif opcion == "4":
            # Salir del programa
            print("👋 Saliendo del programa.")
            break

        else:
            # Opción inválida
            print("⚠️ Opción inválida. Intenta de nuevo.")

# Punto de entrada

if __name__ == "__main__":
    menu()  # Llama a la función del menú si se ejecuta directamente el script
