
def regresar(): #funcionque permite regresar al menu principal
    global regresar #fincion global que permite que la funcion se puede usar fuera de esta
    Regresar = menu_2()#Variable regresar para poder llamar a la funcion menu_principal
    return Regresar #retorna la variable


def historia_4():

    print("\t**** Mad Story_4 ***\n")
    print()
    print("Bienvenidos a Mad Story. Por favor conteste las siguientes preguntas\n")
    dic={ }
    hobby= input("¿Cual es su hobby?:  " )
    nombre_mascota= input("Nombre de su mascota:  ")
    numero= input("Ingrese un numero:"  )
    juguete=input("ingrese el nombre de su juguete:  ")
    comida=input("ingrese el nombre de su comida:  ")
    app=input("Aplicacion de celular:   ")
    print()
    print("listo!!")

    dic['hobby']=hobby
    dic['nombre mascota']=nombre_mascota
    dic['numero']= numero
    dic['juguete']=juguete
    dic['comida']=comida
    dic['app']=app
    print()
    print()
    print("\t****😎 Mad Story 😎***\n")

    d = f'Mi {dic["nombre mascota"]} me conoce mejor que yo. Hacía ya algún tiempo que contemplaba al {dic["comida"]} de enfrente, era una {dic["comida"]} muy linda y amante de los {dic["juguete"]}, tenía una precioso {dic["numero"]} morado que no la dejaba ni a sol ni a sombra. Mi {dic["nombre mascota"]}, un mestizo pequeño con {dic["numero"]}, siempre escapaba de casa, no importaba lo cuidadoso que fuera. Por suerte, siempre regresaba para la hora del {dic["comida"]}. Yo no podía seguirlo a causa de mi trabajo, así que siempre confiaba en encontrarlo frente a la puerta con su {dic["juguete"]}. Un día, no solo lo encontré a él, sino a mi vecina con su {dic["app"]} en el telefono, llevaba en sus manos una caja. Nuestros {dic["nombre mascota"]} nos habían convertido en abuelos y con un poco de suerte, en novios'

    print(d)
    with open('historia_4.txt','w', encoding='UTF-8') as textito:
        textito.write(d)

    return menu_2()


def historia_3():

    print("\t**** Mad Story_3 ***\n")
    print()
    print("Bienvenidos a Mad Story. Por favor conteste las siguientes preguntas\n")
    dic={ }
    hobby= input("¿Cual es su hobby?:  " )
    nombre_mascota= input("Nombre de su mascota:  ")
    numero= input("Ingrese un numero:"  )
    juguete=input("ingrese el nombre de su juguete:  ")
    comida=input("ingrese el nombre de su comida:  ")
    app=input("Aplicacion de celular:   ")
    print()
    print("listo!!")

    dic['hobby']=hobby
    dic['nombre mascota']=nombre_mascota
    dic['numero']= numero
    dic['juguete']=juguete
    dic['comida']=comida
    dic['app']=app
    print()
    print()
    print("\t****😎 Mad Story 😎***\n")

    c = f'Un hombre con su mascota {dic["nombre mascota"]} pasó el día explorando un {dic["app"]} en el que nunca había estado antes. Estaba anocheciendo y su sentido de orientación ya no funcionaba bien, mientras seguía adentrándose más y más en la {dic["app"]}. Tras horas de andar vagando sin rumbo fijo y con la noche encima de él, encontró una cabaña con el numero{dic["numero"]} entre varios árboles. Se dirigió a la cabaña para ver si alguien podía ayudarlo, golpeó la puerta pero no hubo respuesta, estaba abierta así que decidió entrar.No había mucho adentro, solamente una {dic["juguete"]}, y sientiendose cansado pensó que lo mejor sería comer un {dic["comida"]} para despues dormir y si alguien venía le explicaría su historia. Mientras intentaba dormir, notó muchas pinturas extrañas en el interior de la cabaña de rostros  de su animal {dic["nombre mascota"]} deformados con ojos rojos y todos parecían estar mirándole. Sintiéndose incomodo trató de recordar su {dic["hobby"]} favorito, cerró los ojos y'

    print(c)
    with open('historia_3.txt','w', encoding='UTF-8') as textito:
        textito.write(c)

    return menu_2()


