"""
Docstring del módulo suma.py
Este módulo contiene la función metodo_suma 
que recibe una cantidad variable de argumentos y devuelve la suma de todos ellos.

Ejemplo:
    print(metodo_suma(10,20,30,40,50))
    >> Salida: 150

"""

def metodo_suma(*args):
    """
    docstring de la función metodo_suma
    Esta función recibe una cantidad variable de argumentos y devuelve la suma de todos ellos.
    """
    sum = 0
    for arg in args:
        sum += arg
    return sum