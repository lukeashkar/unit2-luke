def spaces(N, yes, today):
    hi = 0
    for i in range (N):
        if yes[i]=="C" and today[i]=="C":
            hi+=1
    print(hi)
spaces(7, "CCCCCCC", "C0C0C0C")
