import random

def print_board(heap):
    print(f"Current heap: {'|' * heap}")

def get_user_move(heap):
    return int(input(f"Enter the number of sticks to remove (1 - {min(heap, heap // 2)}): "))

def get_computer_move(heap):
    max_sticks = min(heap, heap // 2)
    return random.randint(1, max_sticks)

def nim_game():
    heap = 16
    player_turn = 1

    while heap > 1:
        print_board(heap)
        sticks_to_remove = get_user_move(heap) if player_turn == 1 else get_computer_move(heap)
        heap -= sticks_to_remove
        player_turn = 3 - player_turn

    print_board(heap)
    winner = "Player 1" if player_turn == 2 else "Computer"
    print(f"{winner} picks the last stick ")
    print(f"\n{winner} is the winner!")

if __name__ == "__main__":
    nim_game()
