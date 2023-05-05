senha = '123456'
senha_digitada = ''
repeticoes = 0

while senha != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x)')

    repeticoes += 1
print(repeticoes)
print('Aquele laço acima pode ter repetições infinitas')
