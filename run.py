# some crappy code for a game
# with unicorns and stuff
# i like unicorns

import pygame, sys
from pygame.locals import *

# import main game code
import main

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
player_size = player.get_size()
player_height = player_size[1]
player_width = player_size[0]
player_rect = ((screen_width - player_width) / 2, screen_height - player_height)

# setting the window title
pygame.display.set_caption('unicorn rescue')

# setting some stuff for moving the unicorn
pressed = pygame.key.get_pressed()
pygame.key.set_repeat(1,5)

# MAIN GAME LOOP
main.main(screen, player, screen_width, screen_height, player_rect)

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
