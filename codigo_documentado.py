import time
import os
import random

def Mad_Story():
    '''
    Aca estamo importando las historias
    '''
    import historias

def Otros_juegos():
    '''
    Estamos creando una función que se llama otros juegos con parametro vacio, adentro creamos un menu2 que tiene dos opciones juegos_snake y atras, nos va a pedir ingresar una Opción.
    Bueno el usuario va a tener que ingresar la opción correcta caso contrario que no lo ingrese le aparecera un mensaje  diciendo que fue un numero invalido y volvera al menu.
    '''
    menu2 = ''' 
1. Juego_snake
2. Atras
Ingrese una opción:  '''
    elegir_alternativa = int(input(menu2))
    if elegir_alternativa == 1:
        juego_snake()  
    elif elegir_alternativa == 2:
        regresar()
    else:
        print("Ingrese un numero valido")
        elegir_alternativa = int(input(menu2))


def juego_snake():
    "Creamos una función juego_snake con parametro vacio, este importa el juego del snake para luego retornarlo y mas adelante lo llamamos."
    import juego_snake
    return juego_snake


def prepararPalabra(original):
    '''Creamos una función que se llama prepararPalabra con un solo parametro que se llama original. Bueno utilizamos el global para actualizar la variable o sea(palabra adivinada) con el -punto lower- lo que se hace es convertir la palabra a minuscula. Luego creamos una lista vacia que se llama palabraAdivinada para despues iterar en original, tambien utilizaremos el diccionario para añadir a la lista de palabras adivinadas con .append y dentro del diccionario ira la letra adivinada mas si fue falso o verdadero.'''
    global palabraAdivinada 
    original = original.lower() 
    palabraAdivinada = [] 
    for letra in original:
        palabraAdivinada.append({
            "letra": letra,
            "adivinada": False, 
        })


def letraEstaEnPalabra(letra):
    '''Creamos una función que se llama letraEstaEnPalabra con un parametro-letra-, luego usamos la función global para llamar a la palabra adivinada que se encuentra fuera de la función, despues vamos a iterar o sea para cada letracompuesta en palabra adivinada si tenemos que letra compuesta es igual a letra retorna verdadero caso contrario es falso o sea no lo retorna.'''
    global palabraAdivinada
    for letraCompuesta in palabraAdivinada:
        if letraCompuesta["letra"] == letra:
            return True
    return False





def descubrirLetra(letraDeUsuario):
    '''Estamos creando una función que se llama dscubrirletra con un solo parametro que se llama letradeusuario, estamos llamando con la función global al contador, palabraadivinada, letrasEscritas E intentos. Si el usuario ingresa una letra con mayuscula lo que va hacer el punto lower es convertirle a minuscula.Ya bueno ahora si mi letra de usuario esta en letras escritas me retorna el valor caso contrario sino encontramos letras escritas se agregara a la lista de letras escritas.Con el - if not letraEstaEnPalabra - lo que hacemos aqui es que si mi letra en palabras no esta en palabra pierdes un intento sino iteramos cada letra en palabra adivinada, ahora si mi letra compuesta es igual a letra de usuario entonces la letra compuesta es la letra adivinada entonces es verdadero.'''
    global contador, palabraAdivinada, letrasEscritas, intentos

    letraDeUsuario = letraDeUsuario.lower()
    if letraDeUsuario in letrasEscritas:
        return  
    else:
        letrasEscritas.append(letraDeUsuario)
    if not letraEstaEnPalabra(letraDeUsuario):  
        intentos -= 1
        contador -= 10
    else:
        for letraCompuesta in palabraAdivinada:
            if letraCompuesta[
                "letra"] == letraDeUsuario:  
                letraCompuesta["adivinada"] = True 


def imprimirPalabra(): 
    '''Creamos una función que se llama imprimir palabra con parametro vacio 
    luego itereamos para cada letra compuesta en palabra adivinada entonces si mi letra 
    es compuesta se va a imprimir la letra compuesta en una sola linea caso contrario que no
     sea compuesta se imprimira un guión en la misma linea. con el print ultimo lo que hacemos es imprimir una linea vacia, como un salto de linea.'''

    for letraCompuesta in palabraAdivinada:
        if letraCompuesta["adivinada"]:
            print(letraCompuesta["letra"], end="")
        else:
            print("-", end="")
    print("")



