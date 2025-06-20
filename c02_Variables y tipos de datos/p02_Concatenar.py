# Concatinación de cadenas en Python

nombre = "Ana"
edad = 25

# Correcto (ambos son strings):
saludo = "Hola, " + nombre  # "Hola, Ana"

# Error (no se puede concatenar str + int):
# mensaje = "Tienes " + edad + " años"  # ❌ TypeError

# Solución: Convertir a string primero:
mensaje = "Tienes " + str(edad) + " años"  # ✅ "Tienes 25 años"

# f-strings (Python 3.6+, recomendado)

nombre = "Carlos"
puntos = 100

mensaje = f"{nombre} tiene {puntos} puntos"  # "Carlos tiene 100 puntos"

# Concatenación

nombre = "Luis"
apellidos = "Peña"
web = "LuisPeñaEscobar.es"

print(nombre + " " + apellidos + " - " + web)

print(f"{nombre} {apellidos} - {web}")  # Usando f-string

print("Hola me llamo {} {} y mi web es {}".format(nombre, apellidos, web))  # Usando format