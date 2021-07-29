slr = int(input('Salário Bruto: '))
prest = int(input('Informe a prestação: '))
valorTotal = slr * 0.3

if prest < valorTotal:
    print('O emprestimo pode ser concedido')
else: 
    print('O emprestimo não pode ser concedido')