import os
import time

board_size = 3
none_icon = '#'
board = [
    [none_icon for x in range(board_size)] for y in range(board_size)
]

class Move:
    def __init__(self, posx, posy, state):
        self.posx = posx
        self.posy = posy
        self.state = state

        self.neighbors = []
        for dt in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dt == 0 and dc == 0:
                    continue
                
                nt, nc = self.posx + dt, self.posy + dc

                if 0 <= nt < board_size and 0 <= nc < board_size:
                    self.neighbors.append((board[nc][nt], dt, dc))

    def make(self):
        try:
            board[self.posy][self.posx] = self.state
        except:
            print('no')

running = True
state_switch = -1
won = False
draw = False
used = []
pot_moves = [
    (0, 1),
    (1, 0),
    (1, 2),
    (2, 1),
    (1, 1)
]

def draw_board():
    for row in board:
        print(' | '.join(row))
        print('-' * board_size * 3)

while running:
    os.system('clear')
    state_switch += 1

    if state_switch % 2 == 0:
        state = 'X'
    else:
        state = 'O'

    print(f"{state}'s turn")
    print('\n')

    draw_board()
    print('\n')


    x, y = int(input('введите x:')), int(input('введите y:'))
    if x > 2 or x < 0:
        print('NO!')
        state_switch -= 1
        time.sleep(1)
        continue
    elif y > 2 or y < 0:
        print('NO!')
        state_switch -= 1
        time.sleep(1)
        continue

    if board[y][x] != none_icon:
        print('Already on the board')
        state_switch -= 1
        time.sleep(1)
        continue
    else:
        move = Move(x, y, state)
        move.make()
        used.append([x, y])

    if len(used) >= 9:
        draw = True
        continue
    
    for pot_spot in pot_moves:
        foo = Move(pot_spot[0], pot_spot[1], board[pot_spot[1]][pot_spot[0]])

        for neighbor in foo.neighbors:
            target = (foo.state, -neighbor[1], -neighbor[2])
            if neighbor[0] == foo.state and foo.state != none_icon and target in foo.neighbors:
                won = True

    if won:
        os.system('clear')
        draw_board()
        print(f'{state} won!')
        running = False
    if draw:
        os.system('clear')
        draw_board()
        print('Draw!')
        running = False

