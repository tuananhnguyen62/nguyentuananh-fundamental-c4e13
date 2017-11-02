m = int(input("Your weight in kg: "))
n = int(input("Your height in cm: "))/ 100
b = m / (n*n)
print("Your body condition is:")
if b < 16:
    print("Severely underweight")
elif b < 18.5:
    print("Underweight")
elif b < 25:
    print("Normal")
elif b < 30:
    print("Overweight")
else:
    print("Obese")
