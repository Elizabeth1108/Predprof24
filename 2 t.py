fin=open('space.txt','r',encoding='utf-8')
title=fin.readline()
#x[0]- назв корабля
#x[1]- назв планеты
#x[2]- координаты
#x[3]- направление
ships=[x.strip().split('*') for x in fin]

for i in range(1,len(ships)):
    for j in range(i,0,-1):
        x=ships[j]
        names=x[0].split('-')
        nam=names[0]
        cod=names[1]
        
        if ships[j][3]<ships[j-1][3]:
            ships[j][3],ships[j-1][3]=ships[j][3],ships[j-1][3]
cnt=0
for x in ships:
    nam=x[0].split('-')
    print(nam[0])
    cnt+=1
    if cnt==10:
        break
    
        
