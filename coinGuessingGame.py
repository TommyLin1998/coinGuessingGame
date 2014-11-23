#! /usr/bin/env python3

import random

f = open('highScore.txt', 'r+')

highScore = int(f.read())

print('Coin Guessing Game.   All time high score: {}\n'.format(highScore))

score = 0

while True:
    sides = ['h', 't']
    answer = str(random.choice(sides))
    response = input('Predict heads or tails. ')
    if response[0].lower() == answer:
        score += 1
        print('It is {}.   Your score is: {}'.format(answer, score))
    else:
        print('It is {}.   Game over.'.format(answer))

        play = input('Do you want to start over? [Y] or [N] ')

        if play.lower() == 'y':
            f.seek(0)
            f.write('0')
            score = 0
            continue
        elif play.lower() == 'n':
            break
        
if score > highScore:
    f.seek(0)
    highScore = score
    f.write(str(highScore))
print('Your Score: {}   High Score: {}'.format(score, highScore))
