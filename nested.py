# # nested for loop
# for i in range(1, 6):
#     # print ("Hello Aarav, I am in outer loop.,", i)
#     print (i)
#     for j in range(1, 6):
#         print (j)
#         # print ('I am in inner nested loop ', j)

# example 2
# nested for loop
for i in range(1, 6):
    for j in range(1, 6):
        print (i, j)
        if j == 3:
            break

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1
