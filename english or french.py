def language(sentence):
    en=0    
    fr=0
    let= "t"
    letter= "T"
    wi= "S"
    wiwi="s"
    for i in range (len(sentence)):
        if let or letter in sentence:
            en+=1

    for i in range (len(sentence)):
        if wi or wiwi in sentence:
            fr+=1

        if en>fr:
            print("english")

        elif fr>en:
            print("french")
language("Lorsque j'avais six ans j'ai vu, une fois,une magnifique image,dans un livre")            