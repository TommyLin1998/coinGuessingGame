#! /usr/bin/env python3

import random

f = open('highScore.txt', 'r+')

highScore = int(f.read())

print('Coin Guessing Game.   All time high score: {}\n'.format(highScore))

score = 0

while True:
    sides = ['heads', 'tails']
    answer = str(random.choice(sides))
    response = input('Predict heads or tails. ')
    if response.lower() == answer:
        score += 1
        print('It is {}.   Your score is: {}'.format(answer, score))
    else:
        break
print('It is {}.   Game over.'.format(answer))

if score > highScore:
    f.seek(0)
    highScore = score
    f.write(str(highScore))
print('Your Score: {}   High Score: {}'.format(score, highScore))

play = input('Do you want to start over? [Y] or [N] ')

if play.lower() == 'y':
    f.seek(0)
    f.write('0')

elif play.lower() == 'n':
    exit()
