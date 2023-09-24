
from pygame import *


'''Необхідні класи'''
 
#клас-батько для спрайтів
class GameSprite(sprite.Sprite):
    #конструктор класу
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        #кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        #кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed



class Enemy(GameSprite):

    def update(self):
        if self.rect.x <= 170:
            self.direction = "right"
            
        if self.rect.x >= 600:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

 
#Ігрова сцена:
win_width = 700
win_height = 500
 
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))
 
#Персонажі гри:
player = Player('hero.png', 300, win_height - 80, 1)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)
 
game = True
clock = time.Clock()
FPS = 60
 
#музика
mixer.init() # Створює музичний плеєр
mixer.music.load('jungles.ogg') # завантажує музику
mixer.music.play() # зациклює і програє її
 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
 
    window.blit(background,(0, 0))
    player.reset()
    monster.reset()

    player.update()
    monster.update()

    display.update()
    clock.tick(FPS)