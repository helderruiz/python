palavra_secreta = 'perfume'
letras_acertadas = ''
numero_de_tentativas = 0

while True:
    letra_digitada = str(input('Digite uma letra: '))
    numero_de_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite somente uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(f'Palavra fomarda {palavra_formada}')

    if palavra_formada == palavra_secreta:
        print('Você GANHOU!!!')
        print(f'A palafra secreta é {palavra_secreta}')
        print(f'{numero_de_tentativas=}\n')

        letras_acertadas = ''
        numero_de_tentativas = 0
