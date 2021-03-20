#imported modules
from time import *
import random
import threading # https://www.youtube.com/watch?v=Mp6YMt8MSAU&ab_channel=ComputerScienceTutorials

player_num = ["P1", "P2", "P3", "P4"]
number_of_players = 4
#open a text file with a words and make a list out of it
with open("C:\\Users\\AT\\Documents\\git_projects\\brida-app\\brida.py") as f:
    list2 = []
    for item in f:
        list2.append(item.strip())
word_list = list2
player_names1 = []
player_names = []
for i in range(number_of_players): #input player names and make a list out of it
    name = input('enter player name ')
    name = name.upper()
    player_names1.append(name)
def play_again():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')
def random_teams(): # chooese a random team from a list player_names
    while len(player_names1) > 0:
        for _ in range(4):
            player = random.choice(player_names1)
            player_names.append(player)
            player_names1.remove(player)

random_teams_and_players = input('Do you want to randomize teams? (YES or NO)')
if random_teams_and_players.upper().startswith('Y'):
    random_teams()
else:
    player_names = player_names1

player_dict = dict(zip(player_num, player_names))

def gues_word():
    word = random.choice(word_list) #pick a random word from combined_worda_database
    word_list.remove(word)
    return word

print('\nBees: ', player_dict.get('P1'), '& ', player_dict.get('P2') )
print('\nWoolfs: ', player_dict.get('P3'), '& ', player_dict.get('P4'),'\n')
seconds = int(input('TYPE 1 for a correct gues!\nTYPE 2 to skip to the next question. NOTE: it is a -1 point\n\nEnter the number of playseconds and pres ENTER to continue\n\n'))
#my_timer function imported from threading
def countdown():
    global my_timer

    my_timer = seconds
    for x in range(seconds):
        my_timer -= 1
        sleep(1)
    print ('out of time! - PRESS ENTER')

#P1 asking a Q to P2
while True:
    win = 3
    Bees_points = 0
    Woolfs_points = 0
    while True:
        #this starts the my_timer function
        print('Explaining: ', player_dict.get('P1'), '      Guesing: ', player_dict.get('P2'),'\n\n')
        input('press enter to start: ')
        countdown_thread = threading.Thread(target = countdown)
        countdown_thread.start()
        while my_timer > 0:
            #Bees  + P1
            print('\n\n',gues_word())
            answere = input('\nA: ')
            if answere == '1':
                Bees_points +=1
            elif answere == '':
                break
            else:
                Bees_points -=1
            if my_timer == 0:
                break
        print('\nBeess points: ', Bees_points,'\nWoolf points: ', Woolfs_points,'\n\n')
        #this starts the my_timer function
        print('Explaining: ', player_dict.get('P3'), '      Guesing: ', player_dict.get('P4'),'\n\n')
        input('press enter to start: ')
        countdown_thread = threading.Thread(target = countdown)
        countdown_thread.start()
        while my_timer > 0:
            #Woolfs + P1
            print('\n\n',gues_word())
            answere = input('\nA: ')
            if answere == '1':
                Woolfs_points +=1
            elif answere == '':
                 break
            else:
                Woolfs_points -=1
            if my_timer == 0:
                break
        #evaluating results after round
        if Bees_points == Woolfs_points and Bees_points >= win:
            print('final round!')
            print('\nBeess points: ', Bees_points,'\nWoolf points: ', Woolfs_points,'\n\n')
            continue
        else:
            if Woolfs_points >= win and Bees_points < Woolfs_points:
                print('WINNER WOOOOLFS!')
                print('\nBeess points: ', Bees_points,'\nWoolf points: ', Woolfs_points,'\n\n')
                break
            if Bees_points >= win and Bees_points > Woolfs_points:
                print('WINNER BEEEEES!')
                print('\nBeess points: ', Bees_points,'\nWoolf points: ', Woolfs_points,'\n\n')
                break
            else:
                print('\nBeess points: ', Bees_points,'\nWoolf points: ', Woolfs_points,'\n\n')
        #this starts the my_timer function
        print('Explaining: ', player_dict.get('P1'), '      Guesing: ', player_dict.get('P2'),'\n\n')
        input('press enter to start: ')
        countdown_thread = threading.Thread(target = countdown)
        countdown_thread.start()
        while my_timer > 0:
            #Bees  + P1
            print('\n\n',gues_word())
            answere = input('\nA: ')
            if answere == '1':
                Bees_points +=1
            elif answere == '':
                break
            else:
                Bees_points -=1
            if my_timer == 0:
                break
        print('\nBeess points: ', Bees_points,'\nWoolf points: ', Woolfs_points,'\n\n')
        #this starts the my_timer function
        print('Explaining: ', player_dict.get('P4'), '      Guesing: ', player_dict.get('P3'))
        input('press enter to start: ')
        countdown_thread = threading.Thread(target = countdown)
        countdown_thread.start()
        while my_timer > 0:
            #Woolfs + P1
            print('\n\n',gues_word())
            answere = input('\nA: ')
            if answere == '1':
                Woolfs_points +=1
            elif answere == '':
                 break
            else:
                Woolfs_points -=1
            if my_timer == 0:
                break
        #evaluating results after round
        if Bees_points == Woolfs_points and Bees_points >= win:
            print('final round!')
            print('\nBeess points: ', Bees_points,'\nWoolf points: ', Woolfs_points,'\n\n')
            continue
        else:
            if Woolfs_points >= win and Bees_points < Woolfs_points:
                print('WINNER WOOOOLFS!')
                print('\nBeess points: ', Bees_points,'\nWoolf points: ', Woolfs_points,'\n\n')
                break
            if Bees_points >= win and Bees_points > Woolfs_points:
                print('WINNER BEEEEES!')
                print('\nBeess points: ', Bees_points,'\nWoolf points: ', Woolfs_points,'\n\n')
                break
            else:
                print('\nBeess points: ', Bees_points,'\nWoolf points: ', Woolfs_points,'\n\n')
    if not play_again():
        break
