import os
import time
from alpha_beta_pruning import ai_play
from utils import result, terminal, utility, players, actions, PLAYER_X, PLAYER_O

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def symbol(cell):
    if cell == PLAYER_X:
        return " X "
    elif cell == PLAYER_O:
        return " O "
    return "   "


def print_board(board, last_move=None):
    print()
    print("     1   2   3")
    print("   ╔═══╦═══╦═══╗")
    for r, row in enumerate(board):
        row_label = str(r + 1)
        cells = []
        for c, cell in enumerate(row):
            mark = symbol(cell)
            # Highlight last move
            if last_move and last_move == (r, c):
                mark = f"[{mark.strip()}]" if mark.strip() else mark
            cells.append(mark)
        print(f" {row_label} ║{'║'.join(cells)}║")
        if r < 2:
            print("   ╠═══╬═══╬═══╣")
    print("   ╚═══╩═══╩═══╝")
    print()


def print_header():
    print("╔══════════════════════════════════╗")
    print("║      TIC-TAC-TOE  ·  AI vs You   ║")
    print("║      Alpha-Beta Pruning AI        ║")
    print("╚══════════════════════════════════╝")
    print()


def print_result(board):
    score = utility(board)
    if score == 1:
        msg = "✗  X wins!"
    elif score == -1:
        msg = "○  O wins!"
    else:
        msg = "◈  It's a draw!"

    print("─" * 36)
    print(f"  {msg}")
    print("─" * 36)



def get_human_move(board):
    """Prompt the human player for a valid move."""
    valid = actions(board)
    while True:
        try:
            raw = input("  Your move (row col) e.g. '1 3': ").strip()
            parts = raw.split()
            if len(parts) != 2:
                raise ValueError
            r, c = int(parts[0]) - 1, int(parts[1]) - 1
            if (r, c) not in valid:
                print("  ✗ That cell is taken or out of bounds. Try again.")
                continue
            return (r, c)
        except (ValueError, IndexError):
            print("  ✗ Invalid input. Enter row and column as two numbers (1-3).")


def choose_side():
    """Ask the human which mark they want to play."""
    print("  Choose your mark:")
    print("    [1] X  (goes first)")
    print("    [2] O  (goes second)")
    print()
    while True:
        choice = input("  Enter 1 or 2: ").strip()
        if choice == "1":
            return PLAYER_X
        elif choice == "2":
            return PLAYER_O
        print("  ✗ Please enter 1 or 2.")


def play_again():
    ans = input("\n  Play again? (y/n): ").strip().lower()
    return ans in ("y", "yes", "s", "si", "sí")


def play():
    while True:
        clear()
        print_header()

        human = choose_side()
        board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        last_move = None

        clear()
        print_header()

        while not terminal(board):
            current = players(board)
            print_board(board, last_move)

            if current == human:
                print(f"  Your turn  ({'X' if human == PLAYER_X else 'O'})")
                move = get_human_move(board)
            else:
                ai_mark = "X" if current == PLAYER_X else "O"
                print(f"  AI is thinking  ({ai_mark})...")
                time.sleep(0.4)
                move = ai_play(board)

            board = result(board, move)
            last_move = move

            clear()
            print_header()

        # Game over
        print_board(board, last_move)
        print_result(board)

        if not play_again():
            print("\n  Thanks for playing. Goodbye!\n")
            break


if __name__ == "__main__":
    play()