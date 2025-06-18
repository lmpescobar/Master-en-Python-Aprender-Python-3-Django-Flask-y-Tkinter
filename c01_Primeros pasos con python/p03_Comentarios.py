"""
Comentarios de código

1. Comentarios de una línea (#)
Se usan para explicar una línea específica o desactivarla. Ejemplo:
"""

# Esto es un comentario y no se ejecuta
print("Hola")  # Esto imprime "Hola"

# La siguiente línea está desactivada:
# print("Esto no se ejecutará")

"""
2. Comentarios multilínea
Se usan para documentación o bloques de texto largos. También sirven como docstrings (documentación de funciones/clases).
Ejemplo:
"""

'''
Esto es un comentario
que ocupa varias líneas.
No afecta al programa.
'''

def suma(a, b):
    """
    Esta función suma dos números.
    
    Args:
        a (int/float): Primer número.
        b (int/float): Segundo número.
    
    Returns:
        int/float: Resultado de a + b.
    """
    return a + b