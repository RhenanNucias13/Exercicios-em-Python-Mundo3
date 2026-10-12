tabela = ('Flamengo','Palmeiras','Fluminense','Athletico-PR','Bahia','Cruzeiro','Atlético-MG',
          'Santos','São Paulo','Coritiba','Red Bull Bragantino','Vitória','Botafogo','Vasco','Mirassol','Corinthians',
          'Internacional','Grêmio','Remo','Chapecoense')
print('-=' * 15)
print(f'LISTA DE TIMES DO BRASILEIRÃO {tabela}')
print('-=' * 15)
print(f'NO G5 ESTÃO: {tabela[0:5]}')
print('-=' * 15)
print(f'NO Z4 ESTÃO: {tabela[-4:]}')
print('-=' * 15)
print(f'OS TIMES EM ORDEM ALFABÉTICA: {sorted(tabela)}')
print('-=' * 15)
print(f'A Chapecoense está na {tabela.index("Chapecoense")+1} posição.')
