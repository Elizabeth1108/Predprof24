from random import choice
fin=open('space.txt','r',encoding='utf-8')
title=fin.readline().strip()
#x[0]- назв корабля
#x[1]- назв планеты
#x[2]- координаты
#x[3]- направление

ships=[x.strip() for x in fin]

for i in range(len(ships)):
    x=ships[i].split('*')
    names=x[0].split('-')
    plan=x[1]
    nam=names[0]
    cod=names[1]
    cod=cod[::-1]
    p2=nam[(len(nam)//2)-1:len(nam)//2+1]
    p1=plan[-3:]
    nam1=plan[::-1]
    p3=nam1[-3:]
    
    password=p1+p2+p3
    ships[i]=ships[i]+'*'+password
fout=open('space_uniq_password.csv','w',encoding='utf-8')
fout.write(title+'*password'+'\n')

for x in ships:
    fout.write(x+'\n')
fout.close()
