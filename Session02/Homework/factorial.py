n = int(input("Nhap so n: "))
f = 1
if n > 0:
    for i in range(1, n+1):
        f = f * i
    print("Giai thua cua n la: ", f)
else:
    print("Vui long nhap lai so nguyen duong")
