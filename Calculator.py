print("This is a calculator")
num_1=input("Put first number here ")
operator=raw_input("Chose one of the main 4 operators Example:+,-,x,/ ")
num_2=input("Put next number here ")

if operator=="+":
    sum_=num_1+num_2
    print(sum_)
elif operator=="-":
    print(num_1-num_2)
elif operator=="x":
    print(num_1*num_2)
elif operator=="/":
    print(num_1/num_2)
else:
    print("Error: Please contact Aarav shringi.")
