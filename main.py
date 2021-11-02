import pygame
from player import *
from room import Room
from os import system

#########################
pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 720


screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Al'Chemist")

player = Player(x=646, y=450, direction=WEST)

rooms = {
            'spawner': Room('resources/sprites/tiles/spawner_ground_tile.png'),
            'blue': Room('resources/sprites/tiles/blue_ground_tile.png'),
            'green': Room('resources/sprites/tiles/blue_ground_tile.png'),
            'red': Room('resources/sprites/tiles/red_ground_tile.png'),
            'purple': Room('resources/sprites/tiles/blue_ground_tile.png'),
        }

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

# Walls
rooms[room].add_wallbox(-10, -10, 10, 740)
rooms[room].add_wallbox(1280, -10, 10, 740)
rooms[room].add_wallbox(-10, -10, 1290, 65)
rooms[room].add_wallbox(-10, 720, 1290, 65)
############################ GREEN ROOM #############################
room = 'green'
rooms[room].make_maze(7, 8, 'resources/sprites/tiles/blue_maze_tile.png', 48, 0)
rooms[room].add_sprite('resources/sprites/PNJ/panoramix.png', 1180, 430)
rooms[room].add_wallbox(1190, 440, 72, 96)
rooms[room].add_sprite('resources/sprites/portals/green.png', 1200, 550)
rooms[room].add_animation('resources/sprites/epreuves/anim_eau/', 8, 1103, 150)
rooms[room].add_animation('resources/sprites/epreuves/anim_eau/', 8, 1196, 150)

# Walls
rooms[room].add_wallbox(-10, -10, 10, 740)
rooms[room].add_wallbox(1280, -10, 10, 740)
rooms[room].add_wallbox(-10, -10, 1290, 65)
rooms[room].add_wallbox(-10, 720, 1290, 65)
############################ GREEN ROOM #############################
room = 'red'
rooms[room].make_maze(7, 8, 'resources/sprites/tiles/blue_maze_tile.png', 48, 0)
rooms[room].add_sprite('resources/sprites/PNJ/tortue_geniale.png', 1210, 470)
rooms[room].add_wallbox(1210, 470, 56, 96)
rooms[room].add_sprite('resources/sprites/portals/red.png', 1200, 550)
rooms[room].add_animation('resources/sprites/epreuves/anim_eau/', 8, 1103, 150)
rooms[room].add_animation('resources/sprites/epreuves/anim_eau/', 8, 1196, 150)

# Walls
rooms[room].add_wallbox(-10, -10, 10, 740)
rooms[room].add_wallbox(1280, -10, 10, 740)
rooms[room].add_wallbox(-10, -10, 1290, 65)
rooms[room].add_wallbox(-10, 720, 1290, 65)
############################ GREEN ROOM #############################
room = 'purple'
rooms[room].make_maze(7, 8, 'resources/sprites/tiles/blue_maze_tile.png', 48, 0)
rooms[room].add_sprite('resources/sprites/PNJ/gandalf.png', 1180, 450)
rooms[room].add_wallbox(1200, 450, 96, 128)
rooms[room].add_sprite('resources/sprites/portals/purple.png', 1200, 550)
rooms[room].add_animation('resources/sprites/epreuves/anim_eau/', 8, 1103, 150)
rooms[room].add_animation('resources/sprites/epreuves/anim_eau/', 8, 1196, 150)

# Walls
rooms[room].add_wallbox(-10, -10, 10, 740)
rooms[room].add_wallbox(1280, -10, 10, 740)
rooms[room].add_wallbox(-10, -10, 1290, 65)
rooms[room].add_wallbox(-10, 720, 1290, 65)

room = 'spawner'

keys = [False, False, False, False]
v = False


############################# Interactions #########################


########### portal

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
        system('open https://www.youtube.com/watch?v=uDGbCUKqQyQ')
    screen.blit(almanach_potions, (100, 66))

rooms['spawner'].add_interaction("Appuyez sur E pour ouvrir l'almanach",
                                pygame.K_e,
                                Hitbox(500, 260, 72, 84),
                                toggle_potions_hook)
#################

########## Bench
bench = pygame.image.load('resources/sprites/bench/background.png')

bench_hook = False

def toggle_bench_hook():
    global bench_hook
    bench_hook = False if bench_hook == True else True

def open_bench():
    if bench_hook == False:
        return
    screen.blit(bench, (100, 66))

rooms['spawner'].add_interaction("Appuyez sur E pour experimenter",
                                pygame.K_e,
                                Hitbox(680, 280, 96, 64),
                                toggle_bench_hook)
#################

####################################################################

events = []

def handle_keys(events):
    global keys
    global room
    global v
    for event in events:
        if event.type == pygame.QUIT:
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit(0)
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


def run():
    global events
    running = True
    while running:
        events = pygame.event.get()
        handle_keys(events)

        rooms[room].run(screen, player, events, keys)

        if room == 'spawner':
            open_potions()
            open_bench()

        pygame.display.update()
        clock.tick(40)

    # Done! Time to quit.
    pygame.quit()

if __name__ == "__main__":
    run()
