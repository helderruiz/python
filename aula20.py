# Calculadora com while
while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')
    operador = input('Digite o Operador ex(+-/*): ')
#################################################################
    # validação do programa #
    numeros_validos = None
    numero1_float = 0
    numero2_float = 0
    try:
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números são inválidos.')
        continue

    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    if len(operador) > 1:
        print('Digite apenas 1 operador!')
        continue
#################################################################
    # Lógica do Programa #
    print('Realizando sua conta. Confira o resultado abaixo!')
    if operador == '+':
        print(f'{numero1_float} + {numero2_float} =', numero1_float + numero2_float)
    elif operador == '-':
        print(f'{numero1_float} - {numero2_float} =', numero1_float - numero2_float)
    elif operador == '/':
        print(f'{numero1_float} / {numero2_float} =', numero1_float / numero2_float)
    elif operador == '*':
        print(f'{numero1_float} * {numero2_float} =', numero1_float * numero2_float)
    else:
        print('Nunca deveria chegar aqui!!!')

    sair = input('Deseja sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break
