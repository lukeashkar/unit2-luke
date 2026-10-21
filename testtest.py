def casino(m,slots):
    played=0
    while m > 0:
        
        if slots[0] < 35:
            played+=1
            slots[0]+=1
            m-=1
        elif slots[0] == 35:
            m+=29
            played+=1
            slots[0]=0
        if slots[1] < 100:
            played+=1
            slots[1]+=1
            m-=1
        elif slots[1] == 100:
            m+=59
            played+=1
            slots[1]=0
        if slots[2] < 10:
            played+=1
            slots[2]+=1
            m-=1
        elif slots[2] == 10:
            m+=8
            played+=1 
            slots[2]=0
        
     
    print(played)
casino(48,[3,10,4])