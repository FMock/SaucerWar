# Bullet.py by Frank Mock 2016
import pygame
from Constants import *

# This class represents a game bullet
# This class is derives from pygame's Sprite class
class Bullet(pygame.sprite.Sprite):
    
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([3, 10])
        self.image.fill(RED)
 
        self.rect = self.image.get_rect()
        
    # The update method is called for each game frame and describes
    # what should change with the bullet for that frame    
    def update(self):
        # Move the bullet up at a rate of 4 pixels/frame
        self.rect.y -= 4