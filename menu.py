import os  
import random  

def Mad_Story():
    import prueba_2

def Otros_juegos(): #funcion para los otros juegos
    menu2=''' 
1. Juego_snake
2. Atras
Ingrese una opción: '''
    elegir_alternativa=int(input(menu2)) 
    if elegir_alternativa=='1':
        juego_snake()# se llama a funcion juego_snake
    elif elegir_alternativa == '2':
        regresar()
    else:
        print("Ingrese un numero valido")
        elegir_alternativa=int(input(menu2))
def juego_snake():
    import juego_snake
    return juego_snake

def prepararPalabra(original):#
    global palabraAdivinada#para actualizar la variable
    original = original.lower()#Convertimos la palabra a minusculas
    palabraAdivinada = []#lista de la palabra adivinada
    for letra in original:#iteramos en la palabra elegidad(cadena)
        palabraAdivinada.append({ #utilizaremos diccionario para añadir a la lista de palabras adivinadas
            "letra": letra,#si en el caso que fueran iguales las letras de la palabra adivinada
            "adivinada": False,#si las letra de la palabra ingresada son diferentes de las letras de la palabra adivinada.
        })

def letraEstaEnPalabra(letra):
# creamos una función que se llama ltra en palabra con un parametro que se llama letra
    global palabraAdivinada
# aca esta llamando a la palabra adivinada que se encuentra fuera de la función
    for letraCompuesta in palabraAdivinada:
# para cada letra compuesta en palabra adivinada
        if letraCompuesta["letra"] == letra:
# si mi letra compuesta es igual a letra
            return True
# retorna la letra
    return False
# caso contrario no la retorna


def descubrirLetra(letraDeUsuario):
    global contador
# estamos definiendo una función que se llama descubrir letra con un parametro que se denomina letra de usuario
    global palabraAdivinada
# aca esta llamando a la palabra adivinada que se encuentra fuera de la función
    global letrasEscritas
# aca esta llamando a la palabra letras escritas que se encuentra fuera de la función
    global intentos
# aca se esta llamando a la palabra intentos que se encuetra fuera de la fucnión
    letraDeUsuario = letraDeUsuario.lower() #Convertimos las letras a minusculas
    if letraDeUsuario in letrasEscritas:    #si letra de usuario esta en letras escritas
        return                              #retornas el valor
    else:
        letrasEscritas.append(letraDeUsuario)#Si noagregamos letras de usuario a letras escritas
    if not letraEstaEnPalabra(letraDeUsuario):#Si la letra no esta en la palabra                                                    pierdes un intento
        intentos -= 1
        contador -=10
    else:
        for letraCompuesta in palabraAdivinada: # Sino iteramos cada letra compuesta en palabra adivinada
            if letraCompuesta["letra"] == letraDeUsuario: #si letra compuesta es igual                                                    a letra de usuario 
                letraCompuesta["adivinada"] = True  #entonces letra compuesta es letra adivinada es verdadero


def imprimirPalabra():
# creamos una función que se llama imprimir palabra con parametro vacio
    for letraCompuesta in palabraAdivinada:
# luego iteramos para cada letra compuesta en palabra adivinada
        if letraCompuesta["adivinada"]:
# si mi letra es compuesta
            print(letraCompuesta["letra"], end="")
# se va a imprimir la letra compuesta en una sola linea
        else:
# caso contrario que no sea compuesta
            print("-", end="")
# se imprimira un guión en la misma linea
    print("")
# se imprime una linea vacia, como un salto de linea


def imprimirPalabraOriginal():
    for letraCompuesta in palabraAdivinada:  #iteramos letra compuesta en palabra adivinada
        print(letraCompuesta["letra"], end="") #imprimimos letra compuesta


def haGanado():
    global palabraAdivinada
    for letra in palabraAdivinada: #iteramos letra en palabra adivinada
        if not letra["adivinada"]:#si la letra no es adivinada 
            return False          #retornas false
    return True
    #retornas true

def imprimirAhorcado():
# Creamos una función que se llama imprimir ahorcado con parametro vacio.
# cada vez que el usuario ingrese una letra que no pertenesca a la palabra indicada que se encontrara en el archivo txt, se le aumentara partes de su cuerpo que indicara que llegara su muerte(o sea se ahorcara)
    if intentos == 1:
# cuando la cantidad de mis intento sea igual a uno, se imprime todo el muñeco.

        print("""
                       _
                      |   |
                     _O/  |
                      |   |
                     / \  |
                    __|
        """)
    elif intentos == 2:
# cuando la cantidad de mis intentos sea igual a dos, me imprime el muñeco con una sola pata.
        print("""
                       _
                      |   |
                     _O/  |
                      |   |
                       \  |
                    __|
        """)
    elif intentos == 3:
