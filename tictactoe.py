from tpge import *

TWO_PLAYER = 0
EASY = 1
MEDIUM = 2
HARD = 3
CLICK_NUM = 0
playingGame = True

def game_title():
    return "Tic Tac Toe"

def initial_state():
    return {"X":[], "O":[], "ai":TWO_PLAYER}

def images(S):
    return board() + difficulty_buttons() + draw_o(S) + draw_x(S) + won_game(S)

def board():
    TOP_DIVIDER = (96, 288, 384, 288)
    BOTTOM_DIVIDER = (96, 192, 384, 192)
    LEFT_DIVIDER = (192,96,192,384)
    RIGHT_DIVIDER = (288,96,288,384)
    return [TOP_DIVIDER, BOTTOM_DIVIDER, LEFT_DIVIDER, RIGHT_DIVIDER]

def draw_x(S):
    draw = []
    if 0 in S['X']:
        draw.append((124,356,164,316))
        draw.append((164,356,124,316))
    if 1 in S['X']:
        draw.append((220,356,260,316))
        draw.append((260,356,220,316))
    if 2 in S['X']:
        draw.append((316,356,356,316))
        draw.append((356,356,316,316))
    if 3 in S['X']:
        draw.append((124,260,164,220))
        draw.append((164,260,124,220))
    if 4 in S['X']:
        draw.append((220,260,260,220))
        draw.append((260,260,220,220))
    if 5 in S['X']:
        draw.append((316,260,356,220))
        draw.append((356,260,316,220))
    if 6 in S['X']:
        draw.append((124,164,164,124))
        draw.append((164,164,124,124))
    if 7 in S['X']:
        draw.append((220,164,260,124))
        draw.append((260,164,220,124))
    if 8 in S['X']:
        draw.append((316,164,356,124))
        draw.append((356,164,316,124))
    return draw

def draw_o(S):
    draw = []
    if 0 in S['O']:
        draw.append((144,336,20))
    if 1 in S['O']:
        draw.append((240,336,20))
    if 2 in S['O']:
        draw.append((336,336,20))
    if 3 in S['O']:
        draw.append((144,240,20))
    if 4 in S['O']:
        draw.append((240,240,20))
    if 5 in S['O']:
        draw.append((336,240,20))
    if 6 in S['O']:
        draw.append((144,144,20))
    if 7 in S['O']:
        draw.append((240,144,20))
    if 8 in S['O']:
        draw.append((336,144,20))
    return draw

def difficulty_buttons():
    global CLICK_NUM
    returnList = []
    if CLICK_NUM < 1:
        #Easy button
        returnList.append((490,340,620,300,GREEN))
        returnList.append(("Easy",555,320,12))
        #Medium button
        returnList.append((490,240,620,200,BLUE))
        returnList.append(("Medium",555,220,12))
        #Hard button
        returnList.append((490,140,620,100,RED))
        returnList.append(("Hard",555,120,12))
        #Instructions
        returnList.append(("A simple Tic Tac Toe game. To begin 2 player, simply start playing",320,460,10))
        returnList.append(("otherwise select level of difficult on the left hand side.",320,440,10))
    return returnList

def game_over(State):
    #game_over : State -> Boolean
    #game_over(S) is true if and only if the game is over in state S
    return tie_game(State)

def won_game(S):
    global playingGame
    winningPlayer = []
    wins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    for w in wins:
        if (len(set(w) & set(S['X'])) == 3):
            print("Player X has Won!")
            winningPlayer.append(("Player X has Won!",320,50,20))
            playingGame = False
        elif (len(set(w) & set(S['O'])) == 3):
            print("Player O has Won!")
            winningPlayer.append(("Player O has Won!",320,50,20))
            playingGame = False
    return winningPlayer

def tie_game(State):
    return len(State['X'] + State['O']) == 9

def successor_state(S, P):
    #successor_state : State x Point -> State
    global playingGame
    global CLICK_NUM
    if(playingGame):
        if CLICK_NUM < 1:
            if in_easy_button(P):
                S["ai"] = EASY
                print("we got here")
            if in_medium_button(P):
                S["ai"] = MEDIUM
            if in_hard_button(P):
                S["ai"] = HARD
        #successor_state(S,P) returns the successor state of the game resulting
        player = get_turn(S)
        if in_cell_zero(P) and not already_played(0,S):
            CELL = player.append(0)
        elif in_cell_one(P) and not already_played(1,S):
            CELL = player.append(1)
        elif in_cell_two(P) and not already_played(2,S):
            CELL = player.append(2)
        elif in_cell_three(P) and not already_played(3,S):
            CELL = player.append(3)
        elif in_cell_four(P) and not already_played(4,S):
            CELL = player.append(4)
        elif in_cell_five(P) and not already_played(5,S):
            CELL = player.append(5)
        elif in_cell_six(P) and not already_played(6,S):
            CELL = player.append(6)
        elif in_cell_seven(P) and not already_played(7,S):
            CELL = player.append(7)
        elif in_cell_eight(P) and not already_played(8,S):
            CELL = player.append(8)
        else:
            CELL = player
        CLICK_NUM += 1
    print(S)
    print(CLICK_NUM)
    won_game(S)
    return S #Returns successor state of game after event happens

def already_played(cell, S):
    return cell in S['X'] or cell in S['O']

def get_turn(S):
    if(len(S['X']) > len(S['O'])):
        return S['O']
    else:
        return S['X']

def in_easy_button(P):
    (X,Y) = P
    return 490 < X < 620 and 300 < Y < 340

def in_medium_button(P):
    (X,Y) = P
    return 490 < X < 620 and 200 < Y < 240

def in_hard_button(P):
    (X,Y) = P
    return 490 < X < 620 and 100 < Y < 140

def in_cell_zero(P):
    (X,Y) = P
    return 96 < X < 192 and 288 < Y < 384

def in_cell_one(P):
    (X,Y) = P
    return 192 < X < 288 and 288 < Y < 384

def in_cell_two(P):
    (X,Y) = P
    return 288 < X < 384 and 288 < Y < 384

def in_cell_three(P):
    (X,Y) = P
    return 96 < X < 192 and 192 < Y < 288

def in_cell_four(P):
    (X,Y) = P
    return 192 < X < 288 and 192 < Y < 288

def in_cell_five(P):
    (X,Y) = P
    return 288 < X < 384 and 192 < Y < 288

def in_cell_six(P):
    (X,Y) = P
    return 96 < X < 192 and 96 < Y < 192

def in_cell_seven(P):
    (X,Y) = P
    return 192 < X < 288 and 96 < Y < 192

def in_cell_eight(P):
    (X,Y) = P
    return 288 < X < 384 and 96 < Y < 192

if __name__ == "__main__":
    run_game(game_title, initial_state, successor_state, game_over, images)
