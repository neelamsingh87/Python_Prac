#WAP to check if a number entered by user is even or odd
#WAP to find greatest of 3 numbers entered by the user
#WAP to check if a number is multiple of 7 or not

#Even or ODD
num = int(input("Enter number:"))

if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

#Greatest of the 3 number
num1= int(input("Enter first number"))
num2= int(input("Enter second number"))
num3= int(input("Enter third number"))

if (num1 >= num2) and (num1 >=num3):
    print(f" {num1} is the greatest")
elif num2 >= num3:
    print(f" {num2} is the greatest")
else:
    print(f"{num3} is the greatest")


#Multiple of 7 or not
num = int(input("Enter number:"))

if num%7 == 0:
    print(f"{num} is multiple of 7")
else:
    print(f"{num} is not multiple of 7")



