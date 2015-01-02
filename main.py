import pygame, sys
from pygame.locals import *

def main(screen, player, screen_width, screen_height, player_rect):
	font = pygame.font.Font(None, 50)
	score = 0
	while True:
		for event in pygame.event.get():
			if event.type == QUIT: # simply quits the program
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN: # handling keydown events
				if event.key == K_LEFT: # left key
					score = score + 1
					screen.fill(000000) # erase previous screen
					player_rect = (player_rect[0] - 2, player_rect[1]) # set new position
					if player_rect[0] < 0: # don't you dare leaving the screen
						player_rect = (0, player_rect[1])
				if event.key == K_RIGHT: # right key
					score = score + 1
					screen.fill(000000) # erase previous screen
					player_rect = (player_rect[0] + 2, player_rect[1]) # set new position
					if player_rect[0] > screen_width - player.get_size()[0]: # oh no you don't
						player_rect = (screen_width - player.get_size()[0], player_rect[1])
		show_score = font.render(str(score), 1, (0xff, 0xff, 0x00))
		scorepos = (screen_width - 10 - show_score.get_size()[0], 10)
		screen.blit(show_score, scorepos)
		screen.blit(player, player_rect) # spawn player at player_rect
		pygame.display.update() # update the screen
