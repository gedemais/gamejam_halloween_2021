import pygame

NORTH=0
SOUTH=1
EAST=2
WEST=3
V=4

directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

STATE_NONE=-1
STATE_HYDROPHOBE=0
STATE_LEVITATION=1
STATE_ARDENT=2
STATE_PHOSPHORESCENT=3
STATE_TELETUBBIES=4
STATE_WIN=5

potions_drink = [
                    ("Je ne devrais pas boire ca...", False, STATE_NONE, 0),
                    ("Je ne devrais pas boire ca...", False, STATE_NONE, 0),
                    ("On dirait que je repousse l'eau... Ou serait-ce l'eau qui me repousse ?!", True, STATE_HYDROPHOBE, 200),
                    ("Rafraichissant !", False, STATE_NONE),
                    ("Ca fait du bien la ou ca passe.", False, STATE_NONE),
                    ("Je me sens si leger d'un coup...", True, STATE_LEVITATION),
                    ("Je ne devrais pas boire ca...", False, STATE_NONE),
                    ("Je ne devrais pas boire ca...", False, STATE_NONE),
                    ("Ardent comme le soleil, et chaud comme la braise !", True, STATE_ARDENT),
                    ("Je ne devrais pas boire ca...", False, STATE_NONE),
                    ("Je ne devrais pas boire ca...", False, STATE_NONE),
                    ("Aaargh... mes yeux... tout est si lumineux...", True, STATE_PHOSPHORESCENT),
                    ("Shit bruh...", True, STATE_TELETUBBIES),
                    ("Je ne devrais pas boire ca...", False, STATE_NONE),
                    ("Je ne devrais pas boire ca...", False, STATE_NONE),
                    ("Je ne devrais pas boire ca...", False, STATE_NONE),
                    ("Snif... Snif...", False, STATE_NONE),
                    ("Cette piquette est fort mieilleuse !", False, STATE_NONE),
                    ("Je ne devrais pas boire ca...", False, STATE_NONE),
                    ("Je ne devrais pas boire ca...", False, STATE_NONE),
                    ("Je ne devrais pas boire ca...", False, STATE_NONE),
                    ("Une biere qui se respire ? Voyons voir...", True, STATE_WIN)
                ]

potions_ids =   {
                "Huile": 0,
                "Cire d'abeille": 1,
                "Hydrophobie": 2,
                "Red Bull": 3,
                "Vodka": 4,
                "Potion De Levitation": 5,
                "Essence": 6,
                "Nitroglycerine": 7,
                "Solution d'Eau De Feu": 8,
                "Eau Benite": 9,
                "Eau De Galadriel": 10,
                "Potion Phosphorescente": 11,
                "Melange Douteux": 12,
                "Gelee Royale": 13,
                "Napalm": 14,
                "Lotion D'ange": 15,
                "Larmes D'ange": 16,
                "Hydromel": 17,
                "Poudre Blanche": 18,
                "Potion De Nuage": 19,
                "Potion D'uranium": 20,
                "Biere De Dephilosophie": 21,
            }

potions_names =   {
                "0": "Huile",
                "1": "Cire d'abeille",
                "2": "Hydrophobie",
                "3": "Red Bull",
                "4": "Vodka",
                "5": "Potion De Levitation",
                "6": "Essence",
                "7": "Nitroglycerine",
                "8": "Solution d'Eau De Feu",
                "9": "Eau Benite",
                "10": "Eau De Galadriel",
                "11": "Potion Phosphorescente",
                "12": "Melange Douteux",
                "13": "Gelee Royale",
                "14": "Napalm",
                "15": "Lotion D'ange",
                "16": "Larmes D'ange",
                "17": "Hydromel",
                "18": "Poudre Blanche",
                "19": "Potion De Nuage",
                "20": "Potion D'uranium",
                "21": "Biere De Dephilosophie"
            }


class   Hitbox:
    def __init__(self, pos_x, pos_y, width, height):
        self.x = pos_x
        self.y = pos_y
        self.width = width
        self.height = height

    def update_box(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def is_hit(self, box):
        if (self.x < box.x + box.width) and\
            (self.x + self.width > box.x) and\
            (self.y < box.y + box.height) and\
            (self.height + self.y > box.y):
                return True
        else:
            return False


class   Player:
    def __init__(self, x=0, y=0, direction=NORTH):
        self.rpath = 'resources/sprites/player/'
        self.direction = direction
        self.step = 0
        self.substep = 0
        self.speed = 5.5
        self.x = x
        self.y = y
        self.load_sprites()
        self.hitbox = Hitbox(x, y, width=32, height=32)
        self.inventory = [-1 for x in range(20)]
        self.inventory_case_img = pygame.image.load('resources/sprites/inventory_case.png')
        self.handled = 0
        self.state = -1

    def load_sprites(self):
        self.top_walk, self.bot_walk, self.right_walk, self.left_walk = [], [], [], []
        self.walk_ss = pygame.image.load(self.rpath + 'al.png').convert()

        x = 0
        res = 96
        for i in range(8):
            self.top_walk.append(self.walk_ss.subsurface(x, 0, res, res))
            self.right_walk.append(self.walk_ss.subsurface(x, res, res, res))
            self.left_walk.append(self.walk_ss.subsurface(x, res * 2, res, res))
            self.bot_walk.append(self.walk_ss.subsurface(x, res * 3, res, res))
            x += res

        x = 0
        res = 48
        self.potions_images = []
        potion_image = pygame.image.load('resources/sprites/fioles.png')
        for i in range(22):
            self.potions_images.append(potion_image.subsurface(x, 0, res, res))
            x += res

        self.handled_image = pygame.image.load('resources/sprites/selected.png')

    def sip_potion(self, screen, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    if len(self.inventory) == 0:
                        return
                    potion = potions_drink[self.inventory[self.handled]]
                    font = pygame.font.Font('resources/fonts/dpcomic.ttf', 16)
                    text_surface = font.render(potion[0], True, (255, 255, 255))
                    pos = (self.x, self.y)
                    text_rect = text_surface.get_rect(midbottom=pos)
                    screen.blit(text_surface, text_rect)
                    if potion[1]: # is drinkable
                        self.state = potion[2]
                    return True
        return False

    def take_potion(self, potions):
        for i, potion in enumerate(potions):
            if self.hitbox.is_hit(Hitbox(potion[1][0], potion[1][1], 48, 48)):
                for j, c in enumerate(self.inventory):
                    if c == -1:
                        self.inventory[j] = potion[0]
                        potions.pop(i)
                        return


    def walk(self, arrows, room):
        tmp_x = self.x
        tmp_y = self.y
        try:
            self.direction = arrows.index(True)
            self.last_direction = self.direction
            for i in range(4):
                if arrows[i]:
                    self.x += directions[i][0] * self.speed
                    self.y += directions[i][1] * self.speed
            
            self.hitbox.update_box(self.x + 32, self.y + 64)
            for wallbox in room.wallboxes:
                if self.hitbox.is_hit(wallbox):
                    self.x = tmp_x
                    self.y = tmp_y
                    break

            self.substep += 1
            if self.substep >= int(8 / self.speed):
                self.substep = 0
                self.step += 1
            if self.step >= 8 or self.direction != self.last_direction:
                self.step = 0
        except:
            self.step = 0
            pass

        if self.direction == NORTH:
            return self.top_walk[self.step], (self.x, self.y)
        if self.direction == SOUTH:
            return self.bot_walk[self.step], (self.x, self.y)
        if self.direction == EAST:
            return self.right_walk[self.step], (self.x, self.y)
        if self.direction == WEST:
            return self.left_walk[self.step], (self.x, self.y)

