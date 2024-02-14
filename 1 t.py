fin=open('space.txt','r',encoding='utf-8')
title=fin.readline()
#x[0]- назв корабля
#x[1]- назв планеты
#x[2]- координаты
#x[3]- направление
ships=[x.strip().split('*') for x in fin]

for x in ships:
    names=x[0].split('-')
    nam=names[0]
    cod=names[1]
    n=int(cod[0])
    m=int(cod[1])
    t=len(x[1])
    di=x[3].split(' ')
    xd=int(di[0])
    yd=int(di[1])
    if n>5:
        x1=n+xd
    if n<=5:
        x1=-(n+xd)*4+t
    if m>3:
        y1=m+yd+t
    if m<=3:
        y1=-(n+yd)*m
    coord=str(x1)+' '+str(y1)
    if x[2]=='0 0':
        x[2]=coord
fout=open('space_new.txt','w',encoding='utf-8')
fout.write(title)

for x in ships:
    s='*'.join(x)+'\n'
    fout.write(s)
    names1=x[0].split('-')
    if str(names1[0])[-1]=='V':
        x[2]=x[2].split(' ')
        print(names1[0],'-','(',x[2][0],',',x[2][1],')',sep='')
fout.close()
    
    
