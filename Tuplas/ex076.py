listagem = ('Teclado', 150, 'Mouse', 80, 'Headset', 200, 'Monitor', 900, 'Cadeira', 750,
            'Mousepad', 50, 'Controle de videogame', 250, 'Computador', 3500, 'Microfone', 180)
for i in listagem:
    if type(i) is str:
        print(f'{i:.<32}', end='')
    else:
        print(f'R${i:>5.2f}')