valorFb = float(input('Valor de fábrica: '))
percDis = valorFb * 128/100
percImp = valorFb * 145/100
custFb = percDis + percImp
print(f'O valor do cusdo de fábrica é {valorFb} reais e custo do consumidor é {custFb} reais.')