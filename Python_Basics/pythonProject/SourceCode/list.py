#WAP to ask the user to enter names of their 3 favorite movies and store them in a list

movies=[]
movies.append(input("Enter movie name:"))
movies.append(input("Enter movie name:"))
movies.append(input("Enter movie name:"))
print(movies.sort())
print(movies)

#WAP to check if list is palindrome or not

list1 = [1,2,3,4,5]
list2 = [1,2,3,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()
if (list1 == copy_list1):
    print(f" {list1} Palindrome")
else:
    print(f" {list1} Not Palindrome")

copy_list2 = list2.copy()
copy_list2.reverse()
if (list2 == copy_list2):
    print(f" {list2} Palindrome")
else:
    print(f" {list2}Not Palindrome")

#WAP to count number of students with grade A in the following tuple ["C", "D", "A", "A", "B", "B", "A"]

grades= ("C", "D", "A", "A", "B", "B", "A")
print(grades.count("A"))
grade_list = list(grades)
grade_list.sort()
print(grade_list)

