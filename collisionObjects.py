import pygame, random

screen = pygame.display.set_mode((640, 480))
"""The Bluemonster class will make a blue monster image appear randomly across the screen and 
make him move horizontally."""
class Bluemonster(pygame.sprite.Sprite):
    """ makes a box with a random starting 
        position and the given color.  
        requires screen be predefined and import random """       
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Blue monster east.PNG")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(0, screen.get_width())
        self.rect.centery = random.randrange(0, screen.get_height())
        self.dx = 10
        self.dy = 0

    def update(self):
        self.rect.centerx += self.dx
        if self.rect.right > screen.get_width():
            self.rect.left = 0
"""The Bluemonster2 class will make a blue monster image appear randomly across the screen and 
make him move horizontally."""
class Bluemonster2(pygame.sprite.Sprite):
    """ makes a box with a random starting 
        position and the given color.  
        requires screen be predefined and import random """       
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Blue monster east.PNG")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(0, screen.get_width())
        self.rect.centery = random.randrange(0, screen.get_height())
        self.dx = 10
        self.dy = 0

    def update(self):
        self.rect.centerx += self.dx
        if self.rect.right > screen.get_width():
            self.rect.left = 0
"""The Bluemonster3 class will make a blue monster image appear randomly across the screen and 
make him move horizontally."""
class Bluemonster3(pygame.sprite.Sprite):
    """ makes a box with a random starting 
        position and the given color.  
        requires screen be predefined and import random """       
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Blue monster east.PNG")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(0, screen.get_width())
        self.rect.centery = random.randrange(0, screen.get_height())
        self.dx = 10
        self.dy = 0

    def update(self):
        self.rect.centerx += self.dx
        if self.rect.right > screen.get_width():
            self.rect.left = 0
"""The Orc class will make an image of an orc that the user can control with the mouse."""
class Orc(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Orc north.PNG")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
"""The label class will simply make it possible for text to appear on a particular spot in the
program."""
class Label(pygame.sprite.Sprite):
    """ Label Class (simplest version) 
        Attributes:
            font: any pygame font object
            text: text to display
            center: desired position of label center (x, y)
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("None", 30)
        self.text = ""
        self.center = (320, 240)
                
    def update(self):
        self.image = self.font.render(self.text, 1, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.center
