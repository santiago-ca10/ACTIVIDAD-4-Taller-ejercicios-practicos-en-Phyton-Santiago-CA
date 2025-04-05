# Clase base abstracta para todos los alimentos
class Alimento:
    def descripcion(self):
        pass  # Método que se sobreescribirá en las clases hijas
    
    def costo(self):
        pass  # Método que se sobreescribirá en las clases hijas

# Representa un plato principal, hereda de Alimento
class PlatoPrincipal(Alimento):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio  # Precio base del plato principal
    
    def descripcion(self):
        return f"Plato principal: {self.nombre}"  # Describe el plato
    
    def costo(self):
        return self.precio  # Retorna el precio base

# Decorador base que permite añadir extras al alimento
class AdicionalDecorator(Alimento):
    def __init__(self, alimento):
        self.alimento = alimento  # Almacena una instancia de Alimento (composición)
    
    def descripcion(self):
        return self.alimento.descripcion()  # Delega la descripción al alimento base
    
    def costo(self):
        return self.alimento.costo()  # Delega el costo al alimento base

# Decorador para añadir postres al pedido
class PostreDecorator(AdicionalDecorator):
    def __init__(self, alimento, nombre_postre, precio_postre):
        super().__init__(alimento)
        self.nombre_postre = nombre_postre
        self.precio_postre = precio_postre
    
    def descripcion(self):
        return f"{self.alimento.descripcion()} + Postre: {self.nombre_postre}"
    
    def costo(self):
        return self.alimento.costo() + self.precio_postre  # Suma el precio del postre

# Decorador para añadir bebidas al pedido
class BebidaDecorator(AdicionalDecorator):
    def __init__(self, alimento, nombre_bebida, precio_bebida):
        super().__init__(alimento)
        self.nombre_bebida = nombre_bebida
        self.precio_bebida = precio_bebida
    
    def descripcion(self):
        return f"{self.alimento.descripcion()} + Bebida: {self.nombre_bebida}"
    
    def costo(self):
        return self.alimento.costo() + self.precio_bebida  # Suma el precio de la bebida

# Decorador para añadir porciones extras al pedido
class PorcionExtraDecorator(AdicionalDecorator):
    def __init__(self, alimento, extra, precio_extra):
        super().__init__(alimento)
        self.extra = extra
        self.precio_extra = precio_extra
    
    def descripcion(self):
        return f"{self.alimento.descripcion()} + Extra: {self.extra}"
    
    def costo(self):
        return self.alimento.costo() + self.precio_extra  # Suma el precio del extra

