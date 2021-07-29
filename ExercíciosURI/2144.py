final = 0.0
todos = 0
while True:
    w1, w2, r = map(int, input().split())
    
    if(w1 == w2 == r == 0):
        break

    if((w1 >= 1 and w1 <= 60) and (w2 >= 1 and w2 <= 100) and (r >= 1 and r <= 12)):
        m1 = w1* (1 + (r/30))
        m2 = w2* (1 + (r/30))

        media = float((m1 + m2)/2)
        final += media
        todos += 1

        if(0 < media and media < 13):
            print('Nao vai dar nao')
        elif(media >= 13 and media < 14):
            print('E 13')
        elif(media >= 14 and media < 40):
            print('Bora, hora do show! BIIR!')
        elif(media >= 40 and media <= 60):
            print('Ta saindo da jaula o monstro!')
        else:
            print('AQUI E BODYBUILDER!!')

mediaFinal = final/float(todos)
if(mediaFinal > 40):
    print()
    print('Aqui nois constroi fibra rapaz! Nao e agua com musculo!')