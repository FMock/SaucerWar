# Player.py by Frank Mock 2016
import pygame
import Constants
 
from spritesheet_functions import SpriteSheet

# Player represents the user controller player on the screen
class Player(pygame.sprite.Sprite):

    # Constructor
    def __init__(self):
 
        # Call the parent's constructor
        super().__init__()
 
        # Attributes
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0
        
        # Instance variables that control the edges of where we bounce
        self.left_boundary = 0
        self.right_boundary = 0        
 
        # These arrays hold all the images for the player to move left/right
        self.moving_frames_l = []
        self.moving_frames_r = []
 
        # Initial direction the player is facing
        self.direction = "R"
 
        # List of sprites we can bump against
        self.level = None
                 
        sprite_sheet = SpriteSheet("resources/tank.png")
        # Load all the right facing images into a list
        image = sprite_sheet.get_image(0, 0, 50, 43)
        self.moving_frames_r.append(image)
        image = sprite_sheet.get_image(50, 0, 50, 43)
        self.moving_frames_r.append(image)
 
        # Load all the right facing images, then flip them
        # to face left.
        image = sprite_sheet.get_image(0, 0, 50, 43)
        image = pygame.transform.flip(image, True, False)
        self.moving_frames_l.append(image)
        image = sprite_sheet.get_image(50, 0, 50, 43)
        image = pygame.transform.flip(image, True, False)
        self.moving_frames_l.append(image)
 
        # Set the image the player starts with
        self.image = self.moving_frames_r[0]
 
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
 
    # The update method is called for each game frame and describes
    # what should change with the player for that frame    
    def update(self):
        # Update the player's position
        # Move left/right
        self.rect.x += self.change_x
        # Move up/down
        self.rect.y += self.change_y
        
        pos = self.rect.x
        if self.direction == "R":
            frame = (pos // 25) % len(self.moving_frames_r)
            self.image = self.moving_frames_r[frame]
        else:
            frame = (pos // 25) % len(self.moving_frames_l)
            self.image = self.moving_frames_l[frame]
            
        if self.rect.right >= self.right_boundary or \
            self.rect.left <= self.left_boundary:
                    self.change_x = 0     
 
    # Player-controlled movement:
    #
    # Called when the user hits the left arrow
    def go_left(self):
        self.change_x = -4
        self.direction = "L"
        
    # Called when the user hits the right arrow
    def go_right(self):
        self.change_x = 4
        self.direction = "R"
        
    # Called when the user lets off the keyboard
    def stop(self):
        self.change_x = 0