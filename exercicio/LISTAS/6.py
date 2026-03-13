def limpar_reprovados(lista_notas):
    lista_passou = []
    for i in lista_notas:
        if i >= 6:
            lista_passou.append(i)
    
    print(lista_passou)



lista_notas = [5.0, 7.0, 4.5, 9.0, 6.0, 3.0, 8.5]

limpar_reprovados(lista_notas)