from pygame import *
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("Coffin_As_Box.webp"), (win_width, win_height))
game = True
clock = time.Clock()
FPS = 60
#mixer.init()
#mixer.music.load("")
#mixer.music.play()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (80, 100))
        self.rect = self.image.get_rect()
        self.speed = player_speed
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
player = GameSprite("f7d49402cee51150c7068ac0169e34f1.jpg", 5, win_height - 80, 4)
monster = GameSprite("Без названия.jpg", win_height - 80, 280, 3)




while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0, 0))
    player.reset()
    display.update()
    clock.tick(FPS)