anos = int(input('Anos: '))
meses = int(input('Meses: '))
dias = int(input('Dias: '))

anosDias = anos * 360
msDias = meses * 30
soma = anosDias + msDias + dias

print(f'A sua idade em dias é {soma}.')