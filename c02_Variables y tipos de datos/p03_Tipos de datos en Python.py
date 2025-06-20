# ======================================
# DEMOSTRACIÓN DE TIPOS DE DATOS EN PYTHON
# ======================================

# ----------------------------
# 1. Tipos de datos primitivos
# ----------------------------
print("\n=== TIPOS PRIMITIVOS ===")

# Entero (int)
edad = 25
print(f"edad: {edad} | Tipo: {type(edad)}")

# Flotante (float)
altura = 1.75
print(f"altura: {altura} | Tipo: {type(altura)}")

# Cadena (str)
nombre = "Ana"
print(f"nombre: {nombre} | Tipo: {type(nombre)}")

# Booleano (bool)
es_mayor = edad >= 18
print(f"es_mayor: {es_mayor} | Tipo: {type(es_mayor)}")

# NoneType
resultado = None
print(f"resultado: {resultado} | Tipo: {type(resultado)}")

# ------------------------------------
# 2. Tipos de datos compuestos
# ------------------------------------
print("\n=== TIPOS COMPUESTOS ===")

# Lista (list)
numeros = [1, 2, 3, 2]
print(f"numeros: {numeros} | Tipo: {type(numeros)}")

# Tupla (tuple)
coordenadas = (4.5, -2.3)
print(f"coordenadas: {coordenadas} | Tipo: {type(coordenadas)}")

# Diccionario (dict)
usuario = {"nombre": "Carlos", "edad": 30}
print(f"usuario: {usuario} | Tipo: {type(usuario)}")

# Conjunto (set)
unicos = {1, 2, 2, 3}  # Elimina duplicados
print(f"unicos: {unicos} | Tipo: {type(unicos)}")

# Frozenset
fset = frozenset({1, 2, 3})
print(f"fset: {fset} | Tipo: {type(fset)}")

# ------------------------------------
# Características clave
# ------------------------------------
print("\n=== CARACTERÍSTICAS CLAVE ===")

# 1. Tipado dinámico
x = 10
print(f"Inicial: x = {x} | Tipo: {type(x)}")
x = "Ahora soy un string"
print(f"Cambiado: x = {x} | Tipo: {type(x)}")

# 2. Verificación de tipos
print(f"\nTipo de 5: {type(5)}")
print(f"Tipo de 'Texto': {type('Texto')}")

# 3. Conversión entre tipos (casting)
print("\nConversiones:")
print(f"str a int: {int('10')} | Tipo: {type(int('10'))}")
print(f"int a float: {float(5)} | Tipo: {type(float(5))}")
print(f"bool a str: {str(True)} | Tipo: {type(str(True))}")
print(f"tuple a list: {list((1, 2))} | Tipo: {type(list((1, 2)))}")

# ------------------------------------
# Ejemplos prácticos
# ------------------------------------
print("\n=== EJEMPLOS PRÁCTICOS ===")

# Trabajando con strings
texto = "Python"
print(f"\nString: '{texto}'")
print(f"Primer carácter: {texto[0]}")
print(f"Longitud: {len(texto)}")
print(f"Contiene 'Py'? {'Py' in texto}")

# Operaciones con listas
frutas = ["manzana", "banana"]
print(f"\nLista inicial: {frutas}")
frutas.append("naranja")
print(f"Después de append: {frutas}")
print(f"Segundo elemento: {frutas[1]}")

# Diccionarios (clave-valor)
persona = {"nombre": "Luisa", "edad": 25}
print(f"\nDiccionario inicial: {persona}")
print(f"Nombre: {persona['nombre']}")
persona["ciudad"] = "Lima"
print(f"Con nueva clave: {persona}")

# ------------------------------------
# Tipos especiales
# ------------------------------------
print("\n=== TIPOS ESPECIALES ===")

# Bytes
dato = b"Python"
print(f"\nBytes: {dato} | Tipo: {type(dato)}")

# Range
rango = range(5)
print(f"Range: {list(rango)} | Tipo: {type(rango)}")

# ------------------------------------
# Ejemplo de error común
# ------------------------------------
print("\n=== ERROR COMÚN ===")
try:
    resultado = 10 + "5"
except TypeError as e:
    print(f"Error al sumar int + str: {e}")

print("Solución con casting:")
print(f"10 + int('5') = {10 + int('5')}")

# ------------------------------------
# Resumen de tipos
# ------------------------------------
print("\n=== RESUMEN DE TIPOS ===")
print("""
| Categoría   | Tipos                                      |
|-------------|--------------------------------------------|
| Numéricos   | int, float, complex                        |
| Texto       | str                                        |
| Booleanos   | bool                                       |
| Secuencias  | list, tuple, range                         |
| Mapas       | dict                                       |
| Conjuntos   | set, frozenset                             |
| Binarios    | bytes, bytearray, memoryview               |
""")