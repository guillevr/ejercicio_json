



## 1. **Listar Informacion:** Mostrar el nombre de los pokemons junto con el nombre de sus evoluciones.

def lista_pokemons_y_sus_evoluciones(datos):

    ## pye --> lista con los pokemons y evoluciones

    pye=[]
    pye.append("")
    pye.append("")

    for pokemon in datos["pokemon"]:
    	npokemon="\t  %s"%(pokemon["name"])

    	if npokemon not in pye:

    		pye.append("\tNombre Pokemon:")
    		pye.append(npokemon)
    		pye.append("")
    		pye.append("\tEvoluciones: ")

    		try:

    			for evolucion in pokemon["next_evolution"]:

    				nevolucion="\t  %s"%(evolucion["name"])

    				if nevolucion not in pye:
    					pye.append(nevolucion)

    			pye.append("")
    			pye.append("     -----------------------------")
    			pye.append("")

    		except KeyError:

    			pye.append("\t   No tiene evolucion.")
    			pye.append("")
    			pye.append("     -----------------------------")
    			pye.append("")
    			pass

    return pye



## 2. **Contar Informacion:** ¿De que quieres contar informacion? (Dentro del programa habra un submenu en el que podras elegir que informacion quieres contar.)

## Contador de numero de pokemons que existen

def num_pokemon(datos):

    pokemons=[]

    for pokemon in datos["pokemon"]:

    	pokemons.append(pokemon["name"])

    return len(pokemons)


## Contador de numeros de pokemons que nacen de un huevo.

    ## pnd -> pueden nacer de
def num_pokemon_pnd_huevo(datos):

    pokemons=[]

    for pokemon in datos["pokemon"]:
        huevo=pokemon["egg"]

        if huevo != "Not in Eggs":
            pokemons.append(pokemon["name"])

    return len(pokemons)

## Contador de numero de tipos distintos

def num_tipos_dpokemon(datos):

    tipos=[]

    for pokemon in datos["pokemon"]:
        for tiposdpokemon in pokemon["type"]:
            if tiposdpokemon not in tipos:
                tipos.append(tiposdpokemon)

    return len(tipos)


## 3. **Buscar o filtrar Informacion:** Pide el nombre de un pokemon y muestra su tipo.

####### Para comprobar si el pokemon existe

def lista_pokemons(datos):

    pokemons=[]

    for pokemon in datos["pokemon"]:

    	pokemons.append(pokemon["name"])

    return pokemons

#############

def tipos_del_pokemon(nom_pokemon,datos):

    tipos_del_pokemon=[]

    for pokemon in datos["pokemon"]:
        npokemon=pokemon["name"]
        for tipo in pokemon["type"]:
            if npokemon==nom_pokemon:
                tipos_del_pokemon.append(tipo)

    return tipos_del_pokemon


## 4. **Buscar informacion relacionada:** Mostrar el nombre de los pokemon cuyo tipo sea el introducido por teclado.

####### Para comprobar si el tipo de pokemon existe

def tipos_dpokemon(datos):

    tipos=[]

    for pokemon in datos["pokemon"]:
        for tiposdpokemon in pokemon["type"]:
            if tiposdpokemon not in tipos:
                tipos.append(tiposdpokemon)

    return tipos

#############

def pokemons_que_coinciden_con_el_tipo(ntipo_pokemon,datos):

    pokemons=[]

    for pokemon in datos["pokemon"]:
        npokemon=pokemon["name"]
        for tipo in pokemon["type"]:
            if tipo==ntipo_pokemon:
                pokemons.append(npokemon)

    return pokemons

## 5. **Ejercicio Libre:** Pide el nombre de un pokemon y muestra su numero en la pokedex, su nombre, su tipo, su peso, su tiempo de expansion y si tiene caramelo o no.


def info_completa_pokemon(nombre_pokemon,datos):

    info=[]
    info.append("\t--- Información completa de la pokedex ---")

    for pokemon in datos["pokemon"]:
        npokemon=pokemon["name"]
        if npokemon==nombre_pokemon:
            info.append("\tNombre Pokemon %s: "%(npokemon))
            info.append("\tPokemon nº %s"%(pokemon["num"]))

            try:
                evoluciones=" // "
                for evolucion in pokemon["next_evolution"]:
                    nevolucion=evolucion["name"]
                    evoluciones=evoluciones+nevolucion+" // "
                info.append("\tEvoluciones %s"%(evoluciones))
            except KeyError:
                info.append("\tNo tiene evolucion/es")



            ## Añadir los tipos a los que pertenece el pokemon

            tipos=" // "
            for t in pokemon["type"]:
                tipos=tipos+t+" // "
            info.append("\tPokemon tipo %s"%(tipos))

            ########

            caramelo=pokemon["candy"]
            if caramelo != "None":
                info.append("\tNombre caramelo: %s"%(caramelo))
            else:
                info.append("\tNo tiene ningun caramelo.")

            info.append("\tAltura: %s"%(pokemon["height"]))
            info.append("\tPeso: %s"%(pokemon["weight"]))

            huevo=pokemon["egg"]
            if huevo != "Not in Eggs":
                info.append("\tEl huevo eclosiona tras andar %s."%(huevo))
            else:
                info.append("\tNo se encuentran en huevos.")

            ## Añadir debilidades

            debilidades=" // "
            for debilidad in pokemon["weaknesses"]:
                debilidades=debilidades+debilidad+" // "
            info.append("\tSon debiles ante los tipos %s"%(debilidades))
            info.append("")

            ########

    return info




################################################################################
############             MENU DEL PROGRAMA
################################################################################

from fmpokedex import *
def menu(datos):


    while True:

    	print()
    	print("                                   ,'\                                 ")
    	print("     _.----.        ____         ,'  _\   ___    ___     ____")
    	print(" _,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.")
    	print(" \      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |")
    	print("  \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |")
    	print("    \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |")
    	print("     \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |")
    	print("      \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |")
    	print("       \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |")
    	print("        \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |")
    	print("         \_.-'       |__|    `-._ |              '-.|     '-.| |   |")
    	print("                                 `'                            '-._|")

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

    		seguir=input("\t¿Quieres seguir en el programa?(S/N): ")

    		if seguir == "S" or seguir == "s" or seguir == "SI" or seguir == "Si" or seguir == "si":
    			print(menu(datos))
    		else:
    			break

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
    		seguir=input("\t¿Quieres seguir en el programa?(S/N): ")

    		if seguir == "S" or seguir == "s" or seguir == "SI" or seguir == "Si" or seguir == "si":
    			print(menu(datos))
    		else:
    			break

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
    		seguir=input("\t¿Quieres seguir en el programa?(S/N): ")

    		if seguir == "S" or seguir == "s" or seguir == "SI" or seguir == "Si" or seguir == "si":
    			print(menu(datos))
    		else:
    			break

    		print()

    	elif opcion == 5:
    		print()

    		nom_pokemon=input("\tNombre del pokemon: ")
    		print()

    		if nom_pokemon not in lista_pokemons(datos):
    			print("\tError, el pokemon %s no existe."%(nom_pokemon))
    		else:
    			for info in info_completa_pokemon(nom_pokemon,datos):
    				print(info)
    		seguir=input("\t¿Quieres seguir en el programa?(S/N): ")

    		if seguir == "S" or seguir == "s" or seguir == "SI" or seguir == "Si" or seguir == "si":
    			print(menu(datos))
    		else:
    			break

    		print()

    	else:
    		print()
    		print("\tError. opcion incorrecta")
    		print()
