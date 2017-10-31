n = int(input("Enter a number: "))
# solution1
# seq=range(n+1)
# result = sum(seq)
total = 0
for i in range(n+1):
    # total = total + i    or
    total +=i
print("Total is: ", total)
