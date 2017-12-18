import random
from sys import exit
from os import system as do

cards = ['Ae', 'Ac', 'Ap', 'Ao', 'Re', 'Rc', 'Rp', 'Ro', 'Qe', 'Qc', 'Qp', 'Qo', 'Je', 'Jc', 'Jp', 'Jo', '10e', '10c', '10p', '10o', '9e', '9c', '9p', '9o', '8e', '8c', '8p', '8o', '7e', '7c', '7p', '7o', '6e', '6c', '6p', '6o', '5e', '5c', '5p', '5o', '4e', '4c', '4p', '4o', '3e', '3c', '3p', '3o', '2e', '2c', '2p', '2o']
cards_ingame = []
cards_house = []
cards_you = []
score_you = 0
score_house = 0
scoreA = 11
scoreA2 = 1
scoreF = 1
score10 = 10
score9 = 9
score8 = 8
score7 = 7
score6 = 6
score5 = 5
score4 = 4
score3 = 3
score2 = 2
ncards = 0

random.shuffle(cards)

do('clear')
print('')
print('╔╗ ┬  ┌─┐┌─┐┬┌─ ╦┌─┐┌─┐┬┌─')
print('╠╩╗│  ├─┤│  ├┴┐ ║├─┤│  ├┴┐')
print('╚═╝┴─┘┴ ┴└─┘┴ ┴╚╝┴ ┴└─┘┴ ┴')

def show_house():	
	global cards
	global cards_ingame
	global cards_house
	global score_house
	global scoreA
	global scoreA2
	global scoreF
	global score10
	global score9
	global score8
	global score7
	global score6
	global score5
	global score4
	global score3
	global score2
	global ncards
	for i in cards_ingame:
		for a in cards:
			if i == a:
				cards.remove(a)
	cards_house.append(random.choice(cards))#For cryptographically secure random choices (e.g. for generating a passphrase from a wordlist), use random.SystemRandom class
	for i in cards_house:	
		cards_ingame.append(i)
		if i == 'Ae' or i == 'Ac' or i == 'Ap' or i == 'Ao':
			if score_house <= 10:
				score_house += scoreA
			else:
				score_house += scoreA2		
		elif i == 'Re' or i == 'Rc' or i == 'Rp' or i == 'Ro':
			score_house += scoreF
		elif i == 'Qe' or i == 'Qc' or i == 'Qp' or i == 'Qo':
			score_house += scoreF
		elif i == 'Je' or i == 'Jc' or i == 'Jp' or i == 'Jo':
			score_house += scoreF
		elif i == '10e' or i == '10c' or i == '10p' or i == '10o':
			score_house += score10
		elif i == '9e' or i == '9c' or i == '9p' or i == '9o':
			score_house += score9
		elif i == '8e' or i == '8c' or i == '8p' or i == '8o':
			score_house += score8
		elif i == '7e' or i == '7c' or i == '7p' or i == '7o':
			score_house += score7
		elif i == '6e' or i == '6c' or i == '6p' or i == '6o':
			score_house += score6
		elif i == '5e' or i == '5c' or i == '5p' or i == '5o':
			score_house += score5
		elif i == '4e' or i == '4c' or i == '4p' or i == '4o':
			score_house += score4
		elif i == '3e' or i == '3c' or i == '3p' or i == '3o':
			score_house += score3
		elif i == '2e' or i == '2c' or i == '2p' or i == '2o':
			score_house += score2
		if score_house >= 1 and score_house <= 16:
			for i in cards_ingame:
				for a in cards:
					if i == a:
						cards.remove(a)
						cards_house.append(random.choice(cards))
		elif score_house == 20 or score_house == 21:
			print('')
			print('House score is', score_house)
			print('House hand: ', end="")
			print(*cards_house, sep=", ")
			print('')			
		else:
			print('')
			print('House score is', score_house)
			print('House hand: ', end="")
			print(*cards_house, sep=", ")
			print('')

def willloop():
	play_game()

def play_game():
	global cards
	global cards_ingame
	global cards_you
	global score_you
	global scoreA
	global scoreA2
	global scoreF
	global score10
	global score9
	global score8
	global score7
	global score6
	global score5
	global score4
	global score3
	global score2
	global ncards
	for i in cards_ingame:
		for a in cards:
			if i == a:
				cards.remove(a)
	cards_you.append(random.choice(cards))#For cryptographically secure random choices (e.g. for generating a passphrase from a wordlist), use random.SystemRandom class
	print('')
	print('Hand: ', end="")
	print(*cards_you, sep=", ")
	for i in cards_you:
		cards_ingame.append(i)
		if i == 'Ae' or i == 'Ac' or i == 'Ap' or i == 'Ao':
			ace = input('Is the A\'s worth 1 or 11? (default = 11)')
			if ace == '1':
				score_you += scoreA2
			else:
				score_you += scoreA
		elif i == 'Re' or i == 'Rc' or i == 'Rp' or i == 'Ro':
			score_you += scoreF
		elif i == 'Qe' or i == 'Qc' or i == 'Qp' or i == 'Qo':
			score_you += scoreF
		elif i == 'Je' or i == 'Jc' or i == 'Jp' or i == 'Jo':
			score_you += scoreF
		elif i == '10e' or i == '10c' or i == '10p' or i == '10o':
			score_you += score10
		elif i == '9e' or i == '9c' or i == '9p' or i == '9o':
			score_you += score9
		elif i == '8e' or i == '8c' or i == '8p' or i == '8o':
			score_you += score8
		elif i == '7e' or i == '7c' or i == '7p' or i == '7o':
			score_you += score7
		elif i == '6e' or i == '6c' or i == '6p' or i == '6o':
			score_you += score6
		elif i == '5e' or i == '5c' or i == '5p' or i == '5o':
			score_you += score5
		elif i == '4e' or i == '4c' or i == '4p' or i == '4o':
			score_you += score4
		elif i == '3e' or i == '3c' or i == '3p' or i == '3o':
			score_you += score3
		elif i == '2e' or i == '2c' or i == '2p' or i == '2o':
			score_you += score2
	print('Score:', score_you)
	if score_you == 21:
		print('Blackjack m8!')
	if score_you >= 22:
		print('You blew up!')
		keep()
	else:
		print('')
		more_c = input('Want more cards? (Y/N) ')
		if more_c == 'Y' or more_c == 'y' or more_c == 's':		
			score_you = 0			
			willloop()
		else:
			show_house()
			if score_you > score_house or score_house > 21:
				print('You win!')
				keep()
			else:
				print('You lose!')
				keep()
def keep():
	print('')
	keep_p = input('Would you like to keep playing? (Y/N) ')
	if keep_p == 'Y' or keep_p == 'y' or keep_p == 's':
		do('cd /home/diogo/Documents; python3 blackjack_game.py')
	else:
		do('clear')
		exit()

play_game()
