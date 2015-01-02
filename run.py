# some crappy code for a game
# with unicorns and stuff
# i like unicorns

import pygame, sys
from pygame.locals import *

#always needed when using pygame
pygame.init()

# setting the width and height
# then producing a window with
# black background
screen_width = 500
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])
screen.fill(000000)

# loading the unicorn and setting
# it's first position
player = pygame.image.load('player.png')
player_rect = (250,595)

# setting the window title
pygame.display.set_caption('unicorn rescue')

# setting some stuff for moving the unicorn
pressed = pygame.key.get_pressed()
pygame.key.set_repeat(1,5)

# MAIN GAME LOOP
while True:
	for event in pygame.event.get():
		if event.type == QUIT: # simply quits the program
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN: # handling keydown events
			if event.key == K_LEFT: # left key
				screen.fill(000000) # erase previous screen
				player_rect = (player_rect[0] - 2, player_rect[1]) # set new position
				if player_rect[0] < 0: # don't you dare leaving the screen
					player_rect = (0,595)
			if event.key == K_RIGHT: # right key
				screen.fill(000000) # erase previous screen
				player_rect = (player_rect[0] + 2, player_rect[1]) # set new position
				if player_rect[0] > 410: # oh no you don't
					player_rect = (410,595)
	screen.blit(player, player_rect) # spawn player at player_rect
	pygame.display.update() # update the screen

# sorry for the long code
# here's a potato
#   .;;:;;;;;'
#  ,,::::::;:'''
# `::;:::,,::;'',
# ,:,::,:,,,:;'++
# .....,,,,::;;'+
# ....,::::::;'++
# ....,';,:::;'+
#  .,,::::::;''
#    ,::::;;.
