idade = int(input())

if(idade < 16):
    print('Não vota')
elif(idade > 18 and idade < 65):
    print('Eleitor obrigatório')
else:
    print('Eleitor facultativo')