import random
import os

CELLS=[(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
       (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
       (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
       (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
       (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),]

def clear_the_scree():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_location():
    return random.sample(CELLS, 3)

def moved(player,move):
    x,y=player
    if move == 'A':
        x-=1
    if move == 'D':
        x+=1
    if move == 'W':
        y-=1
    if move == 'S':
        y+=1
    return x,y

def get_move(player):
    moves = {'LEFT':'A', 'RIGHT':'D', 'UP':'W', 'DOWN':'S'}
    temp = []
    x,y =player
    if x==0:
        del moves['LEFT']
    if x==4:
        del moves['RIGHT']
    if y==0:
        del moves['UP']
    if y==4:

        del moves['DOWN']
    for key in moves.values():
        temp.append(key)
    return temp

def again():
    print("do you want to play again?")
    ans = input("enter (y/n): ")
    ans= ans.lower()
    if ans == "y":
        game_loop()
    if ans == "n":
        return

def draw_map(player):
    print(' _'*5)
    wall ='|{}'
    for cell in CELLS:
        x,y = cell
        if x<4:
            line_end = ""
            if cell == player:
                output = wall.format('X')
            else:
                output = wall.format('_')
        else:
            line_end = '\n'
            if cell == player:
                output = wall.format('X|')
            else:
                output = wall.format('_|')
        print(output, end=line_end)

def game_loop():
    player, monster, door = get_location()
    while True:
        draw_map(player)
        valid_move = get_move(player)
        print(valid_move)
        print("your current position: {}".format(player))
        print("you can move {}".format(', '.join(get_move(player))))
        print("where you want to move? (Enter 'quit' to exit)")
        move = input("> ")
        move = move.upper()
        if move =="QUIT":
            break
        if move == "HINT":
            print("the door is in {}".format(door))
        if move in valid_move:
            player = moved(player,move)
            if player == monster:
                print("oh! no you are caught by monster. Better luck next time ")
                again()
                break
            if player ==  door:
                print("bingo!!  wow congratulation you played really well")
                again()
                break
        else:
            print("oh the walls are really ward you can't move \n")

        clear_the_scree()

clear_the_scree()
print("welcome to the game ")
print("so before starting the game let me explain you how it works")
print("SO you are a player and you will be in some random cell in 5*5 matrix container \n "
      "Alnog with you there will be monster and a door kept in random cell. so you need to find the door before monster catch you\n"
      "so let me alert you.. you are the only one who can move the door and monster will be in their stationary position"
      ". enjoy the game created by sajan poudel")
input("enter to start a game.......")
clear_the_scree()
game_loop()







