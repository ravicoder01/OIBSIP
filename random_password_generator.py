import random
import string

print("\t\t\tRANDOM PASSWORD GENERATOR\n")
n=True
while n==True:
    z=int(input("what length of password you want to create? \n"))
    a=int(input("Enter how many letters:"))
    b=int(input("Enter how many numeric character to include: "))
    c=int(input("Enter how many special symbol:"))

    if (a+b+c)>z:
        print(f"The total number of characters must be exactly {z}!\n")
        n= True
    elif (a+b+c)<z:
         print(f"The total number of characters must be exactly {z}!\n")
         n= True
    else:
        n=False         

password=''

letter=[random.choice(string.ascii_letters) for i in range(a)]
numbers=[random.choice(string.digits) for i in range(b)]
alpha_no=[random.choice(string.punctuation) for i in range(c)]  
collection=letter+numbers+alpha_no

random.shuffle(collection)

for i in collection:
    password+=i

print("your random password generated is :",password)    
n=True



