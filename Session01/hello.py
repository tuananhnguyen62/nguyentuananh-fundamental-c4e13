print("Giai phuong trinh bac 2")
a = int(input("Nhap a:"))
b = int(input("Nhap b:"))
c = int(input("Nhap c:"))
if a==0:
        x=-c/b
        print("Day la phuong trinh bac 1 co nghiem x la",x)
else:
    e = b*b-4*a*c
    a_2=a*2
    if e<0:
        print("Phuong trinh vo nghiem")
    elif e==0:
        x=-b/a-2
        print("Phuong trinh co nghiem kep", x)
    else:
        x1=(-b+e**0.5)/a_2
        x2=(-b-e**0.5)/a_2
        print("Phuong trinh co 2 nghiem: x1={0}, x2={1}".format(x1,x2,10))
