valor = int(input())

print(valor)
n100 = valor / 100
print(f'{int(n100)} nota(s) de R$ 100,00')
valor_restante = valor % 100

n50 = valor_restante / 50
print(f'{int(n50)} nota(s) de R$ 50,00')
valor_restante = valor_restante % 50

n20 = valor_restante / 20
print(f'{int(n20)} nota(s) de R$ 20,00')
valor_restante = valor_restante % 20

n10 = valor_restante / 10
print(f'{int(n10)} nota(s) de R$ 10,00')
valor_restante = valor_restante % 10

n5 = valor_restante / 5
print(f'{int(n5)} nota(s) de R$ 5,00')
valor_restante = valor_restante % 5

n2 = valor_restante / 2
print(f'{int(n2)} nota(s) de R$ 2,00')
valor_restante = valor_restante % 2
n1 = valor_restante / 1

print(f'{int(n1)} nota(s) de R$ 1,00')
