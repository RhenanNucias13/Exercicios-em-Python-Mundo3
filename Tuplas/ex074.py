from random import randint
nums = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print('Os valores sorteados foram: ', end='')
for n in nums:
    print(f'{n} ',end='')

print(f'\nO MAIOR valor foi {max(nums)}.')
print(f'O MENOR valor foi {min(nums)}.')