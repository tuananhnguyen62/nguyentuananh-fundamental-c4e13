x = int(input("Enter a number: "))
divisor = 2
n = 0
while divisor < x:
    if x % divisor == 0:
        n += 1
        break
    else:
        divisor +=1
if n == 0:
    print("{} is a prime number".format(x))
else:
    print("{} is not a prime number".format(x))
