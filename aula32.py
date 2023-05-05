numeros = []

while True:
    valor = int(input('Digite um valor: '))
    if valor not in numeros:
        numeros.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! não vou adicionar...')

    resposta = str(input('Quer continuar? [S/N]')).upper()
    if resposta in 'N':
        break

print('-=' * 20)
numeros.sort()
print(f'Você adicionou os valores {numeros}')