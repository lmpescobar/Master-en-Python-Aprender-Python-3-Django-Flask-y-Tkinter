# =============================================
# DEMOSTRACIÓN DE CONVERSIÓN ENTRE TIPOS EN PYTHON
# =============================================

def mostrar_titulo(titulo):
    print(f"\n{'='*50}")
    print(f"{titulo.upper():^50}")
    print(f"{'='*50}")

# 1. Conversiones Básicas
mostrar_titulo("Conversiones Básicas")

# De/Entero (int)
num_entero = 10
print(f"\nEntero original: {num_entero} ({type(num_entero)})")

# Entero a Float
a_float = float(num_entero)
print(f"Entero a Float: {a_float} ({type(a_float)})")

# Entero a String
a_string = str(num_entero)
print(f"Entero a String: '{a_string}' ({type(a_string)})")

# Entero a Booleano
a_bool = bool(num_entero)
print(f"Entero a Booleano: {a_bool} ({type(a_bool)})")

# 2. Conversiones con Strings
mostrar_titulo("Conversiones con Strings")

# String a Entero
cadena_num = "25"
a_entero = int(cadena_num)
print(f"\nString original: '{cadena_num}' ({type(cadena_num)})")
print(f"String a Entero: {a_entero} ({type(a_entero)})")

# String a Float
cadena_float = "3.14"
a_float = float(cadena_float)
print(f"\nString original: '{cadena_float}' ({type(cadena_float)})")
print(f"String a Float: {a_float} ({type(a_float)})")

# String a Lista
cadena = "Python"
a_lista = list(cadena)
print(f"\nString original: '{cadena}' ({type(cadena)})")
print(f"String a Lista: {a_lista} ({type(a_lista)})")

# 3. Conversiones con Colecciones
mostrar_titulo("Conversiones con Colecciones")

# Lista a Tupla
lista = [1, 2, 3]
a_tupla = tuple(lista)
print(f"\nLista original: {lista} ({type(lista)})")
print(f"Lista a Tupla: {a_tupla} ({type(a_tupla)})")

# Tupla a Conjunto
tupla = (1, 2, 2, 3)
a_conjunto = set(tupla)
print(f"\nTupla original: {tupla} ({type(tupla)})")
print(f"Tupla a Conjunto: {a_conjunto} ({type(a_conjunto)})")

# Diccionario a Lista (de claves)
diccionario = {"a": 1, "b": 2}
a_lista = list(diccionario)
print(f"\nDiccionario original: {diccionario} ({type(diccionario)})")
print(f"Diccionario a Lista (claves): {a_lista} ({type(a_lista)})")

# 4. Conversiones Especiales
mostrar_titulo("Conversiones Especiales")

# Bytes a String
datos_bytes = b'Python'
a_string = datos_bytes.decode('utf-8')
print(f"\nBytes original: {datos_bytes} ({type(datos_bytes)})")
print(f"Bytes a String: '{a_string}' ({type(a_string)})")

# String a Bytes
cadena = "Conversión"
a_bytes = cadena.encode('utf-8')
print(f"\nString original: '{cadena}' ({type(cadena)})")
print(f"String a Bytes: {a_bytes} ({type(a_bytes)})")

# Lista a String
lista = ['a', 'b', 'c']
a_string = ''.join(lista)
print(f"\nLista original: {lista} ({type(lista)})")
print(f"Lista a String: '{a_string}' ({type(a_string)})")

# 5. Conversiones con Condiciones
mostrar_titulo("Conversiones con Condiciones")

# Booleano a Entero
verdadero = True
a_entero = int(verdadero)
print(f"\nBooleano original: {verdadero} ({type(verdadero)})")
print(f"Booleano a Entero: {a_entero} ({type(a_entero)})")

# Float a Entero (truncamiento)
pi = 3.1416
a_entero = int(pi)
print(f"\nFloat original: {pi} ({type(pi)})")
print(f"Float a Entero (truncado): {a_entero} ({type(a_entero)})")

# Redondeo de Float
redondeado = round(pi, 2)
print(f"\nFloat original: {pi} ({type(pi)})")
print(f"Float redondeado: {redondeado} ({type(redondeado)})")

# 6. Conversiones Avanzadas
mostrar_titulo("Conversiones Avanzadas")

# Diccionario a String (JSON)
import json
diccionario = {"nombre": "Ana", "edad": 30}
a_json = json.dumps(diccionario, indent=2)
print(f"\nDiccionario original: {diccionario} ({type(diccionario)})")
print(f"Diccionario a JSON:\n{a_json} ({type(a_json)})")

# String a Diccionario (JSON)
de_json = json.loads(a_json)
print(f"\nJSON original:\n{a_json} ({type(a_json)})")
print(f"JSON a Diccionario: {de_json} ({type(de_json)})")

# Conjunto a Lista
conjunto = {1, 2, 3}
a_lista = list(conjunto)
print(f"\nConjunto original: {conjunto} ({type(conjunto)})")
print(f"Conjunto a Lista: {a_lista} ({type(a_lista)})")

# Consideraciones Importantes
mostrar_titulo("Consideraciones Importantes")

# 1. Conversiones no siempre posibles
print("\n1. Intentando convertir 'no es número' a entero:")
try:
    int("no es número")
except ValueError as e:
    print(f"Error: {e}")

# 2. Pérdida de precisión
num_grande = 1.9999999999999999
a_entero = int(num_grande)
print(f"\n2. Float grande: {num_grande} ({type(num_grande)})")
print(f"Convertido a entero: {a_entero} (pérdida de decimales)")

# 3. Conversiones implícitas
print("\n3. Conversión implícita:")
print("Operación: 3 (int) + 2.5 (float)")
resultado = 3 + 2.5
print(f"Resultado: {resultado} ({type(resultado)})")

print("\n¡Todas las conversiones demostradas con éxito!")