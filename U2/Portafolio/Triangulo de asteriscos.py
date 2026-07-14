piramide= int(input("ingresa el numero de escalones que tendra la piramide: "))
p=0
while piramide > 0:
    n= piramide-1
    p += 1
    r = "* " * p
    nu= " " * n
    print (nu, r)
    piramide-=1