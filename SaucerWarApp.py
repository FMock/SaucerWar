import pygame
import random
from Constants import *
from Game import *

# Saucer War game by Frank Mock 2016
# This game is coded using Python and is based on the pygame library

# Setup the game and start the game loop
def main():
    # Initialize Pygame and set up the window
    pygame.init()
 
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Saucer War")
    # Hide the mouse pointer
    pygame.mouse.set_visible(False)
         
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    # Create an instance of the Game class
    game = Game()

    # Boolean determines game loop to start/stop
    done = False 
 
    # Main game loop
    while not done:
 
        # Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()
 
        # Update object positions, check for collisions
        game.run_logic()
                
        # Draw the current frame
        game.display_frame(screen)
 
        # Pause for the next frame
        clock.tick(FRAME_RATE)
 
    # Close window and exit
    pygame.quit()
 
# Call the main function, start up the game
if __name__ == "__main__":
    main()