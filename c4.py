

val = int(input())
if val < 10:
    if val != 5:
        print('wow',end='')
        
    else:
        val +=1
        
else:
    if val == 17:
        val+= 10
        
    else:
        print('whoo',end='')
        print(val)
        
        '''
        (a)3 == wow
        (b)21 == whoo21
        (c)5 ==   #(nothing)
        (d)17 ==   #(nothing)
        (e)-5 == wow
        
        '''