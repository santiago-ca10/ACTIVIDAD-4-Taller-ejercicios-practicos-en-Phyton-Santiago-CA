class DatabaseConnection:
    _instance = None  # Instancia única compartida

    def __new__(cls):
        # Método especial que se llama antes de __init__
        if cls._instance is None:
            print("🔧 Creando nueva instancia de conexión...")
            cls._instance = super(DatabaseConnection, cls).__new__(cls)  # Crea la instancia
            cls._instance._connected = False  # Inicializa el estado de conexión
        return cls._instance  # Retorna siempre la misma instancia

    def connect(self):
        # Simula conectar a la base de datos
        if not self._connected:
            print("🔌 Conectando a la base de datos (simulada)...")
            self._connected = True
        else:
            print("⚠️ Ya estás conectado.")

    def disconnect(self):
        # Simula desconectar de la base de datos
        if self._connected:
            print("❌ Desconectando de la base de datos...")
            self._connected = False
        else:
            print("⚠️ La conexión ya estaba cerrada.")

    def status(self):
        # Retorna el estado actual de conexión
        return "✅ Conectado" if self._connected else "⛔ Desconectado"


# Función que muestra el menú de opciones
def mostrar_menu():
    print("\n📋 MENÚ:")
    print("1. Conectar a la base de datos")
    print("2. Desconectar de la base de datos")
    print("3. Ver estado de la conexión")
    print("4. Salir")


# Punto de entrada del programa
if __name__ == "__main__":
    db = DatabaseConnection()  # Obtiene la instancia única

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            db.connect()  # Intenta conectar
        elif opcion == "2":
            db.disconnect()  # Intenta desconectar
        elif opcion == "3":
            print("🔍 Estado actual:", db.status())  # Muestra estado de conexión
        elif opcion == "4":
            print("👋 Saliendo del programa...")  # Sale del programa
            break
        else:
            print("❗ Opción no válida. Por favor intenta de nuevo.")  # Opción inválida