def imprimirPalabraOriginal():
      """
      Creamos una funcion para ver si la letra ingresada esta en la palabra a adivinar y si lo esta imprimimos la letra
      """
    for letraCompuesta in palabraAdivinada:
        print(letraCompuesta["letra"], end="")  


def haGanado():
    """
    Creamos una función que se llama haGanado , luego implementamos una función global palabaraAdivinada para llamarla, ya que se encuentra fuera de la función, y utilizarla aqui, luego lo que haremos sera iterar cada letra en palabra adivinada si mi letra no es la adivinada me retorna falso caso contrario true.
    """
    global palabraAdivinada
    for letra in palabraAdivinada:
        if not letra["adivinada"]:
            return False
    return True
    


def imprimirAhorcado():
    '''Creamos una función que se llama imprimir ahorcado con parametro vacio.
        cada vez que el usuario ingrese una letra que no pertenesca a la palabra indicada que se encontrara en el archivo txt, se le aumentara partes de su cuerpo que indicara que llegara su muerte(o sea se ahorcara) es por eso que en cada condicional aparecen numeros del 1 al 6 indicando la cantidad de intentos que te quedan. '''
   
    if intentos == 1:
        
        print("""
                       _
                      |   |
                     _O/  |
                      |   |
                     / \  |
                    __|
        """)
    elif intentos == 2:
       
        print("""
                       _
                      |   |
                     _O/  |
                      |   |
                       \  |
                    __|
        """)
    elif intentos == 3:
        

        print("""
                       _
                      |   |
                     _O/  |
                      |   |
                          |
                    __|
        """)
    elif intentos == 4:
        
        print("""
                       _
                      |   |
                     _O/  |
                          |
                          |
                    __|
        """)
    elif intentos == 5:
        print("""
                       _
                      |   |
                      O/  |
                          |
                          |
                    __|
        """)
    elif intentos == 6:
        
        print("""
                       _
                      |   |
                      O   |
                          |
                          |
                    __|
        """)

def dibujarIntentos():
    """funcion para imprimir los intentos restantes
    """
    print("Intentos restantes: " + str(intentos))


def regresar():
    """funcion con parametro vacio que cada vez que pongas la opcion regresar te retornara al menu principal
    """  
    global regresar
    Regresar = menu_principal()  
    return Regresar  

def imprimirGruposYSolicitarIndice(grupos):
    '''Creamos una función que se llama imprimirGruposYSolicitarIndice con un parametro que se llama grupos. ahora para cada categorias vamos a enumerar con la función enumerate, como ven en el print, si i empezara desde cero, aumentara mas 1 y asi sucesivamente en categorias. Colocamos print("5. Atrás") como parte faltante del menu ya que no se podia colocar en txt. luego colocamos la varible ingresar como funcion de un imput para que el usuario ingrese la categoria que quiera jugar luego con el con el if ingresar... si es igual a 5 ira a la función regresar y se imprimira pero si el usuario ingresa un numero mayor o negativo que ingresar de nuevo la primera opción que  vendria hacer 1.'''
    
    for i, categorias in enumerate(grupos):
        print(f"{i + 1}. {categorias}")
    print("5. Atrás")
    ingresar = int(input("Selecciona una categoria para jugar >> ")) - 1 
    if ingresar + 1 == 5:
        print('Regresar')
        regresar()
    while ingresar <= -1 or ingresar + 1 > 5: 
        print('Ingrese una opcion válida')
        ingresar = int(input("Selecciona una categoria para jugar >> ")) - 1

    return ingresar


def obtenerPalabrasDeGrupo(categorias):
    '''Creamos una función que se llama obtenerPalabraDeGrupo con un parametro que se denomina categorias, creamo una lista vacia que se llama palabras, despues abrimos el archivo txt con open, utilizamos with para ya no implementar el close al final aya y tambien utilizamos un alias que se llama archivo en la linea 218 luego iteramos para cada linea en archivo implemetando la función strip que lo que hace es cortar los espacios para luego añadir cada linea a la lista vacias en palabras y por ultimo retornar.'''

    palabras = []
    with open(categorias + ".txt") as archivo:
        for linea in archivo:
            linea = linea.strip()
            palabras.append(linea)
    return palabras


