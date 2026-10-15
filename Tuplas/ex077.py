palavras = ('backend', 'frontend', 'framework',
            'biblioteca', 'debug', 'terminal', 'servidor',
            'API', 'loop', 'classe', 'objeto', 'repositório')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')