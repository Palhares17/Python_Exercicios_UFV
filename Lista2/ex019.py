idade = int(input('Idade: '))
peso = int(input('Peso: '))

# 500mg - ml; a cada ml - 20 gota


if idade >= 12: 
    if peso >= 60:
        print('O adulto é 40 gotas')
    else:
        print('Você não tem peso de adulto kkkk')

if idade < 12:
    if peso >= 5 and peso < 9: 
        mg = 125/500
        gotas = mg * 20
        
    elif peso >= 9 and peso < 16: 
        mg = 250/500
        gotas = mg * 20
        
    elif peso >= 16 and peso < 24: 
        mg = 275/500
        gotas = mg * 20
        
    elif peso >= 24 and peso < 30: 
        mg = 500/500
        gotas = mg * 20
        
    elif peso > 30:
        mg = 750/500
        gotas = mg * 20
        
print(f'Gotas: {int(gotas)}')