def obtenerPalabra():
    """Creamos una funcion con parametro vacio, llamamos a la funcion obtener grupos para usarlo como categorias, luego pedimos el indice para seleccionar una de las categorias para despues con las palabras de la categoria seleccionada hacer un random. choice para obtener una palabra aleatoriamente"
    """ 
    print("")
    categorias = obtenerGrupos()  
    indice = imprimirGruposYSolicitarIndice(categorias)
    categorias = categorias[indice]
    palabras = obtenerPalabrasDeGrupo(categorias) 
    return random.choice(palabras)


def juego_ahorcado(name):
    '''Creamos una función que se llama juego del ahorcado con un solo parametro que se llama name, utilizamos la función global para llamar utilizarlas dentro de la función(recuerdad que estas variables que estas juntas al global ya estan definidas), El jugador va iniciar con 6 intentos, creamos una lista vacia que se llama letrasEscritas definimos una variable que se llama palabra y que guarda la función obtnerPalabra(), invocamos  prepararPalabra(palabra) con el while true siempre va pidiendo los datos despues con ingresar_letra se le pedira al usuario ingresar una letra. SI la letra ingresada esta en ese abecedario que se encuentra en la linea 250 nos lleva a la función descubrir letra, caso contrario me imprime solo se admiten letras eso quiere decir que el usuaio ingreso un parametro incorrecto. Si mis intentos con menores o iguales a cero me imprime game over tambien me imprime la palabra correcta y el puntaje que obtuve que vendria hacer 0. todo ese puntaje y nombre se guardara en un arhivho txt.'''
    global letrasEscritas 
    global intentos
    global contador
    intentos = 6
    contador = 60
    letrasEscritas = [] 
    palabra = obtenerPalabra()
    prepararPalabra(palabra) 
    while True: 
        imprimirAhorcado()
        dibujarIntentos()
        imprimirPalabra()
        ingresar_letra = (input("ingresa la letra: "))
        if ingresar_letra in 'abcdefghijklnmñopqrstuvwxyz++ ':
            descubrirLetra(ingresar_letra)
        else:
            print("SOLO SE ADMITE LETRAS")
        if intentos <= 0:
                        print("""(●_•̃)_GAMER OVER""")
          
            
        print("La palabra era: ")
        imprimirPalabraOriginal()
        print()
        print("Tu puntaje es 0")
        actualizar_leaderboard(name, contador)
        return
        if haGanado():
            print("""◄╬►GANASTE◄╬►""")   
            print(f' {contador} puntos')
        actualizar_leaderboard(name, contador)
        return


def obtenerGrupos():
    '''Creamos una función que se llama obtener grupos con parametro vacio, despues creamos un lista vacia que se llama categorias abrimos un archivo txt con with open con el alias archivo e iteramos para linea en archivo, para cada linea con la función rstrip lo que hacemos es eliminar los espacios de adelante  y atras para despues agregar cada linea en categprias y retornarla.'''

    categorias = []
    with open("categorias.txt") as archivo:
        for linea in archivo:
            linea = linea.rstrip()
            categorias.append(linea)
    return categorias

def prepararArchivo():
    """creamos la funcion preparar archivo con parametro vacío, si el archivo txt no existe como una ruta regular , abrimos el achivo llamada categorias en formato txt, en modo escritura con el alias archivo .
    """
    if not os.path.isfile("categorias.txt"):
        with open("categorias.txt",
                  "w") as archivo: 
            archivo.write("")


'-----------------------------------------------------------------------------------'


