turma = {
    'bernardo' : [6,5,3],
    'victor' : [8,5,3],
    'matheus' : [9,7,5],
    'gabriel' : [7,9,5],
    'joao miguel' : [2,7,5]
}

for aluno, valor in turma.items():
    a = sum(valor) / len(valor)

    if a >= 6.0:
        print(f'{aluno} -- Média: {a} -- Situação: Aprovado')
    else:
        print(f'{aluno} -- Média: {a} -- Situação: Reprovado')

