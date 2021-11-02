import pygame
import os
from random import shuffle, randrange
from player import *

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

screen_width = 1280
screen_height = 720

 

class Room:
    def __init__(self, bg_tile_path):
        self.bg = pygame.image.load(bg_tile_path)
        self.sprites = []
        self.animations = []
        self.interactions = []
        self.wallboxes = []
        self.potions = []

    def add_animation(self, sprites_path, nb_frames, x, y):
        if x < 0 or x > screen_width or y < 0 or y > screen_height:
            exit(1)
        frames = []
        paths = [path for path in os.listdir(sprites_path)]
        paths.remove('.DS_Store')
        paths.sort()
        for path in paths:
            frames.append(pygame.image.load(sprites_path + path))
        self.animations.append({"frames" : frames,
                                "coords" : (x, y),
                                'index' : 0,
                                'nb_frames' : nb_frames})

    def add_sprite(self, sprite_path, x, y, img=None):
        if x < 0 or x > screen_width or y < 0 or y > screen_height:
            exit(1)
        if img != None:
            self.sprites.append((img, x, y))
        else:
            self.sprites.append((pygame.image.load(sprite_path), x, y))

    def add_wallbox(self, pos_x, pos_y, width, height):
        self.wallboxes.append(Hitbox(pos_x, pos_y, width, height))

    def add_interaction(self, text, key, hitbox, proc):
        self.interactions.append((text, key, hitbox, proc))

    def add_potions(self, goal_id, nb_rand_potions=3):
        goal_potion = (goal_id, (0, 640))
        self.potions.append(goal_potion)

        for i in range(nb_rand_potions):

            potion_id = 2
            while potion_id in (2, 5, 8, 11):
                potion_id = randrange(11)

            x = randrange(21)
            y = randrange(16)
            while self.maze[y][x] == 0:
                x = randrange(21)
                y = randrange(16)

            potion = (potion_id, (x * 48, y * 48))
            self.potions.append(potion)

    def make_maze(self, w, h, sprite_path, pos_x, pos_y):

        self.maze = [[0 for x in range(w * 3 + 1)] for y in range(h * 3 + 1)] 

        vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
        ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
        hor = [["+--"] * w + ['+'] for _ in range(h + 1)]
     
        def walk(x, y):
            vis[y][x] = 1
     
            d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            shuffle(d)
            for (xx, yy) in d:
                if vis[yy][xx]: continue
                if xx == x: hor[max(y, yy)][x] = "+  "
                if yy == y: ver[y][max(x, xx)] = "   "
                walk(xx, yy)
     
        walk(randrange(w), randrange(h))
     
        s = ""
        for (a, b) in zip(hor, ver):
            s += ''.join(a + ['\n'] + b + ['\n'])

        s = s.split('\n')
        for i, line in enumerate(s):
            for j, c in enumerate(line):
                self.maze[i][j] = 1 if c in ('+', '-', '|') else 0

        i = 0
        while i < len(self.maze):
            if self.maze[i][0] == 0:
                break
            else:
                i += 1

        self.maze = self.maze[:i]
        self.maze.pop(len(self.maze) - 2)

        tile = pygame.image.load(sprite_path)
        tw = tile.get_width()
        th = tile.get_height()

        self.nb_sprites = 0
        for y, line in enumerate(self.maze):
            if y == len(self.maze) - 1:
                continue
            for x, val in enumerate(line):
                if x == 0 or (x == len(line) - 1 and y < 3):
                    self.maze[y][x] = 0
                if self.maze[y][x] == 1:
                    self.nb_sprites += 1
                    tx = pos_x + (x * tw)
                    ty = pos_y + (y * th)
                    self.add_sprite("", tx, ty, tile)
                    self.wallboxes.append(Hitbox(tx, ty, tw, th))

        for y, line in enumerate(self.maze):
            for x, val in enumerate(line):
                self.maze[y][x] = 0 if self.maze[y][x] == 1 else 1

        grid = Grid(matrix=self.maze)
        start = grid.node(20, 13)
        end = grid.node(0, 0)
        finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
        path, runs = finder.find_path(start, end, grid)

        if len(path) == 0:
            self.destroy_maze()
            self.make_maze(w, h, sprite_path, pos_x, pos_y)

    def destroy_maze(self):
        self.wallboxes.clear()
        self.sprites.clear()
        del(self.maze)

    def run(self, screen, player, events, keys):
        self.draw(screen, player, keys)
        self.handle_interactions(screen, player, events)

    def handle_interactions(self, screen, player, events):
        for interaction in self.interactions:
            if player.hitbox.is_hit(interaction[2]):
                font = pygame.font.Font('resources/fonts/dpcomic.ttf', 16)
                text_surface = font.render(interaction[0], True, (255, 255, 255))
                pos = (interaction[2].x, interaction[2].y)
                text_rect = text_surface.get_rect(midbottom=pos)
                screen.blit(text_surface, text_rect)


                for event in events:
                    if event.type == pygame.KEYUP:
                        if event.key == interaction[1]:
                            interaction[3]()

    def draw(self, screen, player, keys):
        # background
        for x in range(0, screen_width, self.bg.get_width()):
            for y in range(0, screen_height, self.bg.get_height()):
                screen.blit(self.bg, (x, y))

        # sprites
        for sprite in self.sprites:
            screen.blit(sprite[0], (sprite[1], sprite[2]))

        # animations
        for anim in self.animations:
            screen.blit(anim['frames'][anim['index']], anim['coords'])
            anim['index'] += 1
            if anim['index'] >= anim['nb_frames']:
                anim['index'] = 0

        # potions
        for potion in self.potions:
            screen.blit(player.potions_images[potion[0]], potion[1])
        # player
        img, dims = player.walk(keys, self)

        screen.blit(img, dims)

        x = 0
        for i in player.inventory:
            if i != 0:
                screen.blit(player.inventory_case_img, (x, 660))
            x += 64
