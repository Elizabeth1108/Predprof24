fin=open('space.txt','r',encoding='utf-8')
title=fin.readline()
#x[0]- назв корабля
#x[1]- назв планеты
#x[2]- координаты
#x[3]- направление
ships=[x.strip().split('*') for x in fin]
def hashstr(st):
        '''
        Функция выводит хэш строки
        :param(st):(str)Название планеты
        :return:(str)хэш названия планеты
        '''
        d={}
        alfabet='йцукенгшщзхъфывапролджэячсмитьбю ЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТБЮ'
        p=68
        m=10**9+9
        hashname=0
        for ind,simb in enumerate(alfabet,1):
            d[simb]=ind
        for i in range(len(st)):
            hashname+=d[st[i]]*p**i
        return hashname%m
cnt=0   
for x in ships:
   print(x[1],':',hashstr(x[1]))
   cnt+=1
   if cnt==10:
       break
   
        
    
