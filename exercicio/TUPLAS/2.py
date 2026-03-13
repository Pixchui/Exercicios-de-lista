produtos = [('Camiseta', 49.90), ('Calça', 89.90), ('Tênis', 199.90)]

for i in produtos:
    pro,val = i

    print(f'{pro}: R${val}')


pr,vl = max(produtos)

print(f'Produto mais caro: {pr}: R${vl}')