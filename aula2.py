nome_completo = input('Qual é seu nome? ')
idade = int(input('Quantos anos você tem? '))

if idade >= 18:
    print(f'{nome_completo} tem {idade} e é maior de idade')
else:
    print(f'{nome_completo} tem {idade} e é menor de idade')
    