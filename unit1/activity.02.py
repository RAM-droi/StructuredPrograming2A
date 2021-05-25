cantidad = int(input("ingrese cantidad: "))

cant500 = cantidad
resto500 = cantidad % 500

cant200 = resto500
resto200 = resto500 % 200

cant100 = resto200
resto100 = resto200 % 100

print("cant de billetes de 500: ", cant500)
print("cant de billetes de 200: ", cant200)
print("cant de billetes de 100: ", cant100)