# Alien_Green by Frank Mock 2016
import pygame
import random
import Constants
from Alien import *

from spritesheet_functions import SpriteSheet

# This class derives from the "Alien" class
# Green alien starts off with 2 HP
class Alien_Green(Alien):
    
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Spritesheet stored in the resources directory          
        sprite_sheet = SpriteSheet("resources/green-ship.png")
        
        # Load all the frames from spritesheet into a list
        image = sprite_sheet.get_image(0, 0, 52, 28)
        self.ship_frames.append(image)
        image = sprite_sheet.get_image(52, 0, 52, 28)
        self.ship_frames.append(image)
        image = sprite_sheet.get_image(0, 28, 52, 28)
        self.ship_frames.append(image)
        image = sprite_sheet.get_image(52, 28, 52, 28)
        self.ship_frames.append(image)

        # Set the image the alien sip starts with
        self.image = self.ship_frames[0]
        
        # Fetch the rectangle object that has the dimensions of the image
        # image and update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        
        # This alien starts off with 2 HP
        self.hitpoints = 2
        self.start_hitpoints = 2
        
        self.not_damaged = True
        
    def load_frames(self):
        pass
    
    # The update method is called for each game frame and describes
    # what should change with the object for that frame    
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
        size = 2
        if self.not_damaged:
            frame = (pos // 20) % 2
        else:
            frame = (pos // 20) % len(self.ship_frames)
            
        self.image = self.ship_frames[frame]
        
        # Randomly activate bombing ability    
        rand = random.randrange(200)
        if(rand < 10):
            self.bombing = False    
        