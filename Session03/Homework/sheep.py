# 2.1 Create a flock of sheep

size_list = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is TAnh and these are my sheep sizes: ")
print(size_list)

#2.2 Find the max value in the list
max_size = max(size_list)
print("Now my biggest sheep has size {0} let's shear it" .format(max(size_list)))

#2.3 Change the value of max
size_list[size_list.index(max(size_list))] = 8
print("After shearing, here is my flock: ")
print(size_list)
print("*" *40)
#2.4 + 2.5 Increasing each item in the list to 50 with several months
month = int(input("How many months you want? "))
for j in range (1, month + 1) :
    print("{0} months have passed, now here is my flock:" .format(j))
    for i in range (len(size_list)):
        size_list[i] += 50
    print(size_list)
