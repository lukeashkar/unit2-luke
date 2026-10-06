def wizards(N, start, duels):
    owner=start
    changed_hands= 1
    
    for i in range(N):   
        if duels[i][1]==owner:
                owner=duels[i][0]    
                changed_hands+=1
    print(owner,changed_hands)

wizards(3, "A", ["BA","CB","DA"])