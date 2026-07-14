texto = input("Introduce una palabra o frase: ")
vocales = "aeiouAEIOU"
contador = 0

for caracter in texto:
    if caracter in vocales:
        contador += 1  

print(f"La frase/palabra tiene un total de {contador} vocales.")