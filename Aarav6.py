#Write a Python program that calculates the area of a square based on the numbers entered by the user.
print("Give me 2 sides of a square or rectangle and I will tell you the area ")
x=input("1st number here ")
y=input("Next number here ")
if x==y:
    print(x*x)
elif x>y or x<y:
    print(x*y)
else:
    print("error")