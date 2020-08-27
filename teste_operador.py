import math

# Anterior e Sucessor
num = int(input('Digita um número aí: '))

ant = num - 1
suc = num + 1

print('O número antes de {} é {} e o depois dele é {}'.format(num, ant, suc))

# Dobro, Triplo e Raiz quadrada
n = int(input('Manda um número: '))
d = n * 2
t = n * 3
r = math.sqrt(n)

print('O dobro de {} é {}'.format(n, d))
print('O triplo de {} é {}'.format(n, t))
print('A raiz quadrada de {} é {}'.format(n, r))