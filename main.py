import pygame
from player import *
from pnj import *
from room import Room
from os import system
from time import sleep

#########################
pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 720


screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Al'Chemist")

player = Player(x=646, y=450, direction=WEST)

rooms = {
            'spawner': Room('resources/sprites/tiles/spawner_ground_tile.png', 'spawner'),
            'blue': Room('resources/sprites/tiles/blue_ground_tile.png', 'blue'),
            'green': Room('resources/sprites/tiles/green_ground_tile.png', 'green'),
            'red': Room('resources/sprites/tiles/red_ground_tile.png', 'red'),
            'purple': Room('resources/sprites/tiles/purple_ground_tile.png', 'purple'),
        }

tlbs = [
            pygame.image.load('resources/sprites/teletubbies/a.png'),
            pygame.image.load('resources/sprites/teletubbies/b.png'),
            pygame.image.load('resources/sprites/teletubbies/c.png'),
            pygame.image.load('resources/sprites/teletubbies/d.png'),
            pygame.image.load('resources/sprites/teletubbies/e.png')
        ]

############################ SPAWNER ROOM #############################
room = 'spawner'
rooms[room].add_sprite('resources/sprites/PNJ/dumbledore.png', 560, 436)
rooms[room].add_wallbox(560, 468, 96, 48)

rooms[room].add_sprite('resources/sprites/chaudron.png', 600, 284)
rooms[room].add_wallbox(600, 284, 48, 58)

rooms[room].add_sprite('resources/sprites/almanach/gueridon.png', 500, 260)
rooms[room].add_wallbox(520, 280, 52, 64)

rooms[room].add_sprite('resources/sprites/bench/bench.png', 680, 280)
rooms[room].add_wallbox(690, 280, 86, 64)


rooms[room].add_sprite('resources/sprites/halloween/bones.png', 100, 200)
rooms[room].add_sprite('resources/sprites/halloween/eye.png', 620, 200)

rooms[room].add_sprite('resources/sprites/halloween/column.png', 350, 100)
rooms[room].add_wallbox(350, 110, 72, 195)
rooms[room].add_sprite('resources/sprites/halloween/column.png', 850, 100)
rooms[room].add_wallbox(850, 110, 72, 195)
rooms[room].add_sprite('resources/sprites/halloween/column_c.png', 350, 440)
rooms[room].add_wallbox(350, 500, 72, 145)
rooms[room].add_sprite('resources/sprites/halloween/column.png', 850, 440)
rooms[room].add_wallbox(850, 450, 72, 195)
# Walls
rooms[room].add_wallbox(-10, -10, 10, 740)
rooms[room].add_wallbox(1280, -10, 10, 740)
rooms[room].add_wallbox(-10, -10, 1290, 65)
rooms[room].add_wallbox(-10, 720, 1290, 65)

# Potions
rooms[room].potions.append((0, (365, 280)))
rooms[room].potions.append((1, (865, 280)))
rooms[room].potions.append((3, (365, 625)))
rooms[room].potions.append((6, (865, 625)))
rooms[room].potions.append((9, (600, 340)))


# Portals
rooms[room].add_sprite('resources/sprites/portals/blue.png', 1200, 50)
rooms[room].add_sprite('resources/sprites/portals/green.png', 1200, 200)
rooms[room].add_sprite('resources/sprites/portals/red.png', 1200, 350)
rooms[room].add_sprite('resources/sprites/portals/purple.png', 1200, 500)


############################ BLUE ROOM #############################
room = 'blue'
rooms[room].make_maze(7, 8, 'resources/sprites/tiles/blue_maze_tile.png', 48, 0)
rooms[room].add_sprite('resources/sprites/PNJ/poseidon.png', 1200, 380)
rooms[room].add_wallbox(1210, 390, 72, 142)
rooms[room].add_sprite('resources/sprites/portals/blue.png', 1200, 550)

rooms[room].add_animation('resources/sprites/epreuves/anim_eau/', 8, 1103, 150)
rooms[room].add_animation('resources/sprites/epreuves/anim_eau/', 8, 1196, 150)

rooms[room].add_obstacle(1106, 150, STATE_HYDROPHOBE)

rooms[room].add_potions(potions_ids["Vodka"], 2)


