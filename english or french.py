def language():
    sentence= int(input("make a sentence"))
    en=0
    fr=0
    english= "t" or "T"
    french= "S" or "s"
    for i in sentence():
        if english in sentence:
            en+=1
        if french in sentence:
            fr+=1
        if en>fr:
            print("your sentence is most likely english")
        if fr>en:
            print("your sentence is most likely french")
language()