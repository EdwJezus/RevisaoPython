n1 = int(input('Digite um valor? '))
n2 = int(input('Digite mais um valor? '))

print('Seus valores são:',n1,'e',n2,'.')

print(f'Seus valores são: {n1} e {n2}.')

print('Seus valores são: {} e {}.'.format(n1, n2))

######Para casas decimais
sal = 340
print(f'Seu salário é {sal:.2f}')

#######Para espaços
sal = 520
print(f'Seu salário é {sal:20} por ano')
