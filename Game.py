# Game.py by Frank Mock 2016
# Used in the Saucer War game
import pygame
import random
from Alien_Green import *
from Alien_Blue import *
from Alien_Purple import *
from Alien_Yellow import *
from Alien_Gold import *
from Alien_Red import *
from Alien_Bonus import *
from Player import *
from Bullet import *
from Constants import *
from Wall import *
from Bomb import *
from Explosion import *
from Timer import *

# This class represents an instance of the game and contains most of the
# game logic, oject and screen display management
# Create a new instance of this class to reset the game

class Game(object):

    level_number = 0
    score = 0
    lives = 3
    show_splash_screen = True

    # Constructor sets up game by allocating resources and
    # initailizing attributes
    def __init__(self):
 
        self.game_over = False # rename to level_completed
        self.end = False # rename to game-over
        
        self.timer = Timer()
        self.timer.count_down = True
        self.seconds = 6
        self.timer.set_start_time(self.seconds)
        
        
        self.message_timer = Timer()
        self.message_timer.count_down = True
        self.message_timer.set_start_time(4)
        self.show_message = False
        self.message = ""
        
        # Initialize sound and image objects
        # Sound and image files are stored in the resources directory
        self.splash_screen = pygame.image.load("resources/splash-screen.jpg").convert()
        self.background_image = pygame.image.load("resources/background001.jpg").convert()
        self.shoot = pygame.mixer.Sound("resources/shoot.wav")
        self.explosion = pygame.mixer.Sound("resources/explosion.wav")
        self.ping = pygame.mixer.Sound("resources/ping.wav")
        self.hit = pygame.mixer.Sound("resources/hit.wav")
        self.life = pygame.mixer.Sound("resources/life.wav")
                
        # This is a list of 'sprites.' Each alien in the program is
        # added to this list. The list is managed by a class called 'Group.'
        self.alien_list = pygame.sprite.Group()
        
        # List of each bullet
        self.bullet_list = pygame.sprite.Group()
        
        # List of each wall piece
        self.wall_list = pygame.sprite.Group()
        
        # List of alien bombs
        self.bomb_list = pygame.sprite.Group()
        
        # List of explosions
        self.explosion_list = pygame.sprite.Group()
         
        # This is a list of every sprite. All aliens and the player alien as well.
        self.all_sprites_list = pygame.sprite.Group()
        
        # Create the alien invaders
        self.create_aliens()
         
        # Create a player
        self.player = Player()
        self.player.right_boundary = SCREEN_WIDTH + 25
        self.player.left_boundary = -25
        # Put self.player at bottom center position
        self.player.rect.x = SCREEN_WIDTH//2
        self.player.rect.y = SCREEN_HEIGHT - 50
        self.all_sprites_list.add(self.player)
        
        #Build protective walls
        wall_x = 160
        wall_y = SCREEN_HEIGHT - 125
        for i in range(3):
            self.build_wall(wall_x, wall_y)
            wall_x += 300
            
    # Creates various amounts of aliens depending on the current level
    def create_aliens(self):
        num_aliens = 0
        
        if Game.level_number > 0 and Game.level_number < 4:
            num_aliens = 6
            rand = random.randrange(0, 100)
            if rand < 20:
                self.create_bonus_alien()            
        elif Game.level_number > 3 and Game.level_number < 6:
            num_aliens = 8
            rand = random.randrange(0, 100)
            if rand < 40:
                self.create_bonus_alien()            
        elif Game.level_number > 5 and Game.level_number < 8:
            num_aliens = 10
            rand = random.randrange(0, 100)
            if rand < 60:
                self.create_bonus_alien()            
        elif Game.level_number > 7 and Game.level_number < 10:
            num_aliens = 12
            rand = random.randrange(0, 100)
            if rand < 80:
                self.create_bonus_alien()            
        elif Game.level_number > 9:
            num_aliens = 15
            rand = random.randrange(0, 100)
            if rand < 80:
                self.create_bonus_alien()            
                
        # Create Alien objects
        # The Alien type and amount depends on the current level
        # Details of each Alien are defined in their class file
        for i in range(num_aliens):
            # This represents a alien
            alien = Alien_Green()
            
            # Set a random location for the alien
            alien.rect.x = random.randrange(SCREEN_WIDTH - 50)
            alien.rect.y = random.randrange(SCREEN_HEIGHT - 200)
             
            alien.change_x = random.randrange(-3, 4)
            alien.change_y = random.randrange(-3, 4)
            alien.left_boundary = 0
            alien.top_boundary = 0
            alien.right_boundary = SCREEN_WIDTH
            alien.bottom_boundary = SCREEN_HEIGHT - 180
             
            # Add the alien to the list of objects
            self.alien_list.add(alien)
            self.all_sprites_list.add(alien)
                              
            
        if Game.level_number > 3 and Game.level_number < 7:
            for i in range(num_aliens//2):
                # This represents a alien
                alien = Alien_Blue()
                 
                # Set a random location for the alien
                alien.rect.x = random.randrange(SCREEN_WIDTH - 50)
                alien.rect.y = random.randrange(SCREEN_HEIGHT - 200)
                 
                alien.change_x = random.randrange(-3, 4)
                alien.change_y = random.randrange(-3, 4)
                alien.left_boundary = 0
                alien.top_boundary = 0
                alien.right_boundary = SCREEN_WIDTH
                alien.bottom_boundary = SCREEN_HEIGHT - 180
                 
                # Add the alien to the list of objects
                self.alien_list.add(alien)
                self.all_sprites_list.add(alien)
        elif Game.level_number > 6 and Game.level_number < 10:
            for i in range(num_aliens//2):
                # This represents a alien
                alien = Alien_Purple()
                 
                # Set a random location for the alien
                alien.rect.x = random.randrange(SCREEN_WIDTH - 50)
                alien.rect.y = random.randrange(SCREEN_HEIGHT - 200)
                 
                alien.change_x = random.randrange(-3, 4)
                alien.change_y = random.randrange(-3, 4)
                alien.left_boundary = 0
                alien.top_boundary = 0
                alien.right_boundary = SCREEN_WIDTH
                alien.bottom_boundary = SCREEN_HEIGHT - 180
                 
                # Add the alien to the list of objects
                self.alien_list.add(alien)
                self.all_sprites_list.add(alien)
        elif Game.level_number > 9 and Game.level_number < 13:
            for i in range(num_aliens//2):
                # This represents a alien
                alien = Alien_Yellow()
                 
                # Set a random location for the alien
                alien.rect.x = random.randrange(SCREEN_WIDTH - 50)
                alien.rect.y = random.randrange(SCREEN_HEIGHT - 200)
                 
                alien.change_x = random.randrange(-3, 4)
                alien.change_y = random.randrange(-3, 4)
                alien.left_boundary = 0
                alien.top_boundary = 0
                alien.right_boundary = SCREEN_WIDTH
                alien.bottom_boundary = SCREEN_HEIGHT - 180
                 
                # Add the alien to the list of objects
                self.alien_list.add(alien)
                self.all_sprites_list.add(alien)
        elif Game.level_number > 12 and Game.level_number < 15:
            for i in range(num_aliens//2):
                # This represents a alien
                alien = Alien_Gold()
                 
                # Set a random location for the alien
                alien.rect.x = random.randrange(SCREEN_WIDTH - 50)
                alien.rect.y = random.randrange(SCREEN_HEIGHT - 200)
                 
                alien.change_x = random.randrange(-3, 4)
                alien.change_y = random.randrange(-3, 4)
                alien.left_boundary = 0
                alien.top_boundary = 0
                alien.right_boundary = SCREEN_WIDTH
                alien.bottom_boundary = SCREEN_HEIGHT - 180
                 
                # Add the alien to the list of objects
                self.alien_list.add(alien)
                self.all_sprites_list.add(alien)
        elif Game.level_number > 14 and Game.level_number < 18:
            for i in range(num_aliens//2):
                # This represents a alien
                alien = Alien_Red()
                 
                # Set a random location for the alien
                alien.rect.x = random.randrange(SCREEN_WIDTH - 50)
                alien.rect.y = random.randrange(SCREEN_HEIGHT - 200)
                 
                alien.change_x = random.randrange(-3, 4)
                alien.change_y = random.randrange(-3, 4)
                alien.left_boundary = 0
                alien.top_boundary = 0
                alien.right_boundary = SCREEN_WIDTH
                alien.bottom_boundary = SCREEN_HEIGHT - 180
                 
                # Add the alien to the list of objects
                self.alien_list.add(alien)
                self.all_sprites_list.add(alien)  
        
            
    def create_bonus_alien(self):
        # Create bonus alien
        alien = Alien_Bonus()
         
        # Set a random location for the alien
        alien.rect.x = -1000
        alien.rect.y = 75
                 
        alien.change_x = random.randrange(1, 4)
        alien.change_y = 0
        alien.left_boundary = -1000
        alien.top_boundary = 0
        alien.right_boundary = SCREEN_WIDTH + 100
        alien.bottom_boundary = SCREEN_HEIGHT - 180
                 
        # Add the alien to the list of objects
        self.alien_list.add(alien)
        self.all_sprites_list.add(alien)      
        
    # Builds protective wall for player       
    def build_wall(self, x, y):
        #x = SCREEN_WIDTH//2 + 280
        y_start_pos = y
        x_offset = 10
        y_offset = 10
        # Create walls
        for j in range(10):
            wall = Wall()
            wall.rect.x = x
            wall.rect.y = y
            # Add the wall to the list of objects
            self.wall_list.add(wall)
            self.all_sprites_list.add(wall)
            for k in range(4):
                y += y_offset
                wall = Wall()
                wall.rect.x = x
                wall.rect.y = y
                # Add the wall to the list of objects
                self.wall_list.add(wall)
                self.all_sprites_list.add(wall)
            x += x_offset
            y = y_start_pos
            
    # Displays the game level on the game screen      
    def display_level_number(self, screen):
        font = pygame.font.SysFont("serif", 25)
        text = font.render("Level " + str(Game.level_number), True, GREEN)
        center_x = (50) - (text.get_width() // 2)
        center_y = (14) - (text.get_height() // 2)
        screen.blit(text, [center_x, center_y])
    
    # Displays the game score on the game screen
    def display_score(self, screen):
        font = pygame.font.SysFont("serif", 25)
        text = font.render("Score " + str(Game.score), True, GREEN)
        center_x = (50) - (text.get_width() // 2)
        center_y = (34) - (text.get_height() // 2)
        screen.blit(text, [center_x, center_y])
        
    # Displays the number of lives on the game screen 
    def display_lives(self, screen):
        font = pygame.font.SysFont("serif", 25)
        text = font.render("Lives " + str(Game.lives), True, GREEN)
        center_x = (50) - (text.get_width() // 2)
        center_y = (54) - (text.get_height() // 2)
        screen.blit(text, [center_x, center_y])
        
    #  Reset the game
    def restart(self):
        self.__init__()
        
        
    # Keyboard event handler
    # Return True to end game, False otherwise
    def process_events(self):
        pressedkeys = pygame.key.get_pressed()
        if pressedkeys[pygame.K_RETURN]: # Go to next level
            if self.game_over:
                self.restart()
        if pressedkeys[pygame.K_r]: # Restart Game
            Game.level_number = 0
            Game.score = 0
            Game.lives = 3
            show_splash_screen = True
            self.restart()
        if pressedkeys[pygame.K_e]: # End Game
            return True
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # move player left
                    self.player.go_left()
                elif event.key == pygame.K_RIGHT:
                    # move player right
                    self.player.go_right()
                elif event.key == pygame.K_SPACE:
                    # Fire a bullet if the user clicks the mouse button
                    bullet = Bullet()
                    # Set the bullet so it is where the self.player is
                    bullet.rect.x = self.player.rect.x + 25
                    bullet.rect.y = self.player.rect.y
                    # Add the bullet to the lists
                    self.all_sprites_list.add(bullet)
                    self.bullet_list.add(bullet)
                    self.shoot.play()
     
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    #self.player.changespeed(3, 0)
                    self.player.stop()
                elif event.key == pygame.K_RIGHT:
                    #self.player.changespeed(-3, 0)
                    self.player.stop()                    
        # If code reaches this point continue the game          
        return False
    
    # This method is run for each game frame
    # Updates positions and checks for collisions
    def run_logic(self):
        if not self.game_over and not self.end:
            # Move all the sprites
            self.all_sprites_list.update()            
            
            # For each bonus alien if alien.x > screen.width + 10 remove alien
            for bonus_alien in self.alien_list:
                if bonus_alien.rect.x > SCREEN_WIDTH + 10:
                    self.alien_list.remove(bonus_alien)
                    self.all_sprites_list.remove(bonus_alien)
                
                      
            # Have the aliens drop bombs           
            for alien in self.alien_list:
                rand = random.randrange(200)
                if(rand < 2):
                    if(alien.bombing == False and alien.bombs > 0):
                        bomb = Bomb()
                        alien.bombing = True
                        alien.bombs -= 1
                        bomb.rect.x = alien.rect.x + 18
                        bomb.rect.y = alien.rect.y
                        # Add the bomb to the lists
                        self.all_sprites_list.add(bomb)
                        self.bomb_list.add(bomb)                           
            
            # Calculate mechanics for each bullet
            for bullet in self.bullet_list:
         
                # See if it hit an alien or wall
                alien_hit_list = pygame.sprite.spritecollide(bullet, self.alien_list, False) # Changed to False
                wall_hit_list = pygame.sprite.spritecollide(bullet, self.wall_list, True)
         
                # For each alien hit, remove the bullet and add to the score
                for alien in alien_hit_list:
                    alien.hitpoints -= 1
                    if alien.hitpoints <= alien.start_hitpoints/2:
                        alien.not_damaged = False
                    if alien.hitpoints < 1:
                        if alien.bonus_points > 0:
                            Game.score += alien.bonus_points
                        else:
                            Game.score += alien.start_hitpoints * 10
                            
                        # Every 1000 points player gets a new life
                        if Game.score > 0 and Game.score % 100 == 0:
                            Game.lives += 1
                            self.life.play()                        
                        alien_hit_list.remove(alien)
                        self.alien_list.remove(alien)
                        self.all_sprites_list.remove(alien)
                        self.ping.play()
                        print(Game.score)
                    self.explosion.play()
                    explode = Explosion()
                    explode.rect.x = alien.rect.x
                    explode.rect.y = alien.rect.y
                    self.all_sprites_list.add(explode)
                    self.explosion_list.add(explode)            
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)                      
         
                # Kill bullet object if it flies up off the screen
                if bullet.rect.y < -10:
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)
                    
                # Remove wall pieces if they have been hit   
                for wall in wall_hit_list:
                    self.explosion.play()
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)
                    
            # Remove explosion objects after they have exploded
            for exp in self.explosion_list:
                if exp.finished:
                    self.explosion_list.remove(exp)
                    self.all_sprites_list.remove(exp)
            

            # Update game for each bomb dropped
            for bomb in self.bomb_list:
                wall_hit_list = pygame.sprite.spritecollide(bomb, self.wall_list, True)
                bomb_hit_list = pygame.sprite.spritecollide(self.player, self.bomb_list, False)
                
                # Play explosion sound and remove bombs that hit the wall
                for wall in wall_hit_list:
                    self.explosion.play()
                    self.bomb_list.remove(bomb)
                    self.all_sprites_list.remove(bomb)
                    
                # Play hit sound and rove bomb that have hit player
                # Reduce player lives and end game if they have no lives
                for b in bomb_hit_list:
                    self.bomb_list.remove(b)
                    self.all_sprites_list.remove(b)
                    self.hit.play()
                    Game.lives -= 1
                    print("Lives = " + str(Game.lives))
                    if Game.lives == 0:
                        self.end = True
                  
                # Remove alien bombs from game that have droped below screen  
                if bomb.rect.y > SCREEN_HEIGHT:
                    self.bomb_list.remove(bomb)
                    self.all_sprites_list.remove(bomb)
                           
                
            # See if the self.player alien has collided with anything.
            aliens_hit_list = pygame.sprite.spritecollide(self.player, self.alien_list, False)
         
            # Check the list of collisions.
            for alien in aliens_hit_list:
                alien.change_y *= -1
                alien.change_x *= -1
                print("Collided with Alien")
                
            # If alien hits wall play explsion, remove wall piece           
            for wall in self.wall_list:
                alien_hit_list = pygame.sprite.spritecollide(wall, self.alien_list, True)
                for alien in alien_hit_list:
                    self.explosion.play()
                    self.wall_list.remove(wall)
                    self.all_sprites_list.remove(wall)
                    print("Alien Hit Wall")            
 
            # Check to see if the game is over
            if len(self.alien_list) == 0:
                self.game_over = True
                Game.level_number += 1
                    
    # Controls what is drawn to the game screen and when it drawn           
    def display_frame(self, screen):
        # Draw background to screen first
        if Game.show_splash_screen:
            screen.blit(self.splash_screen, [0, 0])
        else:
            screen.blit(self.background_image, [0, 0])
            self.display_level_number(screen)
            self.display_score(screen)
            self.display_lives(screen)
            
        
        if self.game_over:
            self.timer.tick()
            center_x = (SCREEN_WIDTH // 2)
            center_y = (SCREEN_HEIGHT // 2)
            
            if Game.level_number > 1:
                # font = pygame.font.Font("Serif", 25)
                font = pygame.font.SysFont("serif", 25)
                message = "Good Job! Level Completed."           
                text = font.render(message, True, GREEN)
                mid_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
                mid_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)             
                screen.blit(text, [mid_x, mid_y])
                
                font = pygame.font.SysFont("serif", 20)
                message = "ENTER = Go To Next Level"
                text = font.render(message, True, GREEN)
                screen.blit(text, [SCREEN_WIDTH - 300, 8])
                
                font = pygame.font.SysFont("serif", 20)
                message = "F1 = Pause Game"
                text = font.render(message, True, GREEN)
                screen.blit(text, [SCREEN_WIDTH - 300, 24])
            
            
            font = pygame.font.SysFont("serif", 28)
            output_string1 = "Get Ready! {0:02}:{1:02}".format(self.timer.minutes, self.timer.seconds)
            # Blit to the screen
            text1 = font.render(output_string1, True, RED)
            screen.blit(text1, [center_x -100, center_y + 100])
            
            # If time has expired display a message
            if self.timer.total_seconds < 1:
                Game.show_splash_screen = False
                self.restart()
 
        if self.end:
            font = pygame.font.SysFont("serif", 40)
            end_message = "Game Over!"           
            text = font.render(end_message, True, GREEN)
            mid_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            mid_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            text_height = text.get_height()
            screen.blit(text, [mid_x, mid_y])
            
            end_message2 = "Press R Key To Re-start."           
            text = font.render(end_message2, True, GREEN)
            mid_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            mid_y = ((SCREEN_HEIGHT // 2) - (text.get_height() // 2)) + text_height            
            screen.blit(text, [mid_x, mid_y])
            
            end_message3 = "Press E Key To End Game."           
            text = font.render(end_message3, True, GREEN)
            mid_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            mid_y = ((SCREEN_HEIGHT // 2) - (text.get_height() // 2)) + (2 * text_height)            
            screen.blit(text, [mid_x, mid_y])            
 
        if not self.game_over:
            self.all_sprites_list.draw(screen)
            
        # update the screen with what has been drawn.
        pygame.display.flip()    