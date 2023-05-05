nome = input('Digite seu nome: ').capitalize()

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice] # Aqui pega cada letra do nome
    print(letra)
    novo_nome += f'|{letra}'
    indice += 1

print(novo_nome)