# Clase que gestiona todo el menú del restaurante
class MenuRestaurante:
    def __init__(self):
        # Diccionarios con las opciones disponibles
        self.platos_principales = {
            1: {"nombre": "Hamburguesa", "precio": 8500},
            2: {"nombre": "Pizza", "precio": 10000},
            3: {"nombre": "Ensalada", "precio": 7000},
            4: {"nombre": "Pasta carbonara", "precio": 9500}
        }
        
        self.postres = {
            1: {"nombre": "Helado de vainilla", "precio": 3000},
            2: {"nombre": "Tarta de chocolate", "precio": 4000},
            3: {"nombre": "Fruta fresca", "precio": 2500},
            0: {"nombre": "Ninguno", "precio": 0}
        }
        
        self.bebidas = {
            1: {"nombre": "Refresco mediano", "precio": 2000},
            2: {"nombre": "Agua mineral", "precio": 1500},
            3: {"nombre": "Cerveza artesanal", "precio": 3500},
            4: {"nombre": "Jugo natural", "precio": 2500},
            0: {"nombre": "Ninguna", "precio": 0}
        }
        
        self.extras = {
            1: {"nombre": "Papas fritas grandes", "precio": 2500},
            2: {"nombre": "Aros de cebolla", "precio": 3000},
            3: {"nombre": "Porción extra de queso", "precio": 1500},
            0: {"nombre": "Ninguno", "precio": 0}
        }
    
    # Muestra las opciones disponibles en un grupo (platos, postres, etc.)
    def mostrar_opciones(self, items, titulo):
        print(f"\n--- {titulo} ---")
        for key, item in items.items():
            if key != 0:  # Solo oculta el precio si es la opción "ninguno"
                print(f"{key}. {item['nombre']} - ${item['precio']:.2f}")
            else:
                print(f"{key}. {item['nombre']}")
    
    # Permite al usuario seleccionar una opción válida
    def seleccionar_opcion(self, items, tipo):
        while True:
            try:
                opcion = int(input(f"\nSeleccione {tipo} (número): "))
                if opcion in items:
                    return opcion
                else:
                    print(f"⚠️ Opción inválida. Por favor ingrese un número entre {min(items.keys())} y {max(items.keys())}.")
            except ValueError:
                print("⚠️ Error: Por favor ingrese solo números.")
    
    # Selecciona el plato principal
    def seleccionar_plato_principal(self):
        self.mostrar_opciones(self.platos_principales, "PLATOS PRINCIPALES")
        opcion = self.seleccionar_opcion(self.platos_principales, "un plato principal")
        plato = self.platos_principales[opcion]
        return PlatoPrincipal(plato["nombre"], plato["precio"])
    
    # Añade un adicional usando el decorador correspondiente
    def seleccionar_adicionales(self, plato, tipo, decorador_clase, items):
        self.mostrar_opciones(items, tipo.upper())
        opcion = self.seleccionar_opcion(items, f"un {tipo.lower()} (o 0 para omitir)")
        
        if opcion != 0:
            item = items[opcion]
            # Se usa el decorador correspondiente
            if decorador_clase == PostreDecorator:
                plato = PostreDecorator(plato, item["nombre"], item["precio"])
            elif decorador_clase == BebidaDecorator:
                plato = BebidaDecorator(plato, item["nombre"], item["precio"])
            elif decorador_clase == PorcionExtraDecorator:
                plato = PorcionExtraDecorator(plato, item["nombre"], item["precio"])
        
        return plato
    
    # Muestra el resumen del pedido y lo confirma
    def confirmar_pedido(self, plato):
        print("\n--- RESUMEN DE SU PEDIDO ---")
        print(plato.descripcion())
        print(f"TOTAL: ${plato.costo():.2f}")
        
        while True:
            confirmacion = input("\n¿Confirmar pedido? (S/N): ").upper()
            if confirmacion in ['S', 'N']:
                return confirmacion == 'S'
            print("⚠️ Por favor ingrese 'S' para Sí o 'N' para No.")
    
    # Orquesta el flujo completo del pedido
    def realizar_pedido(self):
        print("¡Bienvenido al restaurante!")
        print("---------------------------")
        
        # Selección del plato principal y adicionales
        plato = self.seleccionar_plato_principal()
        plato = self.seleccionar_adicionales(plato, "POSTRE", PostreDecorator, self.postres)
        plato = self.seleccionar_adicionales(plato, "BEBIDA", BebidaDecorator, self.bebidas)
        plato = self.seleccionar_adicionales(plato, "EXTRA", PorcionExtraDecorator, self.extras)
        
        # Confirmación del pedido
        if self.confirmar_pedido(plato):
            print("\n✅ ¡Pedido confirmado! Gracias por su compra.\n")
        else:
            print("\n❌ Pedido cancelado.\n")

# Punto de entrada del programa
if __name__ == "__main__":
    while True:
        try:
            menu = MenuRestaurante()
            menu.realizar_pedido()
            
            continuar = input("¿Desea hacer otro pedido? (S/N): ").upper()
            if continuar != 'S':
                print("¡Gracias por visitarnos! Hasta pronto.")
                break
        except KeyboardInterrupt:
            print("\n\n❌ Programa interrumpido por el usuario.")
            break
        except Exception as e:
            print(f"\n⚠️ Error inesperado: {e}")
            print("Reiniciando el menú...\n")
