# Informe nome e idade
nome = input('Informe o seu nome: ')
idade = int(input('Informe a sua idade: '))

while True:

# exibe a lista de filmes e suas salas
    print('LISTA DE FILMES\n')
    print('Sala 1 - A volta dos que não foram - 12 anos.')
    print('Sala 2 - A Roda Quadrada - 14 anos.')
    print('Sala 3 - Poeira em alto mar - 16 anos.')
    print('Sala 4 - As tranças do Rei careca - 10 anos.')
    print('Sala 5 - A vingaça do peixe frito - 18 anos.')


#recebe a sala escolhida
    sala = int(input('Informe a sala desejada de acordo com a Classificação Indicativa: '))


#Apresenta o filme escolhido
    match sala:
        case '1':
             idade_minima = 12
             print(f'Filme escolhido por {nome}: A volta dos que não foram.')
        case '2': 
            idade_minima = 14
            print(f'Filme escolhido {nome}: Poeira em alto mar.')
        case '3':
            idade_minima = 16
            print(f'Filme escolhido {nome}: A Roda Quadrada.')
        case '4': 
            idade_minima = 10
            print(f'Filme escolhido por {nome}: As tranças do Rei careca.')
        case '5':
            idade_minima = 18
            print(f'Filme escolhido por {nome}: A vingança do Peixe Frito.')
        case _:
            print('Sala Inexistente.')
            continue

    if idade >= idade_minima:
        print(f'Ingresso liberado para {nome}.')

    else:
        print(f'Entrada não permitida para {nome}. Escolha outro filme!')
        continue



        

