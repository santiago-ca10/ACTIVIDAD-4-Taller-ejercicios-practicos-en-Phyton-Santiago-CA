from abc import ABC, abstractmethod  # Se importa herramientas para clases abstractas

# Clase abstracta del observador
class Observador(ABC):
    @abstractmethod
    def actualizar(self, evento):
        pass  # Método que será implementado por los observadores concretos

# Clase concreta del observador
class Participante(Observador):
    def __init__(self, nombre):
        self.nombre = nombre  # Guarda el nombre del participante

    def actualizar(self, evento):
        # Notificación al participante cuando el evento cambia
        print(f"[{self.nombre}] Notificado: El evento '{evento.nombre}' ha sido actualizado.")

# Clase del sujeto (Subject)
class EventoCalendario:
    def __init__(self, nombre, fecha, lugar):
        self.nombre = nombre
        self.fecha = fecha
        self.lugar = lugar
        self.observadores = []  # Lista de participantes (observadores)

    def agregar_observador(self, observador):
        self.observadores.append(observador)  # Añade un observador a la lista

    def quitar_observador(self, observador):
        self.observadores.remove(observador)  # Elimina un observador de la lista

    def notificar(self):
        # Notifica a todos los observadores registrados
        for observador in self.observadores:
            observador.actualizar(self)

    def cambiar_evento(self, nueva_fecha=None, nuevo_lugar=None):
        # Permite actualizar la fecha y/o el lugar del evento
        if nueva_fecha:
            self.fecha = nueva_fecha
        if nuevo_lugar:
            self.lugar = nuevo_lugar
        print(f"\n🔔 Evento '{self.nombre}' actualizado.")
        self.notificar()  # Notifica a los observadores del cambio

    def listar_participantes(self):
        # Muestra los participantes actuales
        if not self.observadores:
            print("No hay participantes registrados.")
        else:
            print("👥 Participantes:")
            for obs in self.observadores:
                print(f" - {obs.nombre}")

# Menú interactivo
def menu():
    # Solicita los datos iniciales del evento
    nombre = input("Nombre del evento: ")
    fecha = input("Fecha (ej. 2025-04-10): ")
    lugar = input("Lugar del evento: ")
    evento = EventoCalendario(nombre, fecha, lugar)

    participantes = {}  # Diccionario de participantes registrados

    while True:
        # Menú principal
        print("\n--- MENÚ ---")
        print("1. Añadir participante")
        print("2. Quitar participante")
        print("3. Cambiar fecha/lugar del evento")
        print("4. Ver participantes")
        print("5. Ver detalles del evento")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre_part = input("Nombre del participante: ")
            if nombre_part not in participantes:
                p = Participante(nombre_part)  # Crea un nuevo participante
                participantes[nombre_part] = p
                evento.agregar_observador(p)  # Lo agrega como observador del evento
                print(f"✅ {nombre_part} añadido.")
            else:
                print("⚠️ Ese participante ya está suscrito.")

        elif opcion == "2":
            nombre_part = input("Nombre del participante a quitar: ")
            if nombre_part in participantes:
                evento.quitar_observador(participantes[nombre_part])  # Elimina de la lista de observadores
                del participantes[nombre_part]  # También del diccionario
                print(f"❌ {nombre_part} eliminado.")
            else:
                print("⚠️ Ese participante no está suscrito.")

        elif opcion == "3":
            # Permite cambiar la fecha y/o el lugar del evento
            nueva_fecha = input("Nueva fecha (Enter para dejar igual): ")
            nuevo_lugar = input("Nuevo lugar (Enter para dejar igual): ")
            evento.cambiar_evento(
                nueva_fecha if nueva_fecha else None,
                nuevo_lugar if nuevo_lugar else None
            )

        elif opcion == "4":
            evento.listar_participantes()  # Muestra los participantes actuales

        elif opcion == "5":
            # Muestra los detalles actuales del evento
            print(f"\n📅 Evento: {evento.nombre}")
            print(f"📆 Fecha: {evento.fecha}")
            print(f"📍 Lugar: {evento.lugar}")

        elif opcion == "6":
            print("¡Hasta luego!")  # Cierra el programa
            break

        else:
            print("Opción no válida.")  # Manejo de entradas no válidas

# Ejecutar el menú
menu()  # Se ejecuta el menú si se corre el script directamente


