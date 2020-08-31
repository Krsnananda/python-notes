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

# print('O dobro de {} é {}'.format(n, d))
# print('O triplo de {} é {}'.format(n, t))
# print('A raiz quadrada de {} é {:.3f}'.format(n, r))

print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O triplo de {} vale {}. \n A raiz quadrada de {} vale {:.2f}'.format(n, (n*3), n, pow(n, (1/2)))) #pow(base, expoente)