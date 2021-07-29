N = int(input())

# hr = N // 3600
# tempoRestante = hr % 3600
# hora = tempoRestante

# min = hora // 60
# tempoRestante = min % 60
# minuto = tempoRestante

# seg = minuto

hora = N//3600
resto = (N - hora*3600)

minuto = resto//60
resto = resto - minuto*60





print(f'{hora}:{minuto}:{resto}')


