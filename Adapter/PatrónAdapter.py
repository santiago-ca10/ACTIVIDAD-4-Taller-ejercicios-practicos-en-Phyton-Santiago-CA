from abc import ABC, abstractmethod  # Se importa el módulo para definir clases abstractas

# Target
class Traductor(ABC):  # Interfaz esperada por el cliente
    @abstractmethod
    def traducir(self, frase: str) -> str:  # Método abstracto que todas las clases adaptadoras deben implementar
        pass

# Adaptees 
# Clases existentes que no siguen la interfaz 'Traductor'

class TraductorEspanol:
    def traducir_desde_ingles(self, frase):
        # Diccionario de traducción del inglés al español
        traducciones = {
            "hello": "hola",
            "goodbye": "adiós",
            "thank you": "gracias"
        }
        return traducciones.get(frase.lower(), "[traducción no encontrada]")  # Traducción o mensaje por defecto

class TraductorFrances:
    def traduire_depuis_anglais(self, phrase):
        # Diccionario de traducción del inglés al francés
        traductions = {
            "hello": "bonjour",
            "goodbye": "au revoir",
            "thank you": "merci"
        }
        return traductions.get(phrase.lower(), "[traduction non trouvée]")  # Traducción o mensaje por defecto

class TraductorAleman:
    def aus_englisch_übersetzen(self, satz):
        # Diccionario de traducción del inglés al alemán
        übersetzungen = {
            "hello": "hallo",
            "goodbye": "auf wiedersehen",
            "thank you": "danke"
        }
        return übersetzungen.get(satz.lower(), "[übersetzung nicht gefunden]")  # Traducción o mensaje por defecto

#  Adapters
# Estas clases adaptan los "Adaptees" a la interfaz "Traductor"

class AdaptadorEspanol(Traductor):
    def __init__(self, traductor_espanol):
        self.traductor = traductor_espanol  # Instancia del traductor específico

    def traducir(self, frase: str) -> str:
        return self.traductor.traducir_desde_ingles(frase)  # Adapta el método al interfaz esperado

class AdaptadorFrances(Traductor):
    def __init__(self, traducteur_francais):
        self.traducteur = traducteur_francais  # Instancia del traductor específico

    def traducir(self, frase: str) -> str:
        return self.traducteur.traduire_depuis_anglais(frase)  # Adapta el método al interfaz esperado

class AdaptadorAleman(Traductor):
    def __init__(self, deutscher_übersetzer):
        self.übersetzer = deutscher_übersetzer  # Instancia del traductor específico

    def traducir(self, frase: str) -> str:
        return self.übersetzer.aus_englisch_übersetzen(frase)  # Adapta el método al interfaz esperado

# Menú 
def menu():
    # Diccionario de opciones con instancias de adaptadores
    adaptadores = {
        "1": ("Español", AdaptadorEspanol(TraductorEspanol())),
        "2": ("Francés", AdaptadorFrances(TraductorFrances())),
        "3": ("Alemán", AdaptadorAleman(TraductorAleman()))
    }

    while True:
        # Imprime el menú
        print("\n--- Traductor Interactivo ---")
        print("1. Traducir al Español")
        print("2. Traducir al Francés")
        print("3. Traducir al Alemán")
        print("4. Salir")

        opcion = input("Elige una opción (1-4): ").strip()  # Captura la opción del usuario

        if opcion == "4":
            print("¡Hasta luego!")  # Salida del programa
            break
        elif opcion in adaptadores:
            idioma, traductor = adaptadores[opcion]  # Obtiene el idioma y el adaptador correspondiente
            frase = input(f"Escribe una frase en inglés para traducir al {idioma}: ")
            resultado = traductor.traducir(frase)  # Traduce la frase
            print(f"\"{frase}\" en {idioma} => \"{resultado}\"")  # Muestra el resultado
        else:
            print("Opción no válida. Intenta de nuevo.")  # Manejo de errores para entradas inválidas

# Ejecutar programa 
if __name__ == "__main__":
    menu()  # Llama al menú si el script se ejecuta directamente
