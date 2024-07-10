import random
import string

print("\t\t\tRANDOM PASSWORD GENERATOR\n")
a =int(input("Enter how many letters:"))
b=int(input("Enter how many numbers: "))
c=int(input("Enter how many special symbol:"))
password=''

letter=[random.choice(string.ascii_letters) for i in range(a)]

numbers=[random.choice(string.digits) for i in range(b)]

alpha_no=[random.choice(string.punctuation) for i in range(c)]  

collection=letter+numbers+alpha_no
random.shuffle(collection)

for i in collection:
    password+=i

print("your random password generated is :",password)    



