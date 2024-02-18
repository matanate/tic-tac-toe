import os


class GameBoard:
    # Class constants for player symbols
    PLAYER_X = "X"
    PLAYER_O = "O"

    def __init__(self):
        """
        Initialize the GameBoard object with the initial state.
        """
        self.game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.position_dict = {
            "a1": (0, 0),
            "b1": (0, 1),
            "c1": (0, 2),
            "a2": (1, 0),
            "b2": (1, 1),
            "c2": (1, 2),
            "a3": (2, 0),
            "b3": (2, 1),
            "c3": (2, 2),
        }
        # Set the initial player and game state
        self.player = self.PLAYER_X
        self.game_on = True
        # Print the initial game board
        self.clear_terminal()
        self.print_board()

    def print_board(self):
        """
        Display the current state of the game board.
        """
        print(
            f"""           a     b     c
              |     |     
        1  {self.game_board[0][0]}  |  {self.game_board[0][1]}  |  {self.game_board[0][2]  }
         _____|_____|_____
              |     |     
        2  {self.game_board[1][0]}  |  {self.game_board[1][1]}  |  {self.game_board[1][2]  }
         _____|_____|_____
              |     |     
        3  {self.game_board[2][0]}  |  {self.game_board[2][1]}  |  {self.game_board[2][2]  }
              |     |     """
        )

    def play_turn(self, position, player):
        """
        Play a turn by updating the game board, checking for a win, and switching to the next player.

        Args:
            position (str): The position chosen by the current player.
            player (str): The current player ('X' or 'O').
        """
        if position in self.position_dict:
            self.game_board[self.position_dict[position][0]][
                self.position_dict[position][1]
            ] = player
            # Remove the used position from the dictionary
            self.position_dict.pop(position)
            # Display the updated board, check for a win, and switch to the next player
            self.clear_terminal()
            self.print_board()
            self.check_win()
            self.next_player()

    def next_player(self):
        """
        Switch to the next player.
        """
        if self.player == self.PLAYER_X:
            self.player = self.PLAYER_O
        else:
            self.player = self.PLAYER_X

    def prompt_position(self):
        """
        Prompt the current player to choose a position and play the turn.
        """
        position = input(f"{self.player} turn, chose position: ")
        if position not in self.position_dict:
            # Handle invalid input and prompt again
            print("Wrong input!")
            self.prompt_position()

        # Play the chosen position and switch to the next player
        self.play_turn(position, self.player)

    def check_win(self):
        """
        Check for a win or a draw after each turn.
        """
        for player in [self.PLAYER_X, self.PLAYER_O]:
            for sequence in (
                self.game_board
                + [list(tup) for tup in zip(*self.game_board)]
                + [[self.game_board[i][i] for i in range(3)]]
                + [[self.game_board[i][2 - i] for i in range(3)]]
            ):
                if sequence == [player] * 3:
                    # Display the winner and prompt for a restart
                    print(f"{player} Won!")
                    self.prompt_restart()
                    break
        if not self.position_dict:
            # Display a draw message and prompt for a restart
            print("It's a Draw!")
            self.prompt_restart()

    def prompt_restart(self):
        """
        Prompt the user if they want to play another game and restart if needed.
        """
        user_input = input("Would you like to play another game? (y/n): ")
        if user_input.lower() == "y":
            # Restart the game and switch to the next player
            self.restart_game()
            self.next_player()
        elif user_input.lower() == "n":
            # End the game if the user chooses not to play again
            self.game_on = False
        else:
            print("Wrong input!")
            self.prompt_restart()

    def restart_game(self):
        """
        Restart the game by re-initializing the object.
        """
        self.__init__()

    def clear_terminal(self):
        """
        Clears the terminal."""
        os.system("cls" if os.name == "nt" else "clear")


def main():
    """
    Run the main game loop.
    """
    game = GameBoard()
    while game.game_on:
        game.prompt_position()


if __name__ == "__main__":
    # Run the main function if the script is executed directly
    main()
