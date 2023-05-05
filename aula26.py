numero = int(input('Digite um número para saber a tabuada: '))
i = 0
while i <= 9:
    i += 1
    print(f'A tabuada do número {numero} x {i} = {numero*i}')


    if i == 10:
        sair = str(input('Deseja sair? [S/N]')).upper().strip()
        if sair == 'S':
            print('PROGRAMA FINALIZADO')
        else:
            i = 0
            numero = int(input('Digite um número para saber a tabuada: '))
