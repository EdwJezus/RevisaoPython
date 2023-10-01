def linha():
  print('----------------')

linha()
print('Aula 01')
linha()

########
def cab(atv):
  print('')
  print('---------------')
  print('Atividade', (atv))
  print('---------------')
  print('')


print('Varias atividades')
cab('01')
cab('02')
cab('Final')

###########
def soma(a, b):
  s = a + b
  print(s)


soma(1, 3)

def contador(*num):
  tam = len(num)
  print(f'Os valores são {num} e ao todo são {tam} valores.')


contador(2,3,4,5,6,1,2)

########desafio
cab('Controle de Terrenos')

def area():
  l = float(input('Largura do terreno (m): '))
  c = float(input('Comprimento do terreno (m): '))
  a = l*c
  print(f'A área do terreno {l}x{c} é de {a}m².')
  

area()

###02

def escreva(palavra):
  carc = len(palavra)+2
  print('~'*carc)
  print(palavra.center(carc))
  print('~'*carc)

escreva('Atividade nova')

#######03
cab('Passos')

def contador():
  print('Contagem de 1 até 10 de 1 em 1:')
  for n1 in range (1, 11, 1):
    print(n1)
  print('Fim!')
  ##########
  print('-='*20)
  print('Contagem de 10 até 0 de 2 em 2:')
  for n2 in range (10, -1, -2):
    print(n2)
  print('Fim!')
  ##########
  print('-='*20)
  print('Agora é sua vez de personalizar a contagem!')
  a = int(input('Início: '))
  b = int(input('Fim: '))
  c = int(input('Passo: '))
  print('-='*20)
  print(f'Contagem de {a} até {b} de {c} em {c}:')
  for s in range (a, b+1, c):
    print(s)
  print('Fim!')


contador()
