# Explosion.py by Frank Mock
import pygame
import random
import Constants

from spritesheet_functions import SpriteSheet

# Explosion represents a game explosion
# This class derives from the "Sprite" class in Pygame
class Explosion(pygame.sprite.Sprite):
    
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
          
        # This holds all the images for the ship animation
        self.explosion_frames = []
        
        # Spritesheet for Explosion is stored in resources dir
        sprite_sheet = SpriteSheet("resources/explosion.png")
        
        # Load all the frames from spritesheet into a list
        image = sprite_sheet.get_image(0, 0, 100, 96)
        self.explosion_frames.append(image)
        image = sprite_sheet.get_image(100, 0, 100, 96)
        self.explosion_frames.append(image)
        image = sprite_sheet.get_image(200, 0, 100, 96)
        self.explosion_frames.append(image)
        image = sprite_sheet.get_image(300, 0, 90, 96)
        self.explosion_frames.append(image)
        image = sprite_sheet.get_image(390, 0, 95, 96)
        self.explosion_frames.append(image)
        image = sprite_sheet.get_image(485, 0, 91, 96)
        self.explosion_frames.append(image)
        image = sprite_sheet.get_image(576, 0, 97, 96)
        self.explosion_frames.append(image)
        image = sprite_sheet.get_image(673, 0, 95, 96)
        self.explosion_frames.append(image)
        image = sprite_sheet.get_image(771, 0, 95, 96)
        self.explosion_frames.append(image)
        image = sprite_sheet.get_image(866, 0, 95, 96)
        self.explosion_frames.append(image)
        image = sprite_sheet.get_image(961, 0, 95, 96)
        self.explosion_frames.append(image)
        image = sprite_sheet.get_image(1058, 0, 95, 96)
        self.explosion_frames.append(image)        
        
        # Set the image the alien sip starts with
        self.image = self.explosion_frames[0]        
       
        # Fetch the rectangle object that has the dimensions of the image
        # image and update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()       
       
        # Have all the explosion frames been shown?
        self.finished = False
        
        # To control when to switch to next frame
        self.frame_count = 0

    # The update method is called for each game frame and describes
    # what should change with the explosion for that frame 
    def update(self):

        if(self.finished == False and self.frame_count < len(self.explosion_frames)):
            self.image = self.explosion_frames[self.frame_count]
            self.frame_count += 1
            if self.frame_count >= len(self.explosion_frames):
                self.finished = True