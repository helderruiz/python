valores = []
for contador in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for posicao, valor in enumerate(valores):
    print(f'Na posição {posicao} encontrei o valor {valor}')


lista_a = [2, 3, 4, 5]
lista_b = lista_a[:] # faz uma copia da lista a
lista_b[2] = 0
print(lista_a)
print(lista_b)
