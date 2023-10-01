o = int(input('Number: '))
for p in range(0,3):
  if o <= 10:
    print('dado')
  print('1')
  print('2')
print('pula')

################
print('')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
  print(c)
print('Fim')

############
print('')
p = int(input('Quantas vezes você deseja? '))
for c in range(0,p):
  nome = input('Qual seu nome?')
  print(nome)
print('Tá feito')

##########
print('')
s=0
m = int(input('Quantos números você deseja somar?'))
for c in range(0,m):
  n = int(input('Qual o valor? '))
  s += n
print('O valor final é: ', s)

#########
print('')
for c in range(1, 11):
  print(c)
print('Ok.')

########
print('')
print('O mesmo código mas usando While')
c = 1
while c < 11:
  print(c)
  c = c + 1
print('Fim.')

#######
print('')
n = 1
while n != 0:
  n = int(input('Digite um valor: '))
print('Fim')

