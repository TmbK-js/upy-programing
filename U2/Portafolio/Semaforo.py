#semaforo
color= input("ingresa un color: ").lower()
if color == "red":
    print("stop")
elif color== "green":
    print("go")
elif color== "yellow":
    print("warning")
else:
    print("invalid")