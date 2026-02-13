# input

min = int(input("Digite la duracion de la llamada en minutos: "))

# Processing 

if (min <= 3):
    costo_llamada = 500
else:
    costo_llamada = 500 + (min-3)*100


    print("-----------------------------------")
    print("--------- Resultado ---------------")
    print("-----------------------------------")
    print("Duración de la llamada: " + str(min) + " minutos")
    print("Costo de la llamada: " + str(costo_llamada))