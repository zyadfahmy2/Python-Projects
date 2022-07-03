# 1- import String library
# 2- store all characters in lists
# 3- take number of characters from user
# 4-  shuffle all the lists
# 5- calculate 30% and 20% for number of characters
# 6- create password 60% letters and 40% digits and punctuation
import string
import random

l1 = list(string.ascii_uppercase)
l2 = list(string.ascii_lowercase)
l3 = list(string.digits)
l4 = list(string.punctuation)

in1 = input("Enter number of characters")

while True:
    try:
        in1 = int(in1)  # converting in1 to integer since it was a string
        if in1 < 6:
            print("password need to be at least 6 characters\n")
            in1 = input("Enter number of characters")
        else:
            break
    except:
        print("number of characters must be digits")
random.shuffle(l1)
random.shuffle(l2)
random.shuffle(l3)
random.shuffle(l4)
percentage30 = round(in1 * 30/100)
percentage20 = round(in1 * 20/100)
print(percentage30)
password =[]
for index in range(percentage30):
    password.append(l1[index])
    password.append(l2[index])


for index in range(percentage20):
    password.append(l3[index])
    password.append(l4[index])


random.shuffle(password)
password = "".join(password[0:]) #converting the list to a string
print(password)