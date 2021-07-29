tempoViagem = float(input('Tempo de viagem: '))
vel = float(input('Velocidade média: '))
dis = vel * tempoViagem
litros = dis/12
print(f'Quantidade de litros gastos no percurso de {dis}km de {litros}L')