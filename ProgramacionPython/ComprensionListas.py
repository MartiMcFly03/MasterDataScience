rsultados = []
for i in range(1, 11):
    rsultados.append(i ** 2)

print(rsultados)

#Haciendolo con comprension de listas

rsultados = [i ** 2 for i in range(1, 11)]
print(rsultados)

resultados = [i ** 2 for i in range(1, 11) if i % 3 == 0]
print(resultados)

resdic = {i: i ** 2 for i in range(1, 11) if i % 3 == 0}
print(resdic)

resconj = {i ** 2 for i in range(1, 11) if i % 3 == 0}
print(resconj)