import math

A = int(input())

if(A > 0 or A == 0):
    print(f'A raiz quadrada de {math.sqrt(A):.2f}')    
else:
    print(f'O quadrado é {A**2}')