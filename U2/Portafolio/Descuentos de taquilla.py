price= 150
age= int(input("ingresa laa edad: "))
id= input("cuenta con una tarjeta? (si/no): ")

if age < 12:
    reta= .30
elif age <= 25 and id == "si":
    rate = .20
elif age <=64:
    rate= 0.00
else:
    rate= 0.40
n_price= 150 * (1-rate)
print (f"price $: {price}")