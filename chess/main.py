import os

from typing import Literal

from field import GameField
from figures import *


class Player:
    """Represents a chess player.

    Attributes:
        name (str): The player's name.
        color (Literal["black", "white"]): The color assigned to the player.
    """

    def __init__(self, name, color: Literal["black", "white"]):
        """Initializes a new Player instance.

        Args:
            name (str): The name of the player.
            color (Literal["black", "white"]): The color assigned to the player.
        """
        self.name = name
        self.color: Literal["black", "white"] = color


class GameController:
    """Controls the flow of the chess game.

    Attributes:
        game_field (GameField): The game board.
        players (tuple[Player]): Tuple containing the players.
        move_history (list): History of moves made during the game.
        king_killed (bool): Flag indicating if the king has been captured.
    """

    def __init__(self, game_field: GameField = None, players: tuple[Player] = None):
        """Initializes a GameController instance.

        Args:
            game_field (GameField, optional): The game board. Defaults to a new GameField if None.
            players (tuple[Player], optional): The tuple of players. Defaults to None.
        """
        if game_field is None:
            game_field = GameField()
        self.game_field = game_field
        self.players = players
        self.move_history = []
        self.king_killed = False

    @staticmethod
    def _clear_screen():
        """Clears the terminal screen.

        This method clears the console screen using the appropriate command for the operating system.
        """
        os.system("cls" if os.name == "nt" else "clear")

    def _create_players(self):
        """Creates players by prompting the user for their names.

        This method asks the user to input names for both white and black players and assigns their respective colors.
        """
        players = []
        name = input("1 игрок (белые) – назовите ваше имя: ")
        players.append(Player(name, color="white"))
        name = input("2 игрок (чёрные) – назовите ваше имя: ")
        players.append(Player(name, color="black"))
        self.players = players

    def choose_figure(self, player: Player) -> tuple[Figure, str]:
        """Prompts the user to select a figure to move.

        This method handles input validation, ensuring that the selected figure exists, belongs to the current player,
        and has available moves.
        It recursively prompts the user until a valid selection is made.

        Args:
            player (Player): The player who is making the choice.

        Returns:
            tuple[Figure, str]: A tuple containing the selected figure and its starting position.
        """
        print("Выберите пешку (D2)")
        start_pos = input().lower()
        result = None
        if not Move.check_first_move_syntax(start_pos):
            print("Некорректный ввод.")
            result, start_pos = self.choose_figure(player)

        if result is None:
            chosen_figure = self.game_field.get_figure(start_pos)
            if chosen_figure is None:
                print("В данной клетке нет пешки, выберите другую клетку.")
                result, start_pos = self.choose_figure(player)
            else:
                if chosen_figure.color != player.color:
                    print("В выбранной клетка пешка противника, выберите другую клетку.")
                    result, start_pos = self.choose_figure(player)
                else:
                    available_moves = chosen_figure.get_available_moves(start_pos, self.game_field)
                    if len(available_moves) == 0:
                        print("Данная фигура не может ходить, выберите другую фигуру.")
                        result, start_pos = self.choose_figure(player)
                    else:
                        result = chosen_figure

        return result, start_pos

    def choose_end_pos(self, chosen_figure: Figure, start_pos: str) -> str:
        """Prompts the user to select an ending position for the move.

        This method validates the chosen ending position against the available moves for the figure.
        If the move is not valid, it recursively prompts the user for a correct position.

        Args:
            chosen_figure (Figure): The figure that is being moved.
            start_pos (str): The starting position of the figure.

        Returns:
            str: The validated ending position.
        """
        print("Куда вы хотите поставить пешку?")
        end_pos = input().lower()
        available_moves = chosen_figure.get_available_moves(start_pos, self.game_field)
        if end_pos not in available_moves:
            print("Сюда нельзя походить. Выберите другую клетку.")
            end_pos = self.choose_end_pos(chosen_figure, start_pos)
        return end_pos

    def make_move(self, player: Player):
        """Executes a move for the given player.

        This method orchestrates the process of selecting a figure and its target position, updates the game board,
        checks if a king has been captured, and records the move in the move history.

        Args:
            player (Player): The player making the move.
        """
        chosen_figure, start_pos = self.choose_figure(player)
        self.game_field.print_field_with_hints(chosen_figure, start_pos)
        end_pos = self.choose_end_pos(chosen_figure, start_pos)

        end_pos_figure = self.game_field.get_figure(end_pos)
        self.game_field.remove_figure(start_pos)
        if isinstance(end_pos_figure, King):
            self.king_killed = True
        self.game_field.set_figure(end_pos, chosen_figure)
        self.move_history.append(Move(start_pos, end_pos, chosen_figure))

    def start_game(self):
        """Starts and runs the chess game until a king is captured.

        This method handles the game loop, alternating moves between players, updating the board,
        and declaring the winner when the game ends.
        """
        print("Привет! Это игра в шахматы, правила игры: Белые начинают первыми. Удачи!")
        if self.players is None:
            self._create_players()
        winner = None
        while not self.king_killed:
            for player in self.players:
                self.game_field.print_field()
                print(f"Ход {player.color} - Кол-во ходов: {len(self.move_history)}")
                self.make_move(player)
                if self.king_killed:
                    winner = player
                    break
        print(f"Победил {winner.name}! Пешки цвета {winner.color} оказались сильнее!")
        print(f"Всего сделано: {len(self.move_history)} ходов")


class Move:
    """Represents a move in the chess game.

    Attributes:
        start_pos (str): The starting position of the move.
        end_pos (str): The ending position of the move.
        moving_figure (Figure): The chess figure that is moved.
    """

    def __init__(self, start_pos, end_pos, moving_figure: Figure):
        """Initializes a Move instance.

        Args:
            start_pos (str): The starting position of the move.
            end_pos (str): The ending position of the move.
            moving_figure (Figure): The figure that is moved.
        """
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.moving_figure = moving_figure

    @staticmethod
    def check_syntax(move: str):
        """Checks if the move string adheres to the correct syntax.

        The move string should be 4 characters long, with columns represented by letters A-H and rows by numbers 1-8.

        Args:
            move (str): The move string to check (e.g., "D2D4").

        Returns:
            bool: True if the move string is valid, False otherwise.
        """
        if (len(move) != 4
                or move[0].upper() not in "ABCDEFGH"
                or move[2].upper() not in "ABCDEFGH"
                or move[1] not in "12345678"
                or move[3] not in "12345678"):
            return False
        return True

    @staticmethod
    def check_first_move_syntax(move: str):
        """Checks if the initial move string for figure selection adheres to the correct syntax.

        The move string should be 2 characters long,
        with the column represented by a letter A-H and the row by a number 1-8.

        Args:
            move (str): The move string to check (e.g., "D2").

        Returns:
            bool: True if the move string is valid, False otherwise.
        """
        if (len(move) != 2
                or move[0].upper() not in "ABCDEFGH"
                or move[1].upper() not in "12345678"):
            return False
        return True

    def determine_move(self):
        """Determines the type of move (e.g., normal move, castling, pawn promotion).

        This method is a placeholder for determining the specific move type based on the starting and ending positions.
        """
        pass


# class MoveHistory:
#     """WIP"""
#     def __init__(self):
#         self.history = []
#
#     def undo(self, n):
#         for _ in range(n):
#             self.history.pop()
#         print("Done!")


if __name__ == "__main__":
    # game = GameController()
    # game.start_game()
    custom_game_field = GameField(AUTHOR_FIELD)
    custom_game = GameController(custom_game_field)
    custom_game.start_game()
