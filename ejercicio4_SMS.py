print()
print("Introduce los centimetros para conocer a cuantos kens y shakus equivale")
print("-----------------------------------------------------------------------")
centimetros = float(input("Introduce los centimetros: "))
shaku = centimetros / 30.3 
ken = shaku / 6
print(f"Se han introducido: {centimetros} centimetros")
print(f"equivale a {round(shaku,2)} shakus")
print(f"equivale a {round(ken,2)} kens")
print()