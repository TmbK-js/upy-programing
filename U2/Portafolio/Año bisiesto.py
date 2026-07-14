#año biciesto

year= int(input("ingresa un año: "))
if (year % 4 ==0 and year % 100 != 0) or (year % 400 == 0 ):
    print(f"lap year {year}")
else:
    print("nain")
