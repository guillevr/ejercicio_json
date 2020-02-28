import json

from fmpokedex import *

with open("pokedex.json") as fichero:
	datos=json.load(fichero)

while True:
    print()
    print()
    print("\t------ MENU DE OPCIONES ------")
    print()
    print("\t1. Listar informacion.")
    print("\t2. Contar informacion.")
    print("\t3. Buscar o filtrar informacion.")
    print("\t4. Buscar informacion relacionada.")
    print("\t5. Ejercicio libre.")
    print("\t0. Salir del programa.")
    print()
    print("\t------------------------------")
    print()
    opcion=int(input("\tOpcion: "))

    if opcion ==0:
        break;

    elif opcion ==1:
        print()
        print("\t--- Lista con los nombres de los pokemons y su evolucion ---")
        for pye in lista_pokemon_y_sus_evoluciones(datos):
            print(pye)
        print()

    elif opcion == 2:
        print()

        print()

    elif opcion == 3:
        print()

        print()

    elif opcion == 4:
        print()

        print()

    elif opcion == 5:
        print()

        print()
    else:
        print()
        print("\tError. opcion incorrecta")
        print()
