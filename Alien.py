# Alien.py by Frank Mock 2016
import pygame
import random
import Constants

from spritesheet_functions import SpriteSheet

# Alien is the base class for all the aliens in the game
# This class derives from the "Sprite" class in Pygame
class Alien(pygame.sprite.Sprite):
    
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
          
        # This holds all the images for the ship animation
        self.ship_frames = []
               
        # Instance variables that control the edges of where we bounce
        self.left_boundary = 0
        self.right_boundary = 0
        self.top_boundary = 0
        self.bottom_boundary = 0
        
        # Instance variables for our current speed and direction
        self.change_x = 0
        self.change_y = 0
        
        self.hitpoints = 0
        
        # Has the alien droped a bomb
        self.bombing = False
        
        # The number of alien bombs
        self.bombs = 40
        
        # Bonus points
        self.bonus_points = 0
        
    # Every objects update method is called for each frame of the game
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
 
        if self.rect.right >= self.right_boundary or \
           self.rect.left <= self.left_boundary:
                    self.change_x *= -1
 
        if self.rect.bottom >= self.bottom_boundary or \
           self.rect.top <= self.top_boundary:
            self.change_y *= -1
           
        # Change to next sprite sheet image every 20 pixels of sprite movement 
        pos = self.rect.x
        frame = (pos // 20) % len(self.ship_frames)
        self.image = self.ship_frames[frame]        
        
        # Randomly activate bombing ability    
        rand = random.randrange(200)
        if(rand < 10):
            self.bombing = False