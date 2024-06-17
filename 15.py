from random import choice
from re import search

entrenadores = [
    {
        "nombre": "Ash Ketchum",
        "torneos_ganados": 7,
        "batallas_perdidas": 50,
        "batallas_ganadas": 120
    },
    {
        "nombre": "Goh",
        "torneos_ganados": 2,
        "batallas_perdidas": 10,
        "batallas_ganadas": 40
    },
    {
        "nombre": "Leon",
        "torneos_ganados": 10,
        "batallas_perdidas": 5,
        "batallas_ganadas": 100
    },
    {
        "nombre": "Chloe",
        "torneos_ganados": 1,
        "batallas_perdidas": 8,
        "batallas_ganadas": 30
    },
    {
        "nombre": "Raihan",
        "torneos_ganados": 4,
        "batallas_perdidas": 15,
        "batallas_ganadas": 60
    }
]

pokemons = [
    {
        "nombre": "Pikachu",
        "nivel": 35,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Pikachu",
        "nivel": 20,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Charizard",
        "nivel": 40,
        "tipo": "Fuego",
        "subtipo": "Volador"
    },
    {
        "nombre": "Bulbasaur",
        "nivel": 30,
        "tipo": "Planta",
        "subtipo": "Veneno"
    },
    {
        "nombre": "Starmie",
        "nivel": 30,
        "tipo": "Agua",
        "subtipo": "Psíquico"
    },
    {
        "nombre": "Psyduck",
        "nivel": 25,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Gyarados",
        "nivel": 35,
        "tipo": "Agua",
        "subtipo": "Volador"
    },
    {
        "nombre": "Onix",
        "nivel": 38,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Geodude",
        "nivel": 28,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Vulpix",
        "nivel": 20,
        "tipo": "Fuego",
        "subtipo": None
    },
    {
        "nombre": "Blastoise",
        "nivel": 50,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Umbreon",
        "nivel": 45,
        "tipo": "Siniestro",
        "subtipo": None
    },
    {
        "nombre": "Nidoking",
        "nivel": 40,
        "tipo": "Veneno",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Dragonite",
        "nivel": 55,
        "tipo": "Dragón",
        "subtipo": "Volador"
    },
    {
        "nombre": "Aerodactyl",
        "nivel": 52,
        "tipo": "Roca",
        "subtipo": "Volador"
    }
]

names = ["Ash Ketchum", "Goh", "Leon", "Chloe", "Raihan"]

lista_entrenadores = []

for entrenador in entrenadores:
    entrenador['pokemons'] = []
    lista_entrenadores.append(entrenador)

def cantidad_pokemons(entrenador):
    pos = search(lista_entrenadores, 0, entrenador)
    if pos is not None:
        return len(lista_entrenadores[pos][-1])
    else:
        return 0

def entrenadores_mas_de_tres_torneos(lista):
    result = []
    for entrenador in lista:
        if entrenador[1] > 3:
            result.append(entrenador[0])
    return result

def pokemon_mayor_nivel_entrenador_mas_torneos(lista):
    max_torneos = max(entrenador[1] for entrenador in lista)
    entrenadores_max_torneos = [entrenador for entrenador in lista if entrenador[1] == max_torneos]
    
    if entrenadores_max_torneos:
        max_nivel_pokemon = max(entrenador[-1], key=lambda pokemon: pokemon[1] if entrenador[-1] else [-1])
        return max_nivel_pokemon
    else:
        return None

def mostrar_datos_entrenador_y_pokemons(nombre):
    pos = search(lista_entrenadores, 0, nombre)
    if pos is not None:
        datos_entrenador = lista_entrenadores[pos]
        print(f"Datos del entrenador {nombre}:")
        print(f"Nombre: {datos_entrenador[0]}, Torneos ganados: {datos_entrenador[1]}, Batallas perdidas: {datos_entrenador[2]}, Batallas ganadas: {datos_entrenador[3]}")
        print("Pokémons:")
        for pokemon in datos_entrenador[-1]:
            print(f"  Nombre: {pokemon[0]}, Nivel: {pokemon[1]}, Tipo: {pokemon[2]}, Subtipo: {pokemon[3]}")
    else:
        print(f"El entrenador {nombre} no existe.")

def entrenadores_porcentaje_ganadas(lista):
    result = []
    for entrenador in lista:
        if entrenador[3] > 0:
            porcentaje_ganadas = (entrenador[3] / (entrenador[2] + entrenador[3])) * 100
            if porcentaje_ganadas > 79:
                result.append(entrenador[0])
    return result

def entrenadores_pokemon_tipos(lista):
    result = []
    for entrenador in lista:
        tiene_fuego_planta = False
        tiene_agua_volador = False
        for pokemon in entrenador[-1]:
            if pokemon[2] == "Fuego" and (pokemon[3] == "Planta" or pokemon[3] is None):
                tiene_fuego_planta = True
            if pokemon[2] == "Agua" and pokemon[3] == "Volador":
                tiene_agua_volador = True
        if tiene_fuego_planta and tiene_agua_volador:
            result.append(entrenador[0])
    return result

def promedio_nivel_pokemons(entrenador):
    pos = search(lista_entrenadores, 0, entrenador)
    if pos is not None:
        pokemons_entrenador = lista_entrenadores[pos][-1]
        if pokemons_entrenador:
            promedio = sum(pokemon[1] for pokemon in pokemons_entrenador) / len(pokemons_entrenador)
            return promedio
        else:
            return 0
    else:
        return 0

def cantidad_entrenadores_con_pokemon(nombre_pokemon):
    count = 0
    for entrenador in lista_entrenadores:
        for pokemon in entrenador[-1]:
            if pokemon[0] == nombre_pokemon:
                count += 1
                break
    return count

def entrenadores_con_pokemons_repetidos(lista):
    result = []
    for entrenador in lista:
        nombres_pokemons = set()
        tiene_repetidos = False
        for pokemon in entrenador[-1]:
            if pokemon[0] in nombres_pokemons:
                tiene_repetidos = True
                break
            nombres_pokemons.add(pokemon[0])
        if tiene_repetidos:
            result.append(entrenador[0])
    return result

def entrenadores_con_pokemon_especifico(pokemon):
    result = []
    for entrenador in lista_entrenadores:
        for poke in entrenador[-1]:
            if poke[0] == pokemon:
                result.append(entrenador[0])
                break
    return result

def tiene_entrenador_pokemon(entrenador, pokemon):
    pos_entrenador = search(lista_entrenadores, 0, entrenador)
    if pos_entrenador is not None:
        for poke in lista_entrenadores[pos_entrenador][-1]:
            if poke[0] == pokemon:
                print(f"El entrenador {entrenador} tiene al Pokémon {pokemon}:")