import random

def historia_1():
    lista = []
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

    a = f'Durante una guerra en la época de la {dic["app"]}, un pequeño poblado en el que vivía un \nmaestro guapo muy anciano.Un día, llegó a ellos la noticia de que un {dic["nombre mascota"]}\nse dirigía en su dirección para invadir y tomar la zona. El día anterior a la llegada del \nejército toda la aldea huyó, con la excepción del {dic["numero"]}.Cuando llegó y encontro la aldea \nprácticamente desierta y sabiendo de la existencia del maestro, ordenó que {dic["nombre mascota"]}\nse personase ante él, pero este no lo hizo. Furioso, el general sacó su {dic["juguete"]} y se la\nacercó a la cara, gritándole que si no se daba cuenta de que estaba simplemente parado \ndelante de quien podría atravesarle {dic["numero"]} en un instante.Con total tranquilidad, el anciano\nmaestro le contestó {dic["numero"]} en un instante. El general, sorprendido y confuso, terminó\nhaciéndole una {dic["comida"]} y marchándose de la {dic["app"]}'


    b = f'Un dia en mi cama un {dic["nombre mascota"]}, que le gusta ir a uno de los suburbios de la\n{dic["app"]}.El {dic["juguete"]} de la zona se afanó en agasajarla y darle la bienvenida en el templo, \npreparando para ella la mejor música y {dic["comida"]}. Sin embargo, el {dic["nombre mascota"]} estaba\naturdida y triste, no probando la carne o el vino. Tres días después murió en {dic["numero"]}.\nEl monje agasajó al {dic["nombre mascota"]} tal y como a él le hubiese gustado serlo, no como su\n{dic["hobby"]} kawai'
    
    c = f'Un hombre con su mascota {dic["nombre mascota"]} pasó el día explorando un {dic["app"]} en el que \nnunca había estado antes. Estaba anocheciendo y su sentido de orientación ya no \nfuncionaba bien, mientras seguía adentrándose más y más en la {dic["app"]}. Tras horas de \nandar vagando sin rumbo fijo y con la noche encima de él, encontró una cabaña con el \nnumero{dic["numero"]} entre varios árboles. Se dirigió a la cabaña para ver si alguien podía \nayudarlo, golpeó la puerta pero no hubo respuesta, estaba abierta así que decidió entrar.No \nhabía mucho adentro, solamente una {dic["juguete"]}, y sientiendose cansado pensó que lo \nmejor sería comer un {dic["comida"]} para despues dormir y si alguien venía le explicaría su \nhistoria. Mientras intentaba dormir, notó muchas pinturas extrañas en el interior de la cabaña \nde rostros  de su animal {dic["nombre mascota"]} deformados con ojos rojos y todos parecían \nestar mirándole.. Sintiéndose incomodo trató de recordar su {dic["hobby"]} favorito, cerró los \nojos y se durmió. En la mañana el aventurero despertó aterrorizado al darse cuenta que no había \npinturas en la cabaña, solo ventanas y un numero que decia 666.'

    d = f'Mi {dic["nombre mascota"]} me conoce mejor que yo. Hacía ya algún tiempo que contemplaba \nal {dic["comida"]} de enfrente, era una {dic["comida"]} muy linda y amante de los {dic["juguete"]}, \ntenía una precioso {dic["numero"]} morado que no la dejaba ni a sol ni a sombra. \nMi {dic["nombre mascota"]}, un mestizo pequeño con {dic["numero"]}, siempre escapaba \nde casa, no importaba lo cuidadoso que fuera. Por suerte, siempre \nregresaba para la hora del {dic["comida"]}. Yo no podía seguirlo a causa de mi trabajo, \nasí que siempre confiaba en encontrarlo frente a la puerta con su {dic["juguete"]}. \nUn día, no solo lo encontré a él, sino a mi vecina con su {dic["app"]} en el telefono, \nllevaba en sus manos una caja. Nuestros {dic["nombre mascota"]} nos habían convertido en \nabuelos y con un poco de suerte, en novios'
    
    lista.append(c)
    lista.append(a)
    lista.append(b)
    lista.append(d)

    h_aleatoria = random.choice(lista)

    with open('historia_h_aleatoria.txt','w', encoding='UTF-8') as textito:
        textito.write(h_aleatoria)

    print(h_aleatoria)

historia_1()