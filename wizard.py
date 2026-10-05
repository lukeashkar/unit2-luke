def wizards(N, start, duels):
    owner=start
    changed_hands= 1
    """ print(duels[0][1]) """
    x=0
    y=1
    for i in range(N):   
        if owner== duels[x][y]:
            owner==duels[x][x]    
            changed_hands+=1
        x+=1
        y+=1





    wizards(3, "A", ["BA","CB","DA"])