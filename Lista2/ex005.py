divsor = int(input('Divisor: '))
divdendo = int(input('Dividendo: '))

if(divsor > 0):
    mod = divsor % divdendo
    divInt = divsor // divdendo
    print(f'Resto da divisão: {mod}.')
    print(f'Quociente {divInt}.')
else:
    print('Divisão não permitida.')