# cuando la cantidad de mis intento sea igual 3, me imprime el muñeco de abajo.

        print("""
                       _
                      |   |
                     _O/  |
                      |   |
                          |
                    __|
        """)
    elif intentos == 4:
#cuando la cantidad de mis intentos sea igual a 4 me imprime ese muñeco de abajo.
        print("""
                       _
                      |   |
                     _O/  |
                          |
                          |
                    __|
        """)
    elif intentos == 5:
# cuando la cantidad de mis intentos se igual a 5 me imprime ese muñeco.
        print("""
                       _
                      |   |
                      O/  |
                          |
                          |
                    __|
        """)
    elif intentos == 6:
# yo cuando empieze a jugar, estare empezando con 6 intentos.
        print("""
                       _
                      |   |
                      O   |
                          |
                          |
                    __|
        """)


def dibujarIntentos():
# Creamos una función que se llama dibujar intentos con un parametro vacio
    print("Intentos restantes: " + str(intentos))
# realizamos una cadena, donde se va a imprimir intentos restantes mas la cantidad de intentos.


def regresar(): #funcionque permite regresar al menu principal
    global regresar #fincion global que permite que la funcion se puede usar fuera de esta
    Regresar = menu_principal()#Variable regresar para poder llamar a la funcion menu_principal
    return Regresar #retorna la variable


def imprimirGruposYSolicitarIndice(grupos):
    for i, categorias in enumerate(grupos):#enumeramos  las categorias con la funcion enumerate 
        print(f"{i + 1}. {categorias}")#como i emepezara desde cero , aumentamos mas 1 , y asi sucesivamente en categorias
    print("5. Atrás")


    ingresar=input("Selecciona una categoria para jugar >> ")
    while ingresar not in '123456':
        ingresar=input("Selecciona una categoria para jugar >> ")
        



    ingresar = int(ingresar)-1#ingresar categoria
    if ingresar + 1  == 5: #si es igual a 5 ira a la funcion regresar
        print('Regresar')
        regresar()
    while ingresar <= -1 or ingresar + 1 > 5:#si ingresa un numero mayor o ngeativo , tendra que ingresar de nuevo l
        print('Ingrese una opcion válida')
        ingresar = int(input("Selecciona una categoria para jugar >> "))-1

    return ingresar


def obtenerPalabrasDeGrupo(categorias):
# creamos una función que se llama obtener palabras de grupo con un parametro que se denomia categorias
    palabras = []
# creamos una lista vacia que se llama palabras
    with open(categorias + ".txt") as archivo:
# abrimos el archivo txt que se l en archivos
        for linea in archivo:
            linea = linea.strip()
            palabras.append(linea)
    return palabras

def obtenerPalabra():#Esta funcion
    print("")
    categorias = obtenerGrupos()#llamará a los grupos que estan dentro del txt
    indice = imprimirGruposYSolicitarIndice(categorias)#se pide que elija una opcion de las categorias
    categorias = categorias[indice]#se pide el numero de un grupo de las categorias
    palabras = obtenerPalabrasDeGrupo(categorias)#se llama esta funcion y se abrira las categorias
    return random.choice(palabras) #se usa esta libreria para obteber las palabras aleatoriamente

def juego_ahorcado(name):
    global letrasEscritas #Estas variables ya estan definidas pero para modificarlas dentro de la funcion usamos global
    global intentos 
    global contador
    intentos = 6 # Se inicia con 6 intentos 
    contador = 60
    letrasEscritas = [] # letras que ingresa el jugador
    palabra = obtenerPalabra() 
    prepararPalabra(palabra) # invocamos preparar palabra 
    while True: # siempre va pidiendo los datos
        imprimirAhorcado()
        dibujarIntentos()
        imprimirPalabra() 
        ingresar_letra=(input("ingresa la letra: ")) # Se pide al usuario ingresar una letra
        if ingresar_letra in 'abcdefghijklnmñopqrstuvwxyz++ ': 
            descubrirLetra(ingresar_letra) 
        else: 
            print("SOLO SE ADMITE LETRAS")
        if intentos <= 0: 
            print("Perdiste. La palabra era: "  )
            imprimirPalabraOriginal()
            return
        if haGanado():
            print(f'Ganaste {contador} puntos.')
            actualizar_leaderboard(name, contador)
            return

def obtenerGrupos():
    categorias = []
    with open("categorias.txt") as archivo:
        for linea in archivo:
            linea = linea.rstrip()
            categorias.append(linea)
    return categorias


def prepararArchivo():
    if not os.path.isfile("categorias.txt"):
        with open("categorias.txt", "w") as archivo: # Abriendo el archivo llamado categorias en formato .txt en modo escritura
            archivo.write("")



def merge(lista1, lista2):
    if lista1 == []:
        return lista2
    if lista2 == []:
        return lista1
    if lista1[0] > lista2[0]:
        return [lista1[0]] + merge(lista1[1:], lista2)
    else:
        return [lista2[0]] + merge(lista1, lista2[1:])

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        mitad = len(lista)//2
        return merge(merge_sort(lista[:mitad]), merge_sort(lista[mitad:]))

def actualizar_leaderboard(nombre, puntaje):
    if not os.path.isfile("leaderboard.txt"):
        with open("leaderboard.txt", "w") as archivo0: 
            archivo0.write(f"{nombre},{puntaje}\n")
    else:
        scoresListSorted = []
        encontrado = False
        with open("leaderboard.txt", "r") as archivo1:
            if archivo1.read() == "No hay jugadores":
                with open("leaderboard.txt", "w") as archivo2:
                    archivo2.write(f"{nombre},{puntaje}\n")
                    return # Return vacio para llevarnos al menu principal
            archivo1.seek(0) # Llevar el cursor al inicio del archivo
            for linea in archivo1:
                linea = linea.split(",")
                nuevoPuntaje = int(linea[1])
                if linea[0] == nombre:
                    nuevoPuntaje = nuevoPuntaje + puntaje
                    encontrado = True
                scoresListSorted.append((nuevoPuntaje, linea[0]))
        
        if not encontrado:
            scoresListSorted.append((puntaje, nombre))
        
        scoresListSorted = merge_sort(scoresListSorted)

        with open("leaderboard.txt", "w") as archivo:
            for score in scoresListSorted:
                archivo.write(f"{score[1]},{score[0]}\n")


def Leaderboard():
    if not os.path.isfile("leaderboard.txt"):
        with open("leaderboard.txt", "w") as archivo: 
            archivo.write("No hay jugadores")
            

    scoresListSorted = []
    with open("leaderboard.txt", "r") as archivo:
        if archivo.read() == "No hay jugadores":
            print("No hay jugadores")
            return
        else:
            archivo.seek(0)
            lineas = archivo.readlines()
            for linea in lineas:
                linea = linea.split(",")
                scoresListSorted.append((int(linea[1]), linea[0]))
    
    print("***LEADERBOARD***\n")
    print("\nJugadores\n\n")

    for index, [score, name] in enumerate(scoresListSorted):
        print(str(index + 1) + "° " + name + " - " + str(score) + " pts" + "\n")
        time.sleep(0.5)


import time
def limpiarPantalla():
    print("Cargando...")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')



# Definiendo el menú principal

def menu_principal():
    limpiarPantalla()
    menu = '''      
            🏳  ██╗   ██╗████████╗███████╗ █████╗        ██████╗  █████╗ ███╗   ███╗███████╗ ██████╗
            🏳  ██║   ██║╚══██╔══╝██╔════╝██╔══██╗      ██╔════╝ ██╔══██╗████╗ ████║██╔════╝██╔════╝
            🏳  ██║   ██║   ██║   █████╗  ██║  ╚═╝      ██║   ██╗███████║██╔████╔██║█████╗  ╚█████╗
            🏳  ██║   ██║   ██║   ██╔══╝  ██║  ██╗      ██║  ╚██╗██╔══██║██║╚██╔╝██║██╔══╝   ╚═══██╗
            🏳  ╚██████╔╝   ██║   ███████╗╚█████╔╝      ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗██████╔╝
            🏳   ╚═════╝    ╚═╝   ╚══════╝ ╚════╝        ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═════╝

    [1] Juego del ahorcado               
    [2] Mad Story
    [3] Otros juegos
    [4] Leaderboard
    [5] Salir
    Ingrese una opcion >>>  '''
    eleccion =input(menu) # Se pide al usuario ingresar un numero relacionado a una de las tres opciones

    if eleccion == "1": # Al ingresar la opcion 1 el usuario, este le redireccionará al juego del ahorcado
        print('|-- JUEGO DEL AHORCADO --|')
        juego_ahorcado(name)

    elif eleccion == "2": # Está opción ejecutará el menú de Otros_juegos
        Mad_Story()

    elif eleccion == "3":
        Otros_juegos()
    
    elif eleccion == "4":
        Leaderboard()
        
    elif eleccion == "5": # Esta opción finalizará el programa
        exit()
    else:
        menu_principal()

def main():
    global name
    name = input("Ingrese su nombre: ").lower()
    
    print("Bienvenido a la aplicación de juegos")
    prepararArchivo()
    while True:
        menu_principal() # Llamando a la funcion menú
main()