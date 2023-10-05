"DOBRO, TRIPLO E RAIZ"
import math
import cmath

var = int (input('Digite um número: '))

raiz = math.pow(var, 1/2)

raiz1 = float(var) ** 0.5

raiz2 = cmath.sqrt(var)


print('O dobro de {} é {}.'.format(var, var*2))
print('O triplo de {} é {}'.format(var, var*3))
print('A raiz quadrada de {} é {}.'.format(var, raiz))

print('A raiz quadrada de {} é {}.'.format(var, raiz1))

print('A raiz quadrada de {} é {}.'.format(var, raiz2))


