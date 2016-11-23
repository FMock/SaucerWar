# Bomb.py by Frank Mock 2016
import pygame
from Constants import *

# Class that represents a game bomb
# Bomb derives from pygame's Sprite class
class Bomb(pygame.sprite.Sprite):

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([3, 10])
        self.image.fill(GREEN)
 
        self.rect = self.image.get_rect()
    
    # The update method is called for each game frame and describes
    # what changes with the bomb for that frame 
    def update(self):
        # Move the bomb down at rate of 4 pixel/frame
        self.rect.y += 4