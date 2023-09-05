#! /usr/bin/env nix-shell
#! nix-shell -i python3 -p python3
"""Generate a webmin account creation line, and new user email"""

import argparse
import random
from pathlib import Path

parser = argparse.ArgumentParser(description='Generate account creation script and new user email.')

parser.add_argument('-u', '--username', nargs='+', help='Full user name for the Account', required=True)
parser.add_argument('-s', '--servername', help='Server name the account is created on', required=True)

args = parser.parse_args()

wordLengthMin = 6
wordLengthMax = 15

words = []
p = Path(__file__).with_name('american-english-huge')
with p.open('r') as wordFile:
    for line in wordFile:
        if len(line) < wordLengthMin or len(line) > wordLengthMax:
            continue
        elif not line.find('\'') == -1:
            continue

        words.append(line)
# print('WordArray: ' + str(len(words)))
randomWord = words[random.randint(0, len(words))]
randomNumber = random.randint(0, 100)
randomPass = randomWord.title().rstrip() + str(randomNumber)

firstName = args.username[0]
lastName = args.username[-1]
firstInitial = firstName[0]

userName = str(firstInitial + lastName).lower()
homedir = '/home/' + firstInitial + '/' + userName

seperator = ' '
fullName = seperator.join(args.username).title()

print('create:' + userName + ':' + randomPass + '::1001:' + fullName + ':' + homedir.lower() +':/bin/bash:::::')
print('\n\n------------------------------------------\n\n')

print('Hi '+ firstName.title() +',\n')
print('I\'ve created an account for you to login to ' +str(args.servername).upper() + '\'s computers, here is the login information.\n')

print('Username: ' + userName)
print('Password: ' + randomPass + '\n')

print('You can change your password from any ' +str(args.servername).upper() + ' computer here:\n')

print('https://server.' +str(args.servername) + '.sd73.bc.ca:20000\n')

print("Please let me know if you need data from a previous site moved over. ")

print("If you have a personal computer that you believe needs access to printing, please contact your supervisor as per Administrative Procedure 145")
