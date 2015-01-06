import pygame, sys, random
from pygame.locals import *

def main(screen, player, screen_width, screen_height, player_rect):

	font = pygame.font.Font(None, 50) # using the standard pygame.font font

	score = 0
	level = 1

	donut = pygame.image.load('donut.png')
	donuts = []

	enemy = pygame.image.load('enemy.png')
	enemys = []

	life = pygame.image.load('life.png')
	lifes = 3

	life_one = ((screen_width / 2 - life.get_size()[0]) - 10, 10)
	life_two = ((screen_width / 2), 10)
	life_three = ((screen_width / 2 + life.get_size()[0]) + 10, 10)

	donut_event = pygame.USEREVENT+1
	pygame.time.set_timer(donut_event, 1000)

	new_donuts = []

	move_donuts = pygame.USEREVENT+2
	pygame.time.set_timer(move_donuts, 10)

	draw_event = pygame.USEREVENT+3
	pygame.time.set_timer(draw_event, 15)

	enemy_event = pygame.USEREVENT+4

	new_enemys = []

	move_enemys = pygame.USEREVENT+5
	pygame.time.set_timer(move_enemys, 10)

	game = 1

	life_event = pygame.USEREVENT+6
	pygame.time.set_timer(life_event, 1000)

	lifes_falling = []
	lifes_falling_new = []

	move_life = pygame.USEREVENT+7
	pygame.time.set_timer(move_life, 1)

	enemy_speed = 1
	donut_speed = 1

	def gameover(score):
		while True:
			screen = pygame.display.set_mode((500,700))
			font = pygame.font.Font(None, 20)
			screen.fill(000000)
			gameover = font.render('GAME OVER', 1, (0xff, 0xff, 0xff))
			gameover_pos = [screen_width / 2 - gameover.get_size()[0] / 2, 200]
			final = 'Your final score is %d' % score
			final_score = font.render(str(final), 1, (0xff, 0xff, 0xff))
			final_score_pos = [screen_width / 2 - final_score.get_size()[0] / 2, 250]
			screen.blit(gameover, gameover_pos)
			screen.blit(final_score, final_score_pos)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

	while game == 1:

		for event in pygame.event.get():

			if event.type == QUIT: # simply quits the program
				pygame.quit()
				sys.exit()

			elif event.type == donut_event: # let the donuts appear

					donut_x = random.randint(1,screen_width-donut.get_size()[0])
					screen.blit(donut, (donut_x,0))
					donut_position = (donut_x,0)
					donuts.append([donut_x,0])

			elif event.type == enemy_event:

				if len(new_enemys) < 4:
					enemy_x = random.randint(1,screen_width-enemy.get_size()[0])
					screen.blit(enemy, (enemy_x, 0))
					enemy_position = (enemy_x, 0)
					enemys.append([enemy_x, 0])

			elif event.type == life_event:

				if lifes < 2:
					life_x = random.randint(1,screen_width-life.get_size()[0])
					screen.blit(life, (life_x, 0))
					life_position = (life_x, 0)
					lifes_falling.append([life_x, 0])

			elif event.type == move_donuts:

				if len(donuts) > 0:
					new_donuts = []
					for i in donuts:
						i[1] = i[1] + donut_speed
						if i[0] >= player_rect[0] - donut.get_size()[0]/2 and i[0] <= player_rect[0] + player.get_size()[0] and i[1] >= screen_height - player.get_size()[1] - donut.get_size()[1]/2:
							score = score + 10

							if score == 100:
								level = 2
								pygame.time.set_timer(life_event, 2500)
								pygame.time.set_timer(donut_event, 1500)
								pygame.time.set_timer(enemy_event, 2500)
							elif score == 200:
								level = 3
								enemy_speed = 2
								pygame.time.set_timer(enemy_event, 2000)
								pygame.time.set_timer(life_event, 5000)
							elif score == 500:
								level = 4
								enemy_speed = 3
								donut_speed = 2
								pygame.time.set_timer(enemy_event, 1500)
								pygame.time.set_timer(life_event, 7000)
							elif score == 1000:
								level = 5
								pygame.time.set_timer(donut_event, 2000)
							elif score == 2000:
								level = 6
								pygame.time.set_timer(enemy_event, 1000)

							i[1] = screen_height
						elif i[1] < screen_height - donut.get_size()[1]:
								new_donuts.append([i[0], i[1]])
				donuts = new_donuts

			elif event.type == move_enemys:

				if len(enemys) > 0:
					new_enemys = []
					for i in enemys:
						i[1] = i[1] + enemy_speed
						if i[0] >= player_rect[0] - enemy.get_size()[0]/2 and i[0] <= player_rect[0] + player.get_size()[0] and i[1] >= screen_height - player.get_size()[1] - enemy.get_size()[1]:
							lifes = lifes - 1
							i[1] = screen_height
						elif i[1] < screen_height - enemy.get_size()[1]:
							new_enemys.append([i[0], i[1]])
				enemys = new_enemys

			elif event.type == move_life:

				if len(lifes_falling) > 0:
					lifes_falling_new = []
					for i in lifes_falling:
						i[1] = i[1] + 1
						if i[0] >= player_rect[0] - life.get_size()[0]/2 and i[0] <= player_rect[0] + player.get_size()[0] and i[1] >= screen_height - player.get_size()[1] - life.get_size()[1]:
							if lifes < 3:
								lifes = lifes + 1
							i[1] = screen_height
						elif i[1] < screen_height - life.get_size()[1]:
							lifes_falling_new.append([i[0], i[1]])
					lifes_falling = lifes_falling_new

			elif event.type == KEYDOWN: # handling keydown events

				if event.key == K_LEFT: # left key
					screen.fill(000000)
					player_rect = [player_rect[0] - 1, player_rect[1]] # set new position
					if player_rect[0] < 0: # don't you dare leaving the screen
						player_rect = [0, player_rect[1]]

				if event.key == K_RIGHT: # right key
					screen.fill(000000) # erase previous screen
					player_rect = [player_rect[0] + 1, player_rect[1]] # set new position
					if player_rect[0] > screen_width - player.get_size()[0]: # oh no you don't
						player_rect = [screen_width - player.get_size()[0], player_rect[1]]

			elif event.type == draw_event:

				screen.fill(000000)

				show_score = font.render(str(score), 1, (0xff, 0xff, 0xff)) # rendering the score
				leveltext = 'LEVEL: %d' % level
				show_level = font.render(str(leveltext), 1, (0xff, 0xff, 0xff)) # rendering the level

				for i in new_donuts:
					screen.blit(donut, (i[0], i[1]))

				for i in new_enemys:
					screen.blit(enemy, (i[0], i[1]))

				for i in lifes_falling:
					screen.blit(life, (i[0], i[1]))

				if lifes == 3:
					screen.blit(life, life_one)
					screen.blit(life, life_two)
					screen.blit(life, life_three)
				elif lifes == 2:
					screen.blit(life, life_one)
					screen.blit(life, life_two)
				elif lifes == 1:
					screen.blit(life, life_one)
				else:
					game = 0
					gameover(score)

				levelpos = (10, 10)
				scorepos = (screen_width - 10 - show_score.get_size()[0], 10)
				screen.blit(show_score, scorepos) # showing the score
				screen.blit(show_level, levelpos) # showing the level
				screen.blit(player, player_rect) # spawn player at player_rect

				pygame.display.update() # update the screen
