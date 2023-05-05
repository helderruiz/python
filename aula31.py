lista_numero = []
maior_valor = 0
menor_valor = 0

for contador in range(0, 5):
    lista_numero.append(int(input(f'Digite um valor na posição {contador}: ')))
    if contador == 0:
        maior_valor = menor_valor = lista_numero[contador]
    else:
        if lista_numero[contador] > maior_valor:
            maior_valor = lista_numero[contador]
        if lista_numero[contador] < menor_valor:
            menor_valor = lista_numero[contador]

print(f'Você Digitou os valores {lista_numero}')
print(f'O maior valor digitado foi {maior_valor} nas posições ', end='')
for i, v in enumerate(lista_numero):
    if v == maior_valor:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor_valor} nas posições ', end='')
for i, v in enumerate(lista_numero):
    if v == menor_valor:
        print(f'{i}...', end='')