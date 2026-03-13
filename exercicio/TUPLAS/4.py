lista = [1, 2, 3]
lista[0] = 99
print(lista)

#Tupla não se pode trocar os números, pois é imutável.

tupla = (1, 2, 3)
tupla_lista = list(tupla)
tupla_lista[0] = 99
tupla = tuple(tupla_lista)
print(tupla)