def historia_2():

    print("\t**** Mad Story_2 ***\n")
    print()
    print("Bienvenidos a Mad Story. Por favor conteste las siguientes preguntas\n")
    dic={ }
    hobby= input("¿Cual es su hobby?:  " )
    nombre_mascota= input("Nombre de su mascota:  ")
    numero= input("Ingrese un numero:"  )
    juguete=input("ingrese el nombre de su juguete:  ")
    comida=input("ingrese el nombre de su comida:  ")
    app=input("Aplicacion de celular:   ")
    print()
    print("listo!!")

    dic['hobby']=hobby
    dic['nombre mascota']=nombre_mascota
    dic['numero']= numero
    dic['juguete']=juguete
    dic['comida']=comida
    dic['app']=app
    print()
    print()
    print("\t****😎 Mad Story 😎***\n")

    b = f'Un dia en mi cama un {dic["nombre mascota"]}, que le gusta ir a uno de los suburbios de la {dic["app"]}.El {dic["juguete"]} de la zona se afanó en agasajarla y darle la bienvenida en el templo, preparando para ella la mejor música y {dic["comida"]}. Sin embargo, el {dic["nombre mascota"]} estaba aturdida y triste, no probando la carne o el vino. Tres días después murió en {dic["numero"]}. El monje agasajó al {dic["nombre mascota"]} tal y como a él le hubiese gustado serlo, no como SU {dic["hobby"]} kawai'
    print(b)

    with open('historia_2.txt','w', encoding='UTF-8') as textito:
        textito.write(b)

    return menu_2()



def historia_1():

    print("\t**** Mad Story ***\n")
    print()
    print("Bienvenidos a Mad Story. Por favor conteste las siguientes preguntas\n")
    dic={ }
    hobby= input("¿Cual es su hobby?:  " )
    nombre_mascota= input("Nombre de su mascota:  ")
    numero= input("Ingrese un numero:"  )
    juguete=input("ingrese el nombre de su juguete:  ")
    comida=input("ingrese el nombre de su comida:  ")
    app=input("Aplicacion de celular:   ")
    print()
    print("listo!!")

    dic['hobby']=hobby
    dic['nombre mascota']=nombre_mascota
    dic['numero']= numero
    dic['juguete']=juguete
    dic['comida']=comida
    dic['app']=app
    print()
    print()
    print("\t****😎 Mad Story 😎***\n")

    a = f'Durante una guerra en la época de la {dic["app"]}, \nun pequeño poblado en el que vivía un maestro guapo muy anciano.\nUn día, llegó a ellos la noticia de que un  {dic["nombre mascota"]} se dirigía \nen su dirección para invadir y tomar la zona.\nEl día anterior a la llegada del ejército toda dic {dic["nombre mascota"]} \nprácticamente desierta y sabiendo de la existencia del mae la aldea huyó, con la excepción del {dic["numero"]}. \nCuando llegó y encontro la aldstro, ordenó que  se personase ante él, pero este no lo hizo.\nTU JOBI ES {dic["hobby"]}Durante una guerra en la época de la {dic["app"]}, \nun pequeño poblado en el que vivía un maestro guapo muy anciano'
    print(a)

    with open('historia_1.txt','w', encoding='UTF-8') as textito:
        textito.write(a)

    return menu_2()

def main():
    import menu

def menu_2(): #funcion para los otros juegos
    menu2=''' 
    1. Historia_1
    2. Historia_2
    3. Historia_3
    4. Historia_4
    5. Atras 
    Ingrese una opción >>> '''
    elegir_alternativa=int(input(menu2)) 
    if elegir_alternativa==1:
        historia_1()

    if elegir_alternativa==2:
        historia_2()

    if elegir_alternativa==3:
        historia_3()

    if elegir_alternativa==4:
        historia_4()

    elif elegir_alternativa == 5:
        main()
    else:
        while elegir_alternativa != (1 or 2 or 3 or 4 or 5):
            print("Ingrese una opción válida ")
            elegir_alternativa=int(input(menu2))
        
menu_2()