import pygame, sys, time, random

pygame.init()

ventana = pygame.display.set_mode((500, 500)) #Tamaño de la ventana

font = pygame.font.Font(None, 30) #Tamaño de fuente  del score

fps = pygame.time.Clock()

def food():
    random_pos = random.randint(0,49)*10 #posciciones en donde saldra la comida de manera aleatoria
    food_pos = [random_pos, random_pos]
    return food_pos


def main():

    posicion_serpiente = [100, 50]  #aqui especificamos en que punto sa
    cuerpo = [[100,50],[90,50],[80,50]] #Se especifica el tamaño del cuerpo de la serpiente
    change = "RIGHT"
    run = True
    food_pos = food()
    score = 0

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN: #se especifica el las teclas de movimiento
                if event.key == pygame.K_RIGHT:#Tecla para moverse a la derecha
                    change = "RIGHT"
                if event.key == pygame.K_LEFT:#tecla para moverse a la izquierda
                    change = "LEFT"
                if event.key == pygame.K_UP:#tecla para moverse arriba
                    change = "UP"
                if event.key == pygame.K_DOWN: #tecla para moverse abajo
                    change = "DOWN"
        if change == "RIGHT": #movimientos de la serpiente derecha, arriba, abajo e izquierda
            posicion_serpiente[0] += 10 
        if change == "LEFT":
            posicion_serpiente[0] -= 10
        if change == "UP":
            posicion_serpiente[1] -= 10
        if change == "DOWN":
            posicion_serpiente[1] += 10

        cuerpo.insert(0, list(posicion_serpiente))

        if posicion_serpiente == food_pos: #Cuandola serpiente come la comida el score sube 
            food_pos = food()
            score += 1
            print(score)
        else:
           cuerpo.pop() #Cuerpo de la serpiente aumenta

        ventana.fill((0,0,0))

        for pos in cuerpo:
            pygame.draw.rect(ventana,(200,200,200), pygame.Rect(pos[0], pos[1], 10, 10))
        
        pygame.draw.rect(ventana,(169,6,6), pygame.Rect(food_pos[0], food_pos[1], 10, 10))
        
        text = font.render(str(score),0,(200,60,80)) #color del score 
        ventana.blit(text, (480,20))

        if score < 10:
            fps.tick(10) #velocidad de la serpiente
        if score >= 10:
            fps.tick(20) #aumenta la velocidad de la serpiente

        if posicion_serpiente[0] <= 0 or posicion_serpiente[0] >= 500:
            run = False
            print("YOU LOSE")
        if posicion_serpiente[1] <= 0 or posicion_serpiente[1] >= 500:
            run = False
            print("YOU LOSE")

        pygame.display.flip()

main()

pygame.quit()