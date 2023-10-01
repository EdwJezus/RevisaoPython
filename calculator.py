n1 = int(input('Digite um valor? '))
n2 = int(input('Digite mais um valor? '))
print('[1] somar')
print('[2] multiplicar')
print('[3] maior')
print('[4] novos números')
print('[5] sair do programa')
op = 0
while op != 5:
  op = int(input('Qual operação você deseja realizar? '))
  if op == 4:
    n1 = int(input('Digite um valor? '))
    n2 = int(input('Digite mais um valor? '))
  elif op == 1:
    print(n1 + n2)
  elif op == 2:
    print(n1 * n2)
  elif op == 3:
    print(max(n1, n2))
