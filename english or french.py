def language(sentence):
    en=0    
    fr=0
    let= "t"
    letter= "T"
    wi= "S"
    wiwi="s"
    for i in range (len(sentence)):
        if let in sentence or letter in sentence:
            en+=1

    for i in range (len(sentence)):
        if wi in sentence or wiwi in sentence:
            fr+=1

        if en>fr:
            print("english")

        elif fr>en:
            print("french")
language("The red cat sat on the mat. Why are you so sad cat? Don't ask that.")            