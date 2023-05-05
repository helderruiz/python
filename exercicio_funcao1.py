# Crie funções que duplicam, triplicam e quadriplicam
# o número recibido como parâmetro.

# def duplicar(numero):
#     print(f'O número {numero} duplicado é: ', end='')
#     return numero * 2
#
# sair = ''
# while sair != 'S':
#     numero = int(input('Digite um número para ser duplicado: '))
#     print(duplicar(numero))
#     sair = input('Deseja sair do programa? [s/n]: ').upper().strip()


def criar_multiplicador(multiplicador):
    print(f'O número {numero} ', end='')

    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

sair = ''
while sair != 'S':
    numero = int(input('Digite um número: '))
    duplicar_triplicar_quadriplicar = input('Digite "[D]uplicar", "[T]riplicar", "[Q]uadriplicar" o seu número: ').upper()

    if duplicar_triplicar_quadriplicar == 'D':
        duplicar = criar_multiplicador(2)
        print(f'Duplicado é: {duplicar(numero)}')
    elif duplicar_triplicar_quadriplicar == 'T':
        triplicar = criar_multiplicador(3)
        print(f'Triplicado é: {triplicar(numero)}')
    elif duplicar_triplicar_quadriplicar == 'Q':
        quadriplicar = criar_multiplicador(4)
        print(f'Quadriplicado é: {quadriplicar(numero)}')
    else:
        print(f'Opção {duplicar_triplicar_quadriplicar} é inválido.')

    sair = input('Deseja encerrar o programa? [S/N]: '). upper()
    print('-' * 40)
