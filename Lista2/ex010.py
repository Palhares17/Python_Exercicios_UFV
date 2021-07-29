A = int(input('Primeiro numero: '))
B  = int(input('Segundo numero : '))
C = int(input('Terceiro numero: '))


maior = A

if (B > maior):
    maior = B
if (C > maior):
     maior = C

menor = A

if (B < menor):
    menor = B
if (C < menor):
    menor = C

meio = A
if(B > menor and B < maior):
    meio = B
if(C > menor and C < maior):
    meio = C

print(f'Maior: {maior}; Meio: {meio}; Menor: {menor}')