# Walls
rooms[room].add_wallbox(-10, -10, 10, 740)
rooms[room].add_wallbox(1280, -10, 10, 740)
rooms[room].add_wallbox(-10, -10, 1290, 65)
rooms[room].add_wallbox(-10, 720, 1290, 65)
############################ GREEN ROOM #############################
room = 'green'
rooms[room].make_maze(7, 8, 'resources/sprites/tiles/green_maze_tile.png', 48, 0)
rooms[room].add_sprite('resources/sprites/PNJ/panoramix.png', 1180, 430)
rooms[room].add_wallbox(1190, 440, 72, 96)
rooms[room].add_sprite('resources/sprites/portals/green.png', 1200, 550)

rooms[room].add_animation('resources/sprites/epreuves/anim_acide/', 5, 1103, 150)
rooms[room].add_animation('resources/sprites/epreuves/anim_acide/', 5, 1196, 150)

rooms[room].add_obstacle(1106, 150, STATE_LEVITATION)

rooms[room].add_potions(potions_ids["Nitroglycerine"], 2)

# Walls
rooms[room].add_wallbox(-10, -10, 10, 740)
rooms[room].add_wallbox(1280, -10, 10, 740)
rooms[room].add_wallbox(-10, -10, 1290, 65)
rooms[room].add_wallbox(-10, 720, 1290, 65)
############################ RED ROOM #############################
room = 'red'
rooms[room].make_maze(7, 8, 'resources/sprites/tiles/red_maze_tile.png', 48, 0)
rooms[room].add_sprite('resources/sprites/PNJ/tortue_geniale.png', 1210, 470)
rooms[room].add_wallbox(1210, 470, 56, 96)
rooms[room].add_sprite('resources/sprites/portals/red.png', 1200, 550)

rooms[room].add_animation('resources/sprites/epreuves/anim_feu/', 5, 1103, 150)
rooms[room].add_animation('resources/sprites/epreuves/anim_feu/', 5, 1196, 150)
rooms[room].add_obstacle(1106, 150, STATE_ARDENT)

rooms[room].add_potions(potions_ids["Eau De Galadriel"], 2)

# Walls
rooms[room].add_wallbox(-10, -10, 10, 740)
rooms[room].add_wallbox(1280, -10, 10, 740)
rooms[room].add_wallbox(-10, -10, 1290, 65)
rooms[room].add_wallbox(-10, 720, 1290, 65)
############################ PURPLE ROOM #############################
room = 'purple'
rooms[room].make_maze(7, 8, 'resources/sprites/tiles/purple_maze_tile.png', 48, 0)
rooms[room].add_sprite('resources/sprites/PNJ/gandalf.png', 1180, 450)
rooms[room].add_wallbox(1200, 450, 96, 128)
rooms[room].add_sprite('resources/sprites/portals/purple.png', 1200, 550)

rooms[room].add_animation('resources/sprites/epreuves/anim_eau/', 8, 1103, 150)
rooms[room].add_animation('resources/sprites/epreuves/anim_eau/', 8, 1196, 150)
rooms[room].add_obstacle(1106, 150, STATE_HYDROPHOBE)

rooms[room].add_animation('resources/sprites/epreuves/anim_acide/', 5, 1103, 270)
rooms[room].add_animation('resources/sprites/epreuves/anim_acide/', 5, 1196, 270)
rooms[room].add_obstacle(1106, 270, STATE_LEVITATION)

rooms[room].add_animation('resources/sprites/epreuves/anim_feu/', 5, 1103, 390)
rooms[room].add_animation('resources/sprites/epreuves/anim_feu/', 5, 1196, 390)
rooms[room].add_obstacle(1106, 390, STATE_ARDENT)

rooms[room].add_potions(potions_ids["Eau Benite"], 2)

# Walls
rooms[room].add_wallbox(-10, -10, 10, 740)
rooms[room].add_wallbox(1280, -10, 10, 740)
rooms[room].add_wallbox(-10, -10, 1290, 65)
rooms[room].add_wallbox(-10, 720, 1290, 65)

room = 'spawner'

keys = [False, False, False, False]
v = False


############################# Interactions #########################


########### portals

def toggle_blue_portal_hook():
    global room
    global player
    room = 'blue'
    player.x = 1100
    player.y = 572
    player.direction = NORTH


rooms['spawner'].add_interaction(   "Appuyez sur E pour voyager...",
                                    pygame.K_e,
                                    Hitbox(1200, 80, 72, 80),
                                    toggle_blue_portal_hook)


