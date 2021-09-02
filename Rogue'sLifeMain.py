# import the pygame module, so you can use it
import pygame
import os
import random

# initialize the pygame module
pygame.init()
pygame.display.init()

# constants
WIDTH, HEIGHT = 960, 640
TOP_OF_SCREEN = 96
BORDER_SIZE = 64

screen = pygame.display.set_mode((WIDTH, HEIGHT))
# load and set the logo
logo = pygame.image.load('Logo.png')
pygame.display.set_icon(logo)
pygame.display.set_caption("Rogue's Life")
FPS = 10

# User events
GAME_QUIT = pygame.USEREVENT + 1
USER_HIT = GAME_QUIT + 1

# character constants
CHAR_SIZE = 64

# background/ start menu images
loadingScreen = pygame.transform.scale(pygame.image.load('LoadingScreenMadeByMe.png'), (WIDTH, HEIGHT))
loadingScreen = loadingScreen.convert()
rect = loadingScreen.convert_alpha()
start_image = [pygame.transform.scale(pygame.image.load('StartMenu1.png'), (WIDTH, HEIGHT)),
               pygame.transform.scale(pygame.image.load('StartMenu2.png'), (WIDTH, HEIGHT))]

# death screen
death_image = [pygame.transform.scale(pygame.image.load('DeathMenu1.png'), (WIDTH, HEIGHT)),
               pygame.transform.scale(pygame.image.load('DeathMenu2.png'), (WIDTH, HEIGHT))]

# UI images
UI_IMAGE = pygame.image.load(os.path.join('UI Images', 'UI.png'))
number_images = [pygame.image.load(os.path.join('UI Images', 'numb_0.png')),
                 pygame.image.load(os.path.join('UI Images', 'numb_1.png')),
                 pygame.image.load(os.path.join('UI Images', 'numb_2.png')),
                 pygame.image.load(os.path.join('UI Images', 'numb_3.png')),
                 pygame.image.load(os.path.join('UI Images', 'numb_4.png')),
                 pygame.image.load(os.path.join('UI Images', 'numb_5.png')),
                 pygame.image.load(os.path.join('UI Images', 'numb_6.png')),
                 pygame.image.load(os.path.join('UI Images', 'numb_7.png')),
                 pygame.image.load(os.path.join('UI Images', 'numb_8.png')),
                 pygame.image.load(os.path.join('UI Images', 'numb_9.png'))]
mini_numbers_images = [pygame.transform.scale(number_images[0], (6, 13)),
                       pygame.transform.scale(number_images[1], (6, 13)),
                       pygame.transform.scale(number_images[2], (6, 13)),
                       pygame.transform.scale(number_images[3], (6, 13)),
                       pygame.transform.scale(number_images[4], (6, 13)),
                       pygame.transform.scale(number_images[5], (6, 13)),
                       pygame.transform.scale(number_images[6], (6, 13)),
                       pygame.transform.scale(number_images[7], (6, 13)),
                       pygame.transform.scale(number_images[8], (6, 13)),
                       pygame.transform.scale(number_images[9], (6, 13))]
health_images = [pygame.image.load(os.path.join('UI Images', '0-4_heart.png')),
                 pygame.image.load(os.path.join('UI Images', '1-4_heart.png')),
                 pygame.image.load(os.path.join('UI Images', '2-4_heart.png')),
                 pygame.image.load(os.path.join('UI Images', '3-4_heart.png')),
                 pygame.image.load(os.path.join('UI Images', '4-4_heart.png'))]
potion_images = [pygame.image.load(os.path.join('UI Images', '0-3_potion.png')),
                 pygame.image.load(os.path.join('UI Images', '1-3_potion.png')),
                 pygame.image.load(os.path.join('UI Images', '2-3_potion.png')),
                 pygame.image.load(os.path.join('UI Images', '3-3_potion.png'))]

# stage images

stage_1 = pygame.image.load('Stage1.png')

# character images/ animations
# main character ####################################################################
# WALK ####################################
main_char_walk_up = [pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Walk(Up)-1.png')),
                     pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Walk(Up)-2.png')),
                     pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Walk(Up)-3.png')),
                     pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Walk(Up)-4.png')),
                     pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Walk(Up)-5.png')),
                     pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Walk(Up)-6.png')),
                     pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Walk(Up)-7.png')),
                     pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Walk(Up)-8.png'))]
main_char_walk_down = [pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Walk(Down)-1.png')),
                       pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Walk(Down)-2.png')),
                       pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Walk(Down)-3.png')),
                       pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Walk(Down)-4.png')),
                       pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Walk(Down)-5.png')),
                       pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Walk(Down)-6.png')),
                       pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Walk(Down)-7.png')),
                       pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Walk(Down)-8.png'))]
main_char_walk_right = [pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Walk(Right)-1.png')),
                        pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Walk(Right)-2.png')),
                        pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Walk(Right)-3.png')),
                        pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Walk(Right)-4.png')),
                        pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Walk(Right)-5.png')),
                        pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Walk(Right)-6.png')),
                        pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Walk(Right)-7.png')),
                        pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Walk(Right)-8.png'))]
main_char_walk_left = [pygame.transform.flip(main_char_walk_right[0], True, False),
                       pygame.transform.flip(main_char_walk_right[1], True, False),
                       pygame.transform.flip(main_char_walk_right[2], True, False),
                       pygame.transform.flip(main_char_walk_right[3], True, False),
                       pygame.transform.flip(main_char_walk_right[4], True, False),
                       pygame.transform.flip(main_char_walk_right[5], True, False),
                       pygame.transform.flip(main_char_walk_right[6], True, False),
                       pygame.transform.flip(main_char_walk_right[7], True, False)]
# attack ##################################
# up
# down
main_char_attack_right = [pygame.image.load(os.path.join('Character Sprites', 'Default',
                                                         'MainChar-Attack(Right)-1.png')),
                          pygame.image.load(os.path.join('Character Sprites', 'Default',
                                                         'MainChar-Attack(Right)-2.png')),
                          pygame.image.load(os.path.join('Character Sprites', 'Default',
                                                         'MainChar-Attack(Right)-3.png')),
                          pygame.image.load(os.path.join('Character Sprites', 'Default',
                                                         'MainChar-Attack(Right)-4.png'))]
main_char_attack_left = [pygame.transform.flip(main_char_attack_right[0], True, False),
                         pygame.transform.flip(main_char_attack_right[1], True, False),
                         pygame.transform.flip(main_char_attack_right[2], True, False),
                         pygame.transform.flip(main_char_attack_right[3], True, False)]
# idle #####################################
main_char_idle_up = [pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Idle(Up)-1.png')),
                     pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Idle(Up)-2.png')),
                     pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Idle(Up)-3.png')),
                     pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Idle(Up)-4.png')),
                     pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Idle(Up)-5.png')),
                     pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Idle(Up)-6.png')),
                     pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Idle(Up)-7.png')),
                     pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Idle(Up)-8.png'))]
main_char_idle_down = [pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Idle(Down)-1.png')),
                       pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Idle(Down)-2.png')),
                       pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Idle(Down)-3.png')),
                       pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Idle(Down)-4.png')),
                       pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Idle(Down)-5.png')),
                       pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Idle(Down)-6.png')),
                       pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Idle(Down)-7.png')),
                       pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Idle(Down)-8.png'))]
main_char_idle_right = [pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Idle(Right)-1.png')),
                        pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Idle(Right)-2.png')),
                        pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Idle(Right)-3.png')),
                        pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Idle(Right)-4.png')),
                        pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Idle(Right)-5.png')),
                        pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Idle(Right)-6.png')),
                        pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Idle(Right)-7.png')),
                        pygame.image.load(os.path.join('Character Sprites', 'Default', 'MainChar-Idle(Right)-8.png'))]
main_char_idle_left = [pygame.transform.flip(main_char_idle_right[0], True, False),
                       pygame.transform.flip(main_char_idle_right[1], True, False),
                       pygame.transform.flip(main_char_idle_right[2], True, False),
                       pygame.transform.flip(main_char_idle_right[3], True, False),
                       pygame.transform.flip(main_char_idle_right[4], True, False),
                       pygame.transform.flip(main_char_idle_right[5], True, False),
                       pygame.transform.flip(main_char_idle_right[6], True, False),
                       pygame.transform.flip(main_char_idle_right[7], True, False)]

# slime ######################################################################################################
slime_idle = pygame.image.load(os.path.join('Mob Sprites', 'Slimes', 'Slime-Idle.png'))

mob_grave = pygame.image.load(os.path.join('Mob Sprites', 'grave.png'))

# sound effects

# music


# user class
class User:
    # default class
    def __init__(self):
        self.rectangle = pygame.Rect(BORDER_SIZE, TOP_OF_SCREEN + 4 * BORDER_SIZE, CHAR_SIZE, CHAR_SIZE)
        self.direction = "right"
        self.char_class = "main"
        self.curr_health = 12
        self.max_health = 12
        self.atk = 1
        self.gold = 2
        self.exp = 8
        self.lvl = 88
        self.curr_potions = 4
        self.max_potions = 4
        self.potion_heal = 4
        self.walk_anim = -2
        self.atk_anim = -2
        self.idle_anim = -2
        self.atk_break = 0
        self.collision_break = 0

        # class special stats
        self.regen = 0
        self.bees = 0

    # class changes
    def necromancer(self):
        self.char_class = "necromancer"
        self.atk += 1
        self.max_health += 4
        self.curr_health += 4

    def assassin(self):
        self.char_class = "assassin"
        self.atk += self.atk
        self.max_health += 4
        self.curr_health += 4

    def tank(self):
        self.char_class = "tank"
        self.max_health += 8
        self.curr_health += 8
        self.curr_potions = 4
        self.max_potions = 4

    def chef(self):
        self.char_class = "chef"
        self.atk += 1
        self.max_health += 4
        self.curr_health += 4

    def beekeeper(self):
        self.char_class = "beekeeper"
        self.atk += 1
        self.max_health += 4
        self.curr_health += 4


# mob class
class Mob:
    # default mob
    def __init__(self):
        self.alive = True
        self.walking = False
        self.attacking = False
        self.direction = "left"
        self.hp = 2
        self.atk = 2
        self.rectangle = pygame.Rect(0, 0, CHAR_SIZE, CHAR_SIZE)
        self.type = "slime"
        self.exp = 1
        self.gold = 0
        self.idle_anim = -1
        self.walk_anim = -1
        self.atk_anim = -1
        self.atk_break = 0

    # baby slime mob
    def baby_slime(self):
        self.hp = 1
        self.atk = 1
        self.type = "baby slime"
        self.exp = 1
        self.gold = 1

    # goblin mob
    def goblin(self):
        self.hp = 3
        self.atk = 3
        self.type = "goblin"
        self.exp = 3
        self.gold = 2


# spawn mobs
def spawn_mobs(char, stage):
    mob_list = []
    if stage == 1.1:
        # add five mobs in open areas
        for i in range(5):
            new_mob = Mob()
            temp_rect = pygame.Rect(random.randint(1, 13) * CHAR_SIZE, random .randint(3, 8) * CHAR_SIZE,
                                    CHAR_SIZE, CHAR_SIZE)

            collision = 88
            mob_rect_list = []
            for mob in mob_list:
                mob_rect_list.append(mob.rectangle)

            while collision != -1:
                if temp_rect.colliderect(char):
                    temp_rect = pygame.Rect(random.randint(1, 13) * CHAR_SIZE, random.randint(3, 8) * CHAR_SIZE,
                                            CHAR_SIZE, CHAR_SIZE)

                collision = temp_rect.collidelist(mob_rect_list)
                if collision != -1:
                    temp_rect = pygame.Rect(random.randint(1, 13) * CHAR_SIZE, random.randint(3, 8) * CHAR_SIZE,
                                            CHAR_SIZE, CHAR_SIZE)

            new_mob.rectangle = temp_rect
            mob_list.append(new_mob)

        # change mob types
        mob_list[0].goblin()
        mob_list[1].goblin()

    return mob_list


# game starting up with menu animation
def game_start():
    running = True
    clock = pygame.time.Clock()

    # fade in loading screen
    background = pygame.Surface((screen.get_rect().width, screen.get_rect().height))

    for i in range(50):
        background.fill((0, 0, 0))
        loadingScreen.set_alpha(i)
        screen.blit(loadingScreen, (0, 0))
        pygame.display.update()
        pygame.time.delay(40)

    # show start screen
    curr = 0

    while running:
        clock.tick(FPS)

        # menu
        screen.blit(start_image[curr], (0, 0))

        pygame.display.update()

        # user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.event.post(pygame.event.Event(GAME_QUIT))
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP or event.key == pygame.K_DOWN) and curr == 0:
                    curr = 1
                elif (event.key == pygame.K_UP or event.key == pygame.K_DOWN) and curr == 1:
                    curr = 0
                elif event.key == pygame.K_SPACE and curr == 0:
                    running = False
                elif event.key == pygame.K_SPACE and curr == 1:
                    running = False
                    pygame.event.post(pygame.event.Event(GAME_QUIT))


# display UI
def ui(char):
    screen.blit(UI_IMAGE, (0, 0))

    # displaying current and max health
    screen_heart_y = 10
    screen_heart_x = 228

    empty_hearts = char.max_health - char.curr_health
    curr_health = char.curr_health

    while True:
        if (curr_health - 4) >= 0:
            curr_health -= 4
            screen.blit(health_images[4], (screen_heart_x, screen_heart_y))
            screen_heart_x += 31
        elif curr_health == 3:
            curr_health = 0
            screen.blit(health_images[3], (screen_heart_x, screen_heart_y))
            screen_heart_x += 31
        elif curr_health == 2:
            curr_health = 0
            screen.blit(health_images[2], (screen_heart_x, screen_heart_y))
            screen_heart_x += 31
        elif curr_health == 1:
            curr_health = 0
            screen.blit(health_images[1], (screen_heart_x, screen_heart_y))
            screen_heart_x += 31
        elif curr_health == 0 and (empty_hearts - 4) >= 0:
            empty_hearts -= 4
            screen.blit(health_images[0], (screen_heart_x, screen_heart_y))
            screen_heart_x += 31
        else:
            break

    # displaying current exp points
    screen_exp_y = 60
    screen_exp_x = 171

    screen.blit(number_images[char.exp], (screen_exp_x, screen_exp_y))

    # display level points
    screen_lvl_x = 754

    if char.lvl <= 9:
        screen.blit(number_images[char.lvl], (screen_lvl_x, screen_exp_y))
    else:
        tens = char.lvl // 10
        ones = char.lvl % 10
        screen.blit(number_images[tens], (screen_lvl_x, screen_exp_y))
        screen.blit(number_images[ones], (screen_lvl_x + 15, screen_exp_y))

    # display potion amount
    screen_potion = 15

    if char.curr_potions == char.max_potions:
        screen.blit(potion_images[3], (screen_potion, screen_potion))
    elif (char.curr_potions / char.max_potions) >= 1/3:
        screen.blit(potion_images[2], (screen_potion, screen_potion))
    elif char.curr_potions > 0:
        screen.blit(potion_images[1], (screen_potion, screen_potion))
    else:
        screen.blit(potion_images[0], (screen_potion, screen_potion))

    screen_potion_number_x = 73
    screen_potion_number_y = 56

    screen.blit(mini_numbers_images[char.curr_potions], (screen_potion_number_x, screen_potion_number_y))

    # display gold amount
    screen_gold_x = 346

    if char.gold <= 9:
        screen.blit(number_images[char.gold], (screen_gold_x, screen_exp_y))
    else:
        tens = char.gold // 10
        ones = char.gold % 10
        screen.blit(number_images[tens], (screen_gold_x, screen_exp_y))
        screen.blit(number_images[ones], (screen_gold_x + 15, screen_exp_y))

    pygame.display.update()


# display game
def game(stage, char, mobs, dead_mobs):
    step_size = 8

    # background
    if stage < 2:
        screen.blit(stage_1, (0, TOP_OF_SCREEN))
    # elif stage == 1.2:

    # display graves
    for grave in dead_mobs:
        screen.blit(mob_grave, (grave.x, grave.y))

    # player walk
    if char.walk_anim > -1:
        if char.direction == "up":
            if (char.rectangle.y - step_size) >= (TOP_OF_SCREEN + BORDER_SIZE):
                char.rectangle.y -= step_size
            if char.char_class == "main":
                screen.blit(main_char_walk_up[char.walk_anim], (char.rectangle.x, char.rectangle.y))
        elif char.direction == "down":
            if (char.rectangle.y + step_size) <= (HEIGHT - (2 * BORDER_SIZE)):
                char.rectangle.y += step_size
            if char.char_class == "main":
                screen.blit(main_char_walk_down[char.walk_anim], (char.rectangle.x, char.rectangle.y))
        elif char.direction == "left":
            if (char.rectangle.x - step_size) >= BORDER_SIZE:
                char.rectangle.x -= step_size
            if char.char_class == "main":
                screen.blit(main_char_walk_left[char.walk_anim], (char.rectangle.x, char.rectangle.y))
        else:
            if (char.rectangle.x + step_size) <= (WIDTH - (2 * BORDER_SIZE)):
                char.rectangle.x += step_size
            if char.char_class == "main":
                screen.blit(main_char_walk_right[char.walk_anim], (char.rectangle.x, char.rectangle.y))

    # player attack
    if char.atk_anim > -1:
        if char.direction == "up":
            if char.char_class == "main":
                screen.blit(main_char_attack_right[0], (char.rectangle.x, char.rectangle.y))
        elif char.direction == "down":
            if char.char_class == "main":
                screen.blit(main_char_attack_right[0], (char.rectangle.x, char.rectangle.y))
        elif char.direction == "left":
            if char.char_class == "main":
                screen.blit(main_char_attack_left[char.atk_anim], (char.rectangle.x, char.rectangle.y))
        elif char.direction == "right":
            if char.char_class == "main":
                screen.blit(main_char_attack_right[char.atk_anim], (char.rectangle.x, char.rectangle.y))

        # post collision event if user hits enemy
        if char.atk_anim == 2:
            for mob in mobs:
                # only check if alive
                if mob.alive:
                    atk_char = pygame.Rect(0, 0, 0, 0)

                    if char.direction == "up":
                        atk_char = pygame.Rect(char.rectangle.x, char.rectangle.y - CHAR_SIZE,
                                               CHAR_SIZE, CHAR_SIZE)
                    elif char.direction == "down":
                        atk_char = pygame.Rect(char.rectangle.x, char.rectangle.y + CHAR_SIZE,
                                               CHAR_SIZE, CHAR_SIZE)
                    elif char.direction == "left":
                        atk_char = pygame.Rect(char.rectangle.x - CHAR_SIZE, char.rectangle.y,
                                               CHAR_SIZE, CHAR_SIZE)
                    elif char.direction == "right":
                        atk_char = pygame.Rect(char.rectangle.x + CHAR_SIZE, char.rectangle.y,
                                               CHAR_SIZE, CHAR_SIZE)

                    # check hitting mob
                    if atk_char.colliderect(mob.rectangle):
                        mob.hp -= char.atk

                    # change alive state of mob
                    if mob.hp <= 0:
                        mob.alive = False

    # player idle
    if char.idle_anim > -1 and char.walk_anim == -2 and char.atk_anim == -2:
        if char.direction == "up":
            if char.char_class == "main":
                screen.blit(main_char_idle_up[char.idle_anim], (char.rectangle.x, char.rectangle.y))
        elif char.direction == "down":
            if char.char_class == "main":
                screen.blit(main_char_idle_down[char.idle_anim], (char.rectangle.x, char.rectangle.y))
        elif char.direction == "left":
            if char.char_class == "main":
                screen.blit(main_char_idle_left[char.idle_anim], (char.rectangle.x, char.rectangle.y))
        else:
            if char.char_class == "main":
                screen.blit(main_char_idle_right[char.idle_anim], (char.rectangle.x, char.rectangle.y))

    # mobs
    for mob in mobs:
        if mob.alive:
            if mob.walking:
                if mob.direction == "up":
                    if (mob.rectangle.y - step_size) >= (TOP_OF_SCREEN + BORDER_SIZE):
                        mob.rectangle.y -= step_size
                    screen.blit(slime_idle, (mob.rectangle.x, mob.rectangle.y))
                elif mob.direction == "down":
                    if (mob.rectangle.y + step_size) <= (HEIGHT - (2 * BORDER_SIZE)):
                        mob.rectangle.y += step_size
                    screen.blit(slime_idle, (mob.rectangle.x, mob.rectangle.y))
                elif mob.direction == "left":
                    if (mob.rectangle.x - step_size) >= BORDER_SIZE:
                        mob.rectangle.x -= step_size
                    screen.blit(slime_idle, (mob.rectangle.x, mob.rectangle.y))
                else:
                    if (mob.rectangle.x + step_size) <= (WIDTH - (2 * BORDER_SIZE)):
                        mob.rectangle.x += step_size
                    screen.blit(slime_idle, (mob.rectangle.x, mob.rectangle.y))

            elif mob.attacking:
                if mob.direction == "up":
                    screen.blit(slime_idle, (mob.rectangle.x, mob.rectangle.y))
                elif mob.direction == "down":
                    screen.blit(slime_idle, (mob.rectangle.x, mob.rectangle.y))
                elif mob.direction == "left":
                    screen.blit(slime_idle, (mob.rectangle.x, mob.rectangle.y))
                else:
                    screen.blit(slime_idle, (mob.rectangle.x, mob.rectangle.y))

                if mob.atk_anim == 2:
                    atk_mob = pygame.Rect(0, 0, 0, 0)

                    if mob.direction == "up":
                        atk_mob = pygame.Rect(mob.rectangle.x, mob.rectangle.y - CHAR_SIZE,
                                              CHAR_SIZE, CHAR_SIZE)
                    elif mob.direction == "down":
                        atk_mob = pygame.Rect(mob.rectangle.x, mob.rectangle.y + CHAR_SIZE,
                                              CHAR_SIZE, CHAR_SIZE)
                    elif mob.direction == "left":
                        atk_mob = pygame.Rect(mob.rectangle.x - CHAR_SIZE, mob.rectangle.y,
                                              CHAR_SIZE, CHAR_SIZE)
                    else:
                        atk_mob = pygame.Rect(mob.rectangle.x + CHAR_SIZE, mob.rectangle.y,
                                              CHAR_SIZE, CHAR_SIZE)

                    # check hitting mob
                    if atk_mob.colliderect(char.rectangle):
                        char.curr_health -= mob.atk

            else:  # idle
                if mob.direction == "up":
                    screen.blit(slime_idle, (mob.rectangle.x, mob.rectangle.y))
                elif mob.direction == "down":
                    screen.blit(slime_idle, (mob.rectangle.x, mob.rectangle.y))
                elif mob.direction == "left":
                    screen.blit(slime_idle, (mob.rectangle.x, mob.rectangle.y))
                else:
                    screen.blit(slime_idle, (mob.rectangle.x, mob.rectangle.y))

    # boss

    # collision
    for mob in mobs:
        if char.rectangle.colliderect(mob.rectangle):
            pygame.event.post(pygame.event.Event(USER_HIT))

    pygame.display.update()


# determine if b rect is in rect a's range
def in_range(a, b, dist):
    temp_rect = pygame.Rect(a.x - a.width, a.y - a.height, ((dist * 2) + 1) * a.width, ((dist * 2) + 1) * a.height)
    return temp_rect.colliderect(b)


# move mob
def move_mob(char, mob):

    if in_range(char.rectangle, mob.rectangle, 1):  # attack user if nearby
        if mob.atk_break == -1:
            if (mob.rectangle.x <= char.rectangle.x <= mob.rectangle.x + CHAR_SIZE) or\
                    (mob.rectangle.x <= char.rectangle.x + CHAR_SIZE <= mob.rectangle.x + CHAR_SIZE):
                if mob.rectangle.y < char.rectangle.y:
                    mob.direction = "down"
                    mob.attacking = True
                    mob.atk_anim += 1
                    mob.atk_break += 1
                elif mob.rectangle.y > char.rectangle.y:
                    mob.direction = "up"
                    mob.attacking = True
                    mob.atk_anim += 1
                    mob.atk_break += 1
            elif (mob.rectangle.y <= char.rectangle.y <= mob.rectangle.y + CHAR_SIZE) or\
                    (mob.rectangle.y <= char.rectangle.y + CHAR_SIZE <= mob.rectangle.y + CHAR_SIZE):
                if mob.rectangle.x < char.rectangle.x:
                    mob.direction = "right"
                    mob.attacking = True
                    mob.atk_anim += 1
                    mob.atk_break += 1
                elif mob.rectangle.x > char.rectangle.x:
                    mob.direction = "left"
                    mob.attacking = True
                    mob.atk_anim += 1
                    mob.atk_break += 1
    elif in_range(char.rectangle, mob.rectangle, 5):  # walk into attack range
        if (mob.rectangle.x <= char.rectangle.x <= mob.rectangle.x + CHAR_SIZE) or\
                (mob.rectangle.x <= char.rectangle.x + CHAR_SIZE <= mob.rectangle.x + CHAR_SIZE):
            if mob.rectangle.y < char.rectangle.y:
                mob.direction = "down"
                mob.walking = True
                mob.walk_anim += 1
            elif mob.rectangle.y > char.rectangle.y:
                mob.direction = "up"
                mob.walking = True
                mob.walk_anim += 1
        elif (mob.rectangle.y <= char.rectangle.y <= mob.rectangle.y + CHAR_SIZE) or\
                (mob.rectangle.y <= char.rectangle.y + CHAR_SIZE <= mob.rectangle.y + CHAR_SIZE):
            if mob.rectangle.x < char.rectangle.x:
                mob.direction = "right"
                mob.walking = True
                mob.walk_anim += 1
            elif mob.rectangle.x > char.rectangle.x:
                mob.direction = "left"
                mob.walking = True
                mob.walk_anim += 1
    else:  # mindless roaming and waiting until in range
        idle = random.randint(0, 2)
        if idle == 0:
            directions = ["left", "right", "up", "down"]
            mob.direction = random.choice(directions)
            mob.walking = True
            mob.walk_anim += 1
        else:
            mob.idle_anim += 1


# display skill tree menu
def skill_tree(char):
    x = 5
    x += 5


# display win screen
def winner():
    x = 5
    x += 5


# display death
def death():
    running = True
    clock = pygame.time.Clock()
    curr = 0

    while running:
        clock.tick(FPS)

        screen.blit(death_image[curr], (0, 0))
        pygame.display.update()

        # user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.event.post(pygame.event.Event(GAME_QUIT))
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP or event.key == pygame.K_DOWN) and curr == 0:
                    curr = 1
                elif (event.key == pygame.K_UP or event.key == pygame.K_DOWN) and curr == 1:
                    curr = 0
                elif event.key == pygame.K_SPACE and curr == 0:
                    running = False
                    main()
                elif event.key == pygame.K_SPACE and curr == 1:
                    running = False
                    pygame.event.post(pygame.event.Event(GAME_QUIT))


# main function
def main():
    # character stats
    char = User()

    # level
    stage = 1.1

    mobs = spawn_mobs(char.rectangle, stage)
    dead_mobs = []

    # define a variable to control the main loop
    running = True

    # Creating clock class
    clock = pygame.time.Clock()

    # Starting up game
    game_start()

    # main loop
    while running:
        # Prevents obscene amounts of game window refreshing
        clock.tick(FPS)

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT or event.type == GAME_QUIT:
                # exit game/ since we can return to main menu after dying
                pygame.quit()
                running = False
            elif event.type == pygame.KEYDOWN and char.walk_anim == -2 and char.atk_anim == -2:  # walking and turning
                if char.walk_anim == -2 and char.atk_anim == -2:
                    if event.key == pygame.K_UP:
                        if char.direction == "up":
                            char.walk_anim += 1
                        else:
                            char.direction = "up"
                    elif event.key == pygame.K_DOWN:
                        if char.direction == "down":
                            char.walk_anim += 1
                        else:
                            char.direction = "down"
                    elif event.key == pygame.K_LEFT:
                        if char.direction == "left":
                            char.walk_anim += 1
                        else:
                            char.direction = "left"
                    elif event.key == pygame.K_RIGHT:
                        if char.direction == "right":
                            char.walk_anim += 1
                        else:
                            char.direction = "right"
                    elif event.key == pygame.K_SPACE and char.atk_break == 0 and char.char_class != "tank":  # attacking
                        char.atk_anim += 1
                if event.key == pygame.K_p:
                    skill_tree(char)
                if event.key == pygame.K_x:
                    if char.curr_potions > 0:
                        char.curr_potions -= 1
                        char.curr_health += char.potion_heal
                        if char.curr_health > char.max_health:
                            char.curr_health = char.max_health

            # walking into mob
            if event.type == USER_HIT and char.collision_break == 0:
                char.curr_health -= 2
                char.collision_break += 1

        # increment animation screens
        if char.walk_anim == 7:
            char.walk_anim = -2
        elif char.walk_anim > -2:
            char.walk_anim += 1

        # delay next character attack
        if char.atk_break > 0:
            char.atk_break -= 1

        if char.atk_anim == 3:
            char.atk_anim = -2
            char.atk_break = 8
        elif char.atk_anim > -2:
            char.atk_anim += 1

        # increment idle animation
        if char.idle_anim == 7:
            char.idle_anim = 0
        else:
            char.idle_anim += 1

        # increment collision break / so walking into a mob wont insta-kill user
        if char.collision_break == 32:
            char.collision_break = 0
        elif char.collision_break > 0:
            char.collision_break += 1

        # increment mob attack
        for mob in mobs:
            if mob.atk_anim == 3:
                mob.attacking = False
                mob.atk_anim = -1
            elif mob.attacking and mob.atk_anim > -1:
                mob.atk_anim += 1

        # increment mob attack break
        for mob in mobs:
            if mob.atk_break == 16:
                mob.atk_break = -1
            elif mob.atk_break > -1:
                mob.atk_break += 1

        # increment mob walk
        for mob in mobs:
            if mob.walk_anim == 7:
                mob.walking = False
                mob.walk_anim = -1
            elif mob.walking and mob.walk_anim > -1:
                mob.walk_anim += 1

        # increment mob idle
        for mob in mobs:
            if mob.idle_anim == 7:
                mob.idle_anim = -1
            elif mob.idle_anim > -1:
                mob.walk_anim += 1

        if char.exp > 9:
            char.lvl += 1
            char.exp = 0

        ui(char)
        game(stage, char, mobs, dead_mobs)

        # gain drops
        for mob in mobs:
            if not mob.alive:
                char.exp += mob.exp
                char.gold += mob.gold
                dead_mobs.append(mob.rectangle)
                mobs.remove(mob)

        # move mob
        for mob in mobs:
            if (not mob.walking) and (not mob.attacking) and (mob.idle_anim == -1):
                move_mob(char, mob)

        if char.curr_health <= 0:
            death()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
