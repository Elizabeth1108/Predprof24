fin=open('space.txt','r',encoding='utf-8')
title=fin.readline()
#x[0]- назв корабля
#x[1]- назв планеты
#x[2]- координаты
#x[3]- направление

ships=[x.strip().split('*') for x in fin]

while True:
    n=input('Введите название корабля(или stop):')
    if n=='stop':
        break
    for x in ships:
        names=x[0].split('-')
        nam=names[0]
        plant=x[1]
        di=x[3]
        if nam==n:
            print('Корабль',nam,'был отравлен с планеты',plant,'и его направление движения было:',di)
            break
    else:
        print('error.. er.. ror..')
