# Programa para verificar si los dos ultimos digitos de un número son iguales

# input
print("-------------------------------------")
print("---- Ultimos digitos iguales --------")
print("-------------------------------------")
x = int(input("Digite un número: "))

# processing
ultimo_digito = x % 10
penultimo_digito == (x//10)%10
if (ultimo_digito == penultimo_digito):
    rta = "IGUALES"
else:
    rta = "DIFERENTES"

# output
print("--------------------------------------")
print("---------- Resultado -----------------")
print("--------------------------------------")
print("El número ingresado fue: " + str(x))
print("Su ultimo digito es: " + str(ultimo_digito))
print("Su penultimo digito es: " str(penultimo_digito))
print("Los dos ultimos digitos son: " rta)