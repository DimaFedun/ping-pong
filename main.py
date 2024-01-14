from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_speed, player_x, player_y, size_x,size_y ):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y) )
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite): 

    def update_r(self):
        keys = key.get_pressed()
        if keys[k_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[k_DOWN] and self.rect.y < win_height-80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[k_s] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[k_w] and self.rect.y < win_height-80:
            self.rect.y += self.speed

racket1 = Player('0409.png_860.png',4,20,200,100,100)
racket2 = Player('0409.png_860.png',4,520,200,100,100)
ball = Player('png-transparent-football-ball-game-fussball-sport-sports-equipment-football-pitch.png',4,200,200,50,50)


back = (100,20,190)
win_height = 500
win_wight = 600
window = display.set_mode((win_wight, win_height))
window.fill(back)

clock = time.Clock()
FPS = 60
finish = False 
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        racket1.reset()
        racket2.reset()
        ball.reset()


    display.update()
    clock.tick(FPS)
