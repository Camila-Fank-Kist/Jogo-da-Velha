# Atividade 4 - Jogo da Velha - fucnionando com
def verificar_digito(caractere, qual):
    while True:
        digito = input(f'{caractere}, informe a {qual}: ')
        if digito.isdigit():
            digito = int(digito)
            if 0 <= digito <= 2:
                break
            else:
                print('Informe um número entre 0 e 2.')
        else:
            print('Informe um número.')
    return digito


def inserir(caractere):
    while True:
        linha = verificar_digito(caractere, 'linha')
        coluna = verificar_digito(caractere, 'coluna')
        if matriz[linha][coluna] == '':
            matriz[linha][coluna] = caractere
            break
        else:
            print('Espaço já ocupado. Tente novamente.')


def imprimir(matriz):
    for i in range(3):
        for j in range(3):
            print(f'[{matriz[i][j]:^3}]', end='')
        print()


def verificacao(matriz):
    ganhou = False
    # verificar as linhas (1°) e colunas (2°):
    for i in range(3):
        if matriz[i][0] == matriz[i][1] == matriz[i][2] != '':
            ganhou = True
        if matriz[0][i] == matriz[1][i] == matriz[2][i] != '':
            ganhou = True
    # verificar as diagonais:
    if matriz[0][0] == matriz[1][1] == matriz[2][2] != '':
        ganhou = True
    if matriz[0][2] == matriz[1][1] == matriz[2][0] != '':
        ganhou = True
    return ganhou


matriz = [['' for _ in range(3)] for _ in range(3)]
qtd_jogadas = 0

while True:
    inserir('X')
    qtd_jogadas += 1
    imprimir(matriz)
    ganhou = verificacao(matriz)
    if ganhou == True:
        print('X ganhou')
        break
    elif qtd_jogadas == 9:
        print('Velha')
        break
    inserir('O')
    qtd_jogadas += 1
    imprimir(matriz)
    ganhou = verificacao(matriz)
    if ganhou == True:
        print('O ganhou')
        break
    elif qtd_jogadas == 9:
        print('Velha')
        break
