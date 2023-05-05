# condicao = True
#
# while condicao:
#     nome = input('Qual é seu nome: ').upper()
#     print(f'Seu nome é {nome}')
#
#     if nome == 'SAIR':
#         break
# print('Acabou')

contador = 0
while contador < 20:
    contador += 1

    if contador == 6: #vai pular o número 6
        continue

    if contador >= 10 and contador <=15:#vai pular o número 10 ao 15
        continue

    print(contador)
print('Acabou')
