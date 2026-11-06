def emeralds(N, weight):
    x=[]
    y=0
    for i in range(N):
        
        if weight[i] % 2 == 0:
            y += weight[i]
        elif weight[i] % 2 ==1:
            x.append(y)
            y=0
    x.append(y)
    print(f"the max weight u can buy is {max(x)} pounds")
emeralds(13,[2,3,4,4,5,6,1,2,2,2,1,8,2])