def toggle_green_portal_hook():
    global room
    global player
    room = 'green'
    player.x = 1100
    player.y = 572
    player.direction = NORTH


rooms['spawner'].add_interaction(   "Appuyez sur E pour voyager...",
                                    pygame.K_e,
                                    Hitbox(1200, 230, 72, 80),
                                    toggle_green_portal_hook)

def toggle_red_portal_hook():
    global room
    global player
    room = 'red'
    player.x = 1100
    player.y = 572
    player.direction = NORTH


rooms['spawner'].add_interaction(   "Appuyez sur E pour voyager...",
                                    pygame.K_e,
                                    Hitbox(1200, 380, 72, 80),
                                    toggle_red_portal_hook)

def toggle_purple_portal_hook():
    global room
    global player
    room = 'purple'
    player.x = 1100
    player.y = 572
    player.direction = NORTH


rooms['spawner'].add_interaction(   "Appuyez sur E pour voyager...",
                                    pygame.K_e,
                                    Hitbox(1200, 530, 72, 80),
                                    toggle_purple_portal_hook)

#dialogue_dumbledore = False
#
#def toggle_dialogue_dumbledore():
#    global dialogue_dumbledore
#
#    dialogue_dumbledore = True if dialogue_dumbledore == False else False
#
#
#rooms['spawner'].add_interaction(   "Appuyez sur E pour parler",
#                                    pygame.K_e,
#                                    Hitbox(560, 436, 96, 96),
#                                    toggle_dialogue_dumbledore)

def toggle_spawner_portal_hook():
    global room
    global player
    spawns =    {
                    "blue" : (1100, 50),
                    "green" : (1100, 200),
                    "red" : (1100, 350),
                    "purple" : (1100, 500)
                }
    player.x = spawns[room][0]
    player.y = spawns[room][1]
    room = 'spawner'
    player.direction = NORTH

interaction = ( "Appuyez sur E pour voyager...",
                pygame.K_e,
                Hitbox(1200, 570, 72, 100),
                toggle_spawner_portal_hook)

rooms['blue'].add_interaction(*interaction)
rooms['green'].add_interaction(*interaction)
rooms['red'].add_interaction(*interaction)
rooms['purple'].add_interaction(*interaction)



##################

########## Almanach

almanach_potions = pygame.image.load('resources/sprites/almanach/background_potions.png')

potions_hook = False

def toggle_potions_hook():
    global potions_hook
    potions_hook = False if potions_hook == True else True

def open_potions():
    if potions_hook == False:
        return
    if v:
        system('osascript -e \"set Volume 10\" ; open https://www.youtube.com/watch?v=uDGbCUKqQyQ')
    screen.blit(almanach_potions, (100, 66))

rooms['spawner'].add_interaction("Appuyez sur E pour ouvrir l'almanach",
                                pygame.K_e,
                                Hitbox(500, 260, 72, 84),
                                toggle_potions_hook)
#################

########## Bench
bench = pygame.image.load('resources/sprites/bench/background.png')

bench_hook = False

alambic_in = -1
alambic_out = []
mixer_in = []
mixer_out = -1

error_time = 0


def toggle_bench_hook():
    global bench_hook
    global alambic_in
    global alambic_out
    global mixer_in
    global mixer_out

    alambic_in = -1
    alambic_out = []
    mixer_in = [-1, -1]
    mixer_out = -1
    
    bench_hook = False if bench_hook == True else True


def alambic(player):
    global alambic_in
    global alambic_out
    global error_time

    if potions_tree[player.inventory[player.handled]][0]:
        alambic_in = player.inventory[player.handled]
    else:
        error_time = 60
        return

    if alambic_in > -1:
        alambic_out = [potions_tree[alambic_in][1], potions_tree[alambic_in][2]]

def mixer(player, key):
    global mixer_in
    global mixer_out
    global error_time

    if key == pygame.K_2:
        mixer_in[0] = player.inventory[player.handled]
    elif key == pygame.K_3:
        mixer_in[1] = player.inventory[player.handled]
    elif key == pygame.K_5:
        found = False
        for index, comb in enumerate(potions_tree):
            comb = (comb[1], comb[2])
            if comb.count(mixer_in[0]) == 1 and comb.count(mixer_in[1]) == 1:
                mixer_out = index
                found = True
                break
        if not found:
            error_time = 60
            return
        player.inventory.remove(mixer_in[0])
        player.inventory.remove(mixer_in[1])
        for j, c in enumerate(player.inventory):
            if c == -1:
                player.inventory[j] = mixer_out
                mixer_in = [-1, -1]
                mixer_out = -1
                break




def open_bench(player, events):
    global alambic_in
    global alambic_out
    global mixer_in
    global mixer_out
    global error_time

    if bench_hook == False:
        return
    screen.blit(bench, (100, 16))

    if error_time > 0:
        error_time -= 1

        font = pygame.font.Font('resources/fonts/dpcomic.ttf', 32)
        text_surface = font.render("Liquide non distillable / Melange impossible ...", True, (255, 0, 0))
        pos = (620, 400)
        text_rect = text_surface.get_rect(midbottom=pos)
        screen.blit(text_surface, text_rect)

    for event in events:
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                alambic(player)
            elif event.key == pygame.K_4:
                player.inventory.remove(alambic_in)
                for i in range(2):
                    for j, c in enumerate(player.inventory):
                        if c == -1:
                            player.inventory[j] = alambic_out[i]
                            break
                alambic_in = -1
                alambic_out = []
            elif event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_5:
                mixer(player, event.key)

    if alambic_in > -1:
        screen.blit(player.potions_images[alambic_in], (258, 90))
    if len(alambic_out) > 0:
        screen.blit(player.potions_images[alambic_out[0]], (157, 500))
        screen.blit(player.potions_images[alambic_out[1]], (360, 500))

    if mixer_out > -1:
        screen.blit(player.potions_images[mixer_out], (877, 500))
    if mixer_in[0] != -1:
        screen.blit(player.potions_images[mixer_in[0]], (788, 90))
    if mixer_in[1] != -1:
        screen.blit(player.potions_images[mixer_in[1]], (965, 90))




rooms['spawner'].add_interaction("Appuyez sur E pour experimenter",
                                pygame.K_e,
                                Hitbox(680, 280, 96, 64),
                                toggle_bench_hook)
#################

####################################################################

events = []

def handle_keys(events):
    global player
    global keys
    global room
    global v
    for event in events:
        if event.type == pygame.QUIT:
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit(0)
            if potions_hook == False and bench_hook == False:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    keys[NORTH] = True
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    keys[SOUTH] = True
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    keys[WEST] = True
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    keys[EAST] = True
            if event.key == pygame.K_v:
                v = True

        if event.type == pygame.KEYUP:
            if potions_hook == False and bench_hook == False:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    keys[NORTH] = False
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    keys[SOUTH] = False
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    keys[WEST] = False
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    keys[EAST] = False
            if event.key == pygame.K_v:
                v = False

        if event.type == pygame.MOUSEWHEEL:
            player.handled += event.y
            nb_potions = len(player.inventory) - player.inventory.count(-1) - 1
            if player.handled > nb_potions:
                player.handled = 0
            if player.handled < 0:
                player.handled = nb_potions


def ending(screen):


    creditentials = [
                pygame.image.load('resources/sprites/credits/a.png'),
                pygame.image.load('resources/sprites/credits/b.png'),
                pygame.image.load('resources/sprites/credits/c.png'),
                pygame.image.load('resources/sprites/credits/d.png'),
                pygame.image.load('resources/sprites/credits/e.png')
            ]

    z = 0
    while z <= 4:
        screen.blit(creditentials[z], (0, 0))
        pygame.display.update()

        time = 5000 if z < 2 else 2000

        if z == 2:
            time = 0
            system("osascript -e \"set Volume 10\"")
            system("afplay resources/sounds/psht.mp3")

        pygame.time.wait(time)
        z += 1

    system("afplay resources/sounds/Chocolat.mp3")
    pygame.quit()


def run():
    global events
    running = True
    i = 0
    while running:
        s = 0

        events = pygame.event.get()
        handle_keys(events)

        rooms[room].run(screen, player, events, keys)

        if room == 'spawner':
            open_potions()
            open_bench(player, events)

        if player.state == STATE_TELETUBBIES:
            if i % 2 == 0:
                screen.blit(tlbs[int(i / 2)], (0, 0))
            i += 1
            if i == (len(tlbs) - 1) * 2:
                i = 0
            s = 0.1

        if player.sip_potion(screen, events):
            s = 2

        if player.state == STATE_WIN:
            ending(screen)

        pygame.display.update()
        clock.tick(40)
        sleep(s)

    # Done! Time to quit.
    pygame.quit()

if __name__ == "__main__":
    run()
