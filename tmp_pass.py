#!/usr/bin/env nix-shell
#! nix-shell -i python3 -p python3
"""Generate a few random temporary passwords to use for account resets"""

import random
from pathlib import Path

WORD_LENGTH_MIN = 8
WORD_LENGTH_MAX = 14

words = []
p = Path(__file__).with_name('american-english-huge')
with p.open('r') as wordFile:
    for line in wordFile:
        if len(line) < WORD_LENGTH_MIN or len(line) > WORD_LENGTH_MAX:
            continue
        elif not line.find('\'') == -1:
            continue

        words.append(line)
# print('WordArray: ' + str(len(words)))
I = 0
while I < 10:
    randomWord = words[random.randint(0, len(words))]
    randomNumber = random.randint(0, 100)
    randomPass = randomWord.title().rstrip() + str(randomNumber)
    print(randomPass)
    I += 1
