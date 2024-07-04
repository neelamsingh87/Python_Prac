#WAP to print numbers from 1 to 100
count = 1
while count <= 100:
    print(count)
    count += 1

#WAP to print numbers from 100 to 1
count = 100
while count >= 1:
    print(count)
    count -= 1

#WAP to print multiplication table of number
num = int(input("Enter multiplication number:"))
count = 1
while count <= 10:
    table = num * count
    print(f"{num}*{count}={table}")
    count += 1

#WAP to print elements of the following list using loop
list = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i < len(list):
    print(list[i])
    i += 1

#WAP to search for a number x in this tuple using loop
tuple = (1,4,9,16,25,36,49,64,81,100)
find_num = int(input("Enter number to be searched in the tuple:"))
i = 0
while i < len(tuple):
    if find_num == tuple[i]:
        print(f"{find_num} found in the tuple")
        break
    i += 1
    print(f"{find_num} not found in the tuple")

#WAP to print even numbers using continue
i=1
while i <= 10:
    if i%2 != 0:
        i += 1
        continue #Skip
    print(f" Even Numbers: {i}")
    i += 1

#WAP to find sum of first n numbers (using while)
num = [2,7,1,8]
i = 0
sum = 0
while i < len(num):
    sum += num[i]
    i += 1
print(sum)
