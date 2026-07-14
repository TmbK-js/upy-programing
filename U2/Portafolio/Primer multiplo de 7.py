numero = int(input("Introduce un número entero de inicio: "))

candidato = numero

while True:
    if candidato % 7 == 0:
        print(f"El primer múltiplo de 7 a partir de {numero} es: {candidato}")
        break  
    candidato += 1