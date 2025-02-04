import pygame, random, sys
pygame.init()

pygame.mixer.init()
###def play_background_music():
  ###  pygame.mixer.music.load('resources/bg_music_1.mp3')
  ###  pygame.mixer.music.play(-1, 0)

###def play_sound(sound_name):
###    if sound_name == "crash":
###        sound = pygame.mixer.Sound("FOR-GO/crash.mp3")
####    elif sound_name == 'ding':
###       sound = pygame.mixer.Sound("FOR-GO/ding.mp3")
###   pygame.mixer.Sound.play(sound)

WIDTH = 1400
HEIGHT = 800
display = pygame.display.set_mode((WIDTH, HEIGHT))
game_close = False
game_over = False
cell = 40
clock = pygame.time.Clock()
is_eaten = False
score = 0

def draw_grids():
    for x in range(0, WIDTH, cell):
        for y in range(0, HEIGHT, cell):
            rect = pygame.Rect(x, y, cell, cell)
            pygame.draw.rect(display, '#404040', rect, 1)

def display_score():
    font = pygame.font.SysFont('Tlwg Typist', 30)
    score_font = font.render(f"score:{score}", True, 'white')
    font_pos = score_font.get_rect(center=((WIDTH/2)-30, 30))
    display.blit(score_font, font_pos)

class Snake:
    def __init__(self):
        self.x = 300
        self.y = 300
        self.body = [pygame.Rect(self.x, self.y, cell, cell)]
        self.direction = 'none'

    def draw_snake(self):
        for block in self.body:
            pygame.draw.rect(display, 'green', block, 0)

    def update_snake(self):
        self.body.append(pygame.Rect(self.x, self.y, cell, cell))
        self.head = self.body[-1]

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move(self):
        if self.direction == 'right':
            self.x += cell
        if self.direction == 'left':
            self.x -= cell
        if self.direction == 'up':
            self.y -= cell
        if self.direction == 'down':
            self.y += cell

        self.update_snake()

    def is_dead(self):
        global game_over
        if self.head.x <= 0 or self.head.x >= WIDTH:
            game_over = True
        elif self.head.y <= 0 or self.head.y >= HEIGHT:
            game_over = True
        for block in self.body[1:]:
            if block.colliderect(self.body[0]):
                game_over = True
               ### play_sound('crash')
class Fruit:
    def __init__(self):
        self.get_random_pos()

    def draw_fruit(self):
        self.body = pygame.Rect(self.x, self.y, cell, cell)
        pygame.draw.rect(display, 'red', self.body)

    def get_random_pos(self):
        self.x = (random.randint(0, WIDTH) // cell) * cell
        self.y = (random.randint(0, HEIGHT) // cell) * cell

snake = Snake()
fruit = Fruit()

###play_background_music()

while not game_close:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_close = True
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.direction != 'right':
                snake.move_left()
            if event.key == pygame.K_RIGHT and snake.direction != 'left':
                snake.move_right()
            if event.key == pygame.K_UP and snake.direction != 'down':
                snake.move_up()
            if event.key == pygame.K_DOWN and snake.direction != 'up':
                snake.move_down()

    display.fill((0, 0, 0))
    draw_grids()
    snake.draw_snake()
    snake.move()
    fruit.draw_fruit()
    display_score()

    if snake.head.colliderect(fruit.body):
        is_eaten = True
        score += 10
        ###play_sound('ding')

    if is_eaten:
        fruit.get_random_pos()
        is_eaten = False
    else:
        snake.body.pop(0)
    snake.is_dead()
    if game_over:
        font = pygame.font.SysFont('Tlwg Typist', 50)
        game_over_font = font.render("Game Over! Press Q to Quit or C to Play Again", True, 'white')
        font_pos = game_over_font.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        display.blit(game_over_font, font_pos)
        score_view = font.render(f"Score :{score}",True,'white')
        font_pos1 = score_view.get_rect(center=(WIDTH / 2, HEIGHT / 3))
        display.blit(score_view, font_pos1)
        pygame.display.update()
 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_q:
                game_over = True
                pygame.quit()
                sys.exit()
               if event.key == pygame.K_c:
                # Reset game variables here to restart the game
                snake = Snake()
                fruit = Fruit()
                score = 0
                game_over = False
                break


    pygame.display.update()
    clock.tick(9)  # Increase FPS for smoother gameplay
