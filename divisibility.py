x=input("put first here  ")
y=input("put next here  ")
z=input("put next here  ")
a=input("put next here  ")
b=input("put next here  ")
num_list = [b, a, z, y, x]
print("Given list:", num_list)
print('Divisible by 5:')
for num in num_list:
    if num % 5 == 0:
        print(num)
