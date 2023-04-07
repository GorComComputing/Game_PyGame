import pygame
pygame.init()   # импорт всех нужных библиотек


sc = pygame.display.set_mode((600, 400), pygame.DOUBLEBUF | pygame.HWSURFACE) # задаем размеры окна
pygame.display.set_caption("Игра на Python PyGame")
pygame.display.set_icon(pygame.image.load("icon48.png"))
clock = pygame.time.Clock() # для создания задержки

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

#pygame.draw.rect(sc, BLUE, (10, 10, 50, 100), 2)
#pygame.display.update() # вывести из буфера на экран pygame.display.flip()

x = 600//2
y = 400//2
speed = 5

#flLeft = flRight = False

# Главный цикл
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Нажата кнопка: ", event.button)
        elif event.type == pygame.MOUSEMOTION:
            print("Позиция мыши: ", event.pos)
#        elif event.type == pygame.KEYDOWN:  # нажатие клавиш
#            if event.key == pygame.K_LEFT:
#                flLeft = True
#            elif event.key == pygame.K_RIGHT:
#                flRight = True
#        elif event.type == pygame.KEYUP:    # отпускание клавиш
#            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
#                flLeft = flRight = False
                
                
#    if flLeft:
#        x -= speed
#    elif flRight:
#        x += speed

    # простая обработка нажатия клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed
        
    
    sc.fill(WHITE)
    pygame.draw.rect(sc, BLUE, (x, y, 10, 20))
    pygame.display.update() # вывести из буфера на экран
            
    clock.tick(60)  # задержка по времени до 60 FPS