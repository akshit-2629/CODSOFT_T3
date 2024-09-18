import random
letters = ['a', 'b', 'c',  'd' , 'e' , 'f', 'g','h','i','k','1','m', 'n', 'o', 'p' , 'q', 'r' , 's' ,'t','u', 'v', 'w','x','y', 'z' , 'A', 'B','C', 'D','E','F','G','H','I','J','K', 'L', 'M','N', 'O', 'P', 'Q', 'R','S', 'T','U','V','W','X','Y','Z']


numbers = ['0','1','2','3','4','5','6', '7','8','9']

symbols = ['!','#','$' ,'응','*','+' , '@']

n = int(input("enter the number of characters : "))
password = " "
for char in range(n) :
 random_character = random.choice(letters + numbers + symbols)

 password += random_character

print(password)