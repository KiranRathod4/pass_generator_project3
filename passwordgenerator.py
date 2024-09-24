import random 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!','@','#', '$', '%', '^', '&', '*','(',')']

print("welcome to password generator!")

n_letters = int(input("How many letters would you like?\n"))
n_numbers = int(input("How many number would you like ?\n"))
n_symbols = int(input("How many symbols would you like?\n")) 

password_list = []                            #password_list = []: This creates an empty list where random characters (letters, numbers, and symbols) will be stored as we build the password.

for i in range (1,n_letters+1):#1, 2, 3, 4
    char=random.choice(letters)
    password_list+=char 
    
for i in range (1, n_numbers+1):
    num=random.choice(numbers)
    password_list+= num
    
for i in range(1,n_symbols+1): 
    sym=random.choice(symbols)
    password_list+= sym
    
print(password_list)
random.shuffle(password_list)

password=""                                        #Initializes an empty string called password.
for i in password_list:                            #This loop iterates through each character in password_list
    password += i                                  # concatinates characters of i from the shuffle list
print(f'your password is :{password}')


'''
example output:


welcome to password generator!
How many letters would you like?
4
How many number would you like ?
2
How many symbols would you like?
2
['B', 'm', 'Q', 'z', '6', '2', '@', '!']
your  password is :@!zmQ62B 

'''