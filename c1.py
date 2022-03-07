print('welcome to tax calculator mochin')
x = int(input('please enter income number ='))
if x<=1000:
    
    print('final earning =',x)
elif 1000 < x <=2500: 
    print('final earning =',x-((x*10)/100))
elif 2500 < x <=4000:
    
    print('final earning =',x-((x*15)/100))
elif 4000 < x <= 6000 :
    
    print('final earning =',x-((x*20)/100))
elif 6000 < x<=8000 :
    print('final earning =',x-((x*25)/100))
    
else:
    print('final earning =',x-((x*30)/100))

  

    
 
    
