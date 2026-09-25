""" bill=float(input( "how much the bill bro."))
tip=int(input("how much you tipping"))
print(bill+tip)
print(f"your total is {bill+tip} you better pay up") """


#make a code using the input to make them say a sentence
#use the len and .split to make it so they count words
""" 
sentence= input("enter a sentence")
word_count=len(sentence.split())
print(word_count) """

""" odd_or_even=int(input("pick a number"))

if int(odd_or_even%2==0):
    print("even")
elif (odd_or_even%2==1):
    print("odd") """
""" else:
    print("ima slime u out") """

""" bill=float(input("What is the bill?"))
service=int(input("Rate the service from 1-4"))
if service==1:
    print("We recommend not tipping/ tipping 0 percent.")
elif service==2:
    print("We recommend tipping 15 percent.")
elif service==3:
    print("We recommend tipping 20 percent.")
elif service==4:
    print("We recommend tipping 25 percent.")
else:
    print("We said rate 1-4 we jus gon rob u now.") """

""" number=int(input("pick a number: "))
for i in range(1, number + 1):
    if number % (i) == 0:
        print(i) """

n1=int(input("Give me a number"))
n2=int(input("Give me another number"))
def factor(x, y):
    factorlist = []
    for i in range(1,n1+1):
        if x % (i) ==0 and y % (i) ==0:
            factorlist.append(i)
    print(factorlist[-1])
factor(n1, n2)