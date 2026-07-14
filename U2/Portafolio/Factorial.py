n = int(input("Ingrese un número para calcular su factorial: "))
fc = 1
i = n
while i > 0:
        fc = fc * i
        i = i - 1
    
print(f"El factorial de {n} es: {fc}")