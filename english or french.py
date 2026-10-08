def language(n, sent):
    s=0
    t=0
    for i in range(n):
        if sent[i].lower() =="s":
            s+=1
        if sent[i].lower() =="t":
            t+=1
    print(t,s)
    if t > s:
        print("this is prolly english")
    else:
        print("this is prolly french")
language(14,"die you triangle")