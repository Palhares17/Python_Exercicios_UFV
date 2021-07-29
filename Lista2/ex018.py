peso = int(input('Peso na Terra: '))

print('===================== MENU ==========================')
print('\n1-Mercúrio\n2-Vênus\n3-Marte\n4-Júpiter\n5-Saturno\n6-Urano\n')

planeta = int(input('Planeta: '))

if planeta == 1:
    print(f'Mercúrio: {peso * 0.37:.2f}')
elif planeta == 2:
    print(f'Vênus: {peso * 0.88:.2f}')
elif planeta == 3:
    print(f'Marte: {peso * 0.38:.2f}')
elif planeta == 4:
    print(f'Júpiter: {peso * 2.64:.2f}')
elif planeta == 5:
    print(f'Saturno: {peso * 1.15:.2f}')
elif planeta == 6:
    print(f'Urano: {peso * 1.17:.2f}')