def merge(lista1, lista2):
    '''Creamos una función merge con dos parámetros lista1 y lista2. si mi lista 1 es una lista vacia retornamos lista 2 y viceversa, si el primer indice en la lista1 es mayor al primer indice de la lista 2 retornamos la lista1 y lista2 caso contrario el otro.'''
    if lista1 == []:
        return lista2
    if lista2 == []:
        return lista1
    if lista1[0] > lista2[0]:
        return [lista1[0]] + merge(lista1[1:], lista2)
    else:
        return [lista2[0]] + merge(lista1, lista2[1:])


def merge_sort(lista):
    '''Creamos una función que se llama merge_sort con un parametro lista. si la longitus de mi lista es menor o igual a 1 retorna la lista caso contrario  a mi lista lo divimos a la mitad y retornamos la primer parte de la lista y despues la otra parte con la funcion merge.'''
    if len(lista) <= 1:
        return lista
    else:
        mitad = len(lista) // 2
        return merge(merge_sort(lista[:mitad]), merge_sort(lista[mitad:]))


def actualizar_leaderboard(nombre, puntaje):
    '''
    Creamos una función actualizar_leaderboard con dos parametros nombre y puntaje, si el archivo txt leaderboard no existe como una ruta regular exitente abrimos el archivo modo escritura con el alias archivos0 con su respectivo nombre y puntaje mas el salto de linea.
    caso contraio creamos una lista vacia scoresListSorted sino se encontro abrimos un archivo con el alias archivo1 si al momento de leer el archivo no hay jugadores abrimos el archivo2 escribiendo el nombre y el puntaje respectivo luego retorna al menu principal para despues llevar el cursos al inicio del archivo.
    Luego iteramos para linea en archivo1 a cada linea lo vamos a separar por comas y saldra mi nuevo puntaje, ahora  si mi línea en el primer indice es igual a nombre mi puntaje se va a ir actualizando y guardando en la lista scoresListSorted.
    '''
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
                    return  
            archivo1.seek(0)  
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
    """
    Creamos una función que se llama Leaderboard, luego si mi archivo Leaderboard txt no existe abrimos un archivo para que se escriba en el txt con el alias archivo y esté no hay jugadores.
    Creamos una lista vacia llamada scoresListSorted, abrimos ese archivo modo lectura con el alias archivo, ahora si mi archivo esta no hay jugadores se imprime no hay jugadores caso contario cambiamos la posición del identificados a 0, despues iteramos cada linea separandolos por coma con la función split para despues añadir todo con la función append en la lista vacia.
    Luego aparece el puntaje por un tiempo dado de 0.5 segundos en orden.
    """
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


'-----------------------------------------------------------------------------------'



def limpiarPantalla():
  """Creamos una funcion con parametro vacio que limpia la pantalla de la consola con un tiempo de 1 seg
  """
    print("Cargando...")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

# Definiendo el menú principal

def menu_principal():
    """
    creamos la funcion menu principal en la cual se imprime el menu Utec Games, si la eleccion del usuario es 1 iras al juego del ahorcado, si eliges la opcion 2 iras al mad story, si eliges la opcions 2 iras a otros juegos, si eliges la opcion 3 iras a otros juegos, si eliges la opcion 4 iras al leaderboard y la opcion 5 es la de salir, como extra usamos un while para que solo acepte valores ingresados del numero 1 al 5
    """
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
    eleccion = int(input(menu))

    while eleccion <= 0 or eleccion >= 6:
        print('<< Opción de entrada invalida >>')
        eleccion = int(input(menu))

    if eleccion == 1: 
        print('*JUEGO DEL AHORCADO*')
        juego_ahorcado(name)

    elif eleccion == 2: 
        Mad_Story()

    elif eleccion == 3:
        Otros_juegos()

    elif eleccion == 4:
        Leaderboard()

    elif eleccion == 5:
        exit()

def main():
    '''Creamos una función que se llama main, utilizamos la función global para llamar a la variable que se encuentra fuera de la función ademas el usuario va a ingresar su nombre, luego se imprimira Bienvenido a la aplicación de juegos se llama a la función prepaparArchivo si es verdadero tambien se llamara a la función menu_principal.'''
    
    global name
    name = input("Ingrese su nombre: ")

    print("Bienvenido a la aplicación de juegos")
    prepararArchivo()
    while True:
        menu_principal()

main()