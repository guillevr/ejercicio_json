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
		break

	elif opcion ==1:
		print()
		print("\t--- Lista con los nombres de los pokemons y su evolucion ---")
		for pye in lista_pokemons_y_sus_evoluciones(datos):
			print(pye)

		print()

	elif opcion == 2:
		while True:
			print()
			print()
			print("\t------ MENU DE CONTAR ------")
			print()
			print("\t1. Número de pokemons que existen.")
			print("\t2. Número de pokemons que nacen de un huevo.")
			print("\t3. Número de tipos distintos de pokemons.")
			print("\t0. Salir del programa.")
			print()
			print("\t------------------------------")
			print()
			opcion=int(input("\tOpcion: "))

			if opcion==0:
				break

			elif opcion==1:
				print()
				print("\t--- Número de pokemons que existen ---")
				print()
				print("\t   Hay un total de %i pokemons registrados en la pokedex."%(num_pokemon(datos)))
				print()

			elif opcion==2:
				print()
				print("\t--- Número de pokemons que nacen de un huevo ---")
				print()
				print("\t   Hay %i pokemons que pueden nacer de un huevo."%(num_pokemon_pnd_huevo(datos)))
				print()

			elif opcion==3:
				print()
				print("\t--- Número de tipos distintos de pokemons ---")
				print()
				print("\t   Hay %i tipos distintos de pokemons."%(num_tipos_dpokemon(datos)))
				print()

			else:
				print("\tError, opción incorrecta.")

	elif opcion == 3:
		print()
		nom_pokemon=input("\tNombre del pokemon: ")
		print()

		if nom_pokemon not in lista_pokemons(datos):
			print("\tError, el pokemon %s no existe."%(nom_pokemon))
		else:

			tipos=" // "
			for t in tipos_del_pokemon(nom_pokemon,datos):
				tipos=tipos+t+" // "

			print("\t--- Los tipos del pokemon %s son:---"%(nom_pokemon))
			print()
			print("\t   %s"%(tipos))
			print()
		print()

	elif opcion == 4:
		print()
		tipo_pokemon=input("\tTipo del pokemon: ")

		print()
		if tipo_pokemon not in tipos_dpokemon(datos):
			print("\tError, no hay ningun pokemon que sea de tipo %s"%(tipo_pokemon))
		else:
			print("\t--- Pokemons cuyo tipo pertenece a %s ---"%(tipo_pokemon))

			pkms=" // "
			for t in pokemons_que_coinciden_con_el_tipo(tipo_pokemon,datos):
				pkms=pkms+t+" // "
			print()
			print("\t   %s"%(pkms))
		print()

	elif opcion == 5:
		print()
		print()

	else:
		print()
		print("\tError. opcion incorrecta")
		print()
