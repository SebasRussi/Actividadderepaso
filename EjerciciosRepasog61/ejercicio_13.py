numero1 = int(input("ingrese numero 1 "))
numero2 = int(input("ingrese numero 2 "))

suma = numero1 + numero2
resta = numero1 - numero2
multi = numero1 * numero2
div = numero1 / numero2

mensaje = f"""
para los numeros {numero1} y {numero2},
el resultado de la suma es {suma}.
el resultado de la resta es {resta}.
el resultado de la multiplicacion es {multi}.
el resultado de la division es {div}.
"""
print(mensaje)