#WAP to print the elements of the following list using a loop [1,4,9,16,25,36,49,64,81,100]
list = [1,4,9,16,25,36,49,64,81,100]
for val in list:
    print(f"{val}")

#Search for a number x in this tuple using loop
tuple = tuple(list)
print(tuple)
num = int(input("Enter number to be searched:"))
for val in tuple:
    if val == num:
        print(f"{num} found")
        break
    print("Number not found")

#WAP to print numbers from 1 to 100
for val in range(1,101):
     print(val)

#WAP to print numbers from 100 to 1
for val in range(100,0,-1):
    print(val)

#WAP for multiplication table
num= int(input("Enter multiplication table:"))
for val in range(1,11):
    table = num * val
    print(f"{num}*{val} = {table}")

#WAP to find factorial of first n numbers
n = int(input("Enter factorial number:"))
fact = 1
for val in range(1, n+1):
    fact *= val
print("factorial = ", fact)
