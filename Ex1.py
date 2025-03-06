#program to find the greates of three numbers
#Input: Reading three numbers from the user
a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))
c = float(input("Enter the third number:"))
#Logic: Finding The greates number
if a>=b and a>=c:
    greatest=a
elif b >=a and b >=c:
    greatest=b
else:
    greatest=c
    #Output: Display the greates number
    print(f"The greatest number among {a}, {b},and {c} is {greatest}.")