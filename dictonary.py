store = [
        {
            "name":"mcchicken",
            "price":int(43.99),
            "department":"Food",
            "description":"A mcdonalds mcchicken, the only thing there for you when you get divorced, graduate college, when your hungry, want mcdonalds, get a girfriend, when your dog dies, and when you die."
        },
        {
            "name":"russia",
            "price":int(24.99),
            "department":"countries",
            "desription":"bro someone buy this country so i dont gotta do russian homework anymore"
        },
        {
            "name":"ton 618",
            "price":float(0.84),
            "department":"blackholes",
            "description":"a blackhole with estimates of 40 to 66 billion solar mass for a cheap price of 84 cents "
        },
        {
            "name":"hank",
            "price": float(0.1),
            "department":"people",
            "description":"its hank"
        },
        {
             "name":"emperor of worlds, the one who controls the balance in the universe, the one who pierces the heavens, the one who the impossible becomes possible for, simon.",
             "price": int(1000),
             "departments":"people",
             "description":"yo i pretty much did this in the name already just buy him"
        }
        ]
def dictonary(items):
    for index, item in enumerate(items):
            print(index, ":", item["name"]) 
dictonary(store)
def p():
    purchased=int(input("which item do u want"))
    confirmation = input(f"are you sure you wanna buy {store[purchased]['name']} for {store[purchased]['price']} dollars ? (respond with yes or no caps do matter here also DO NOT put a space before typing your answer) -")
    if confirmation== "yes":
         print("alr thanks for shopping hope you come back eventually")
    else:
         print("why did bro just waste my time")


p()
































