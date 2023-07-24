# Range function - start, end, step 
# start - from where we want to start the loop
# end - from where we want to end the loop. and it's not inclusive.
# step - how many steps we want to jump in every iteration. By default it's 1
for i in range(5):
    print (i)
print ('*'*10)

for i in range(-11, 5):
    print (i)    
print ('*'*10)

for i in range(5, 50, 5):
    print (i)
print ('*'*10)

# we can also loop over any list
fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print (fruit)
print ('*'*10)