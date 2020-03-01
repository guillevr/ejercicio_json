

## **Listar Informacion:** Mostrar el nombre de los pokemons junto con el nombre de sus evoluciones.

def lista_pokemon_y_sus_evoluciones(datos):

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



## **Contar Informacion:** ¿De que quieres contar informacion? (Dentro del programa habra un submenu en el que podras elegir que informacion quieres contar.)

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


## **Buscar o filtrar Informacion:** Pide el nombre de un pokemon y muestra su tipo.



## **Buscar informacion relacionada:** Mostrar el nombre de los pokemon cuyo tipo sea el introducido por teclado.



## **Ejercicio Libre:** Pide el nombre de un pokemon y muestra su numero en la pokedex, su nombre, su tipo, su peso, su tiempo de expansion y si tiene caramelo o no.
