from random import randint

caixa = int(input('Dinheiro em caixa: '))
nBola = randint(0, 9)
print(f'\nO número da bola sorteado é {nBola}\n')

if nBola == 0:
    caixa = caixa * 0.05
elif nBola == 1:
    caixa = caixa * 0.25
elif nBola == 2:
    caixa = caixa * 0.1
elif nBola == 3:
    caixa = caixa * 0.07
elif nBola == 4:
    caixa = caixa * 0.08
elif nBola == 5:
    caixa = caixa * 0.05
elif nBola == 6:
    caixa = caixa * 0.15
elif nBola == 7:
    caixa = caixa * 0.12
elif nBola == 8:
    caixa = caixa * 0.03
elif nBola == 9:
    caixa = caixa * 0.1

print(f'O valor do prêmio é {caixa}')