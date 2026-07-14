#IMC

weight= float(input("ingrese su peso: "))
height= float (input("ingrese su altura: "))
IMC = weight / (height*heignt)
if IMC < 18.5:
    print("estas desnutrido")
elif IMC <= 25:
    print("estas en un peso saludable")
elif IMC <= 30:
    print("estas gordito")
else:
    print("estas majin boo")