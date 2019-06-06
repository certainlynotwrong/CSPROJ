import random
import time

print('Welcome! What is your name?')
name = input()
def displayIntro():
    print(name + ' is in a land full of dragons. In front of ' + name + ',')
    print('He/she/it sees three caves. In one cave, the dragon is friendly')
    print('and will share his treasure with ' + name+ '. The other dragon')
    print('is greedy and hungry, and will eat ' + name + ' on sight.')
    print('The final cave contains a friendly dragon who does not have treasure')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2' and cave !='3':
        print('Which cave will he/she/it go into? (1 or 2 or 3)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print(name + ' approaches the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of his/her/it! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 3)
    
    

    if chosenCave == int(1):
         print('Gives him/her/it his treasure!')

    elif chosenCave == int(2):
         print('Gobbles ' + name + ' down in one bite!')
    else:
        print('says welcome to my cave, ' + name + '. However, I do not have any treasure.')
         

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    displayIntro()

    caveNumber = chooseCave()
    
    checkCave(caveNumber)

    print('Does ' + name + ' want to play again? (yes or no)')
    playAgain = input()
