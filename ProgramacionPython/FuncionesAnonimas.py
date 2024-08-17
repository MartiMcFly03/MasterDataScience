#Entendiendo las funciones lambda

#Funcion lambda
#Es una funcion anonima que se puede usar para realizar calculos rapidos
#Se puede usar en cualquier lugar donde se requiera una funcion
#No tiene nombre
#No tiene un return explicito
#No tiene un cuerpo de funcion
#No tiene un docstring
#No tiene un nombre de argumento

#Sintaxis
#lambda argumentos: expresion

#Ejemplo
#Funcion que suma dos numeros
suma = lambda x, y: x + y
print(suma(3, 5))

#funcion que devuelve los numeros pares
pares = lambda x: x % 2 == 0
print(pares)

#entendiendo la funcion filter
#filter(funcion, secuencia)
#Devuelve una secuencia de elementos para los cuales la funcion devuelve True
#Si la funcion es None, devuelve los elementos que son True
#La secuencia puede ser una lista, una tupla, un string, un diccionario, un set

#Ejemplo
#Lista de numeros
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Filtrar los numeros pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

#Entendiendo la funcion map
#map(funcion, secuencia)
#Devuelve una secuencia de elementos donde la funcion se aplica a cada elemento de la secuencia
#La secuencia puede ser una lista, una tupla, un string, un diccionario, un set

#Ejemplo
#Lista de numeros
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Elevar al cuadrado los numeros
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)
