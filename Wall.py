import pygame
from Constants import *

class Wall(pygame.sprite.Sprite):
    # This class derives from the "Sprite" class in Pygame
    
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.image.load("resources/wall2.png").convert()
 
        # Fetch the rectangle object that has the dimensions of the image
        # image and update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
 
        # Instance variables that control the edges (boundries) of wall
        self.left_boundary = 0
        self.right_boundary = 0
        self.top_boundary = 0
        self.bottom_boundary = 0
        
        # Instance variables for our current speed and direction
        # Set to zero since the wall does not move
        self.change_x = 0
        self.change_y = 0
        
    # The update method is called for each game frame and describes
    # what should change with the wall for that frame
    def update(self):

        self.rect.x += self.change_x
        self.rect.y += self.change_y
 
        if self.rect.right >= self.right_boundary or \
           self.rect.left <= self.left_boundary:
                    self.change_x *= -1
 
        if self.rect.bottom >= self.bottom_boundary or \
           self.rect.top <= self.top_boundary:
            self.change_y *= -1