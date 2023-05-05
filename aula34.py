lista = []

while True:
    print('\033[33mSelecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar [s]air: \033[m')

    if opcao == 'i':
        valor = input('\033[1;30;43m Digite o item: \033[m').upper().strip()
        lista.append(valor)
    elif opcao == 'a':
        try:
            indice_str = int(input('\033[1;30;43mEscolha o índice que deseja apagar: \033[m'))
            del lista[indice_str]
            print('\033[1;32mITEM APAGADO COM SUCESSO...\033[m')
        except ValueError:
            print('\033[1;31mNÃO FOI POSSÍVEL APAGAR ESSE ITEM. DIGITE UM NÚMERO VÁLIDO...\033[m')
        except IndexError:
            print('\033[1;31mÍNDICE NÃO EXISTE NA LISTA...\033[m')
        except Exception:
            print('\033[1;31mErro Desconhecido...\033[m')
    elif opcao == 'l':
        if len(lista) == 0:
            print('\033[1;36mNada para listar.\033[m')
        for i, valor in enumerate(lista):
            print(f'\033[40m {i} {valor} \033[m')
    elif opcao == 's':
        print('\033[1;32mPROGRAMA ENCERRADO! VOLTE SEMPRE...\033[m')
        break
    else:
        print('\033[1;31mPor favor, escolha "i", "a", "l" ou "s"\033[m')
