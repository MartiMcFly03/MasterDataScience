#Comando para restar 
# n cantidad de numeros

"""
docstring del modulo Resta.py
Este modulo contiene la funcion metodo_resta
que recibe n cantidad de argumentos y los resta

Ejemplo:
    print(metodo_resta(10,20,30,40,50))
    >> Salida: -150
"""

def metodo_resta(*args):
    """
    docstring de la funcion metodo_resta
    Esta funcion recibe n cantidad de argumentos y los resta
    """
    resta = 0
    for arg in args:
        resta -= arg
    return resta
