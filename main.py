board_size = 3
none_icon = '#'
board: list[list[str]] = [[none_icon] * board_size for _ in range(board_size)]

WIN_LINES = [
    ((0,0),(0,1),(0,2)), ((1,0),(1,1),(1,2)), ((2,0),(2,1),(2,2)),
    ((0,0),(1,0),(2,0)), ((0,1),(1,1),(2,1)), ((0,2),(1,2),(2,2)),
    ((0,0),(1,1),(2,2)), ((0,2),(1,1),(2,0)),
]

def clear() -> None:
    print('\033[2J\033[H', end='', flush=True)

def draw_board() -> None:
    for row in board:
        print(' | '.join(row))

def winner() -> str | None:
    for line in WIN_LINES:
        a, b, c = (board[y][x] for x, y in line)
        if a != none_icon and a == b == c:
            return a
    return None

def main() -> None:
    used: list[tuple[int, int]] = []

    while True:
        clear()
        state = 'X' if len(used) % 2 == 0 else 'O'
        print(f"{state}'s turn\n")
        draw_board()
        print()

        try:
            x = int(input('введите x: '))
            y = int(input('введите y: '))
        except ValueError:
            continue

        if not (0 <= x < board_size and 0 <= y < board_size):
            continue
        if board[y][x] != none_icon:
            continue

        board[y][x] = state
        used.append((x, y))

        w = winner()
        if w:
            clear()
            draw_board()
            print(f'{w} won!')
            return

        if len(used) == board_size * board_size:
            clear()
            draw_board()
            print('Draw!')
            return

if __name__ == '__main__':
    main()
