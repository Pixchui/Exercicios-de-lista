def estatistica(numeros):
    a = sum(numeros)
    b = len(numeros)
    c = a / b

    lista = [a , c , b]

    tupla = tuple(lista)

    print(tupla)
    

numeros = [10, 20, 30, 40, 50]

estatistica(numeros)