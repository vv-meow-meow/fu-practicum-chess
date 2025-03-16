import os

from figures import *
from field import GameField


class Player:
    def __init__(self, name, color: Literal["black", "white"]):
        self.name = name
        self.color: Literal["black", "white"] = color


class GameController:
    def __init__(self, game_field: GameField = None, players: tuple[Player] = None):
        if game_field is None:
            self.game_field = GameField()
        self.players = players
        self.move_history = []

    @staticmethod
    def _clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    def _create_players(self):
        players = []
        name = input("1 игрок (белые) – назовите ваше имя: ")
        players.append(Player(name, color="white"))
        name = input("2 игрок (чёрные) – назовите ваше имя: ")
        players.append(Player(name, color="black"))
        self.players = players

    def start_game(self):
        print("Привет! Это игра в шахматы, правила игры: Белые начинают первыми. Удачи!")
        if self.players is None:
            self._create_players()
        while True:
            for player in self.players:
                self.game_field.print_field()
                print(f"Ход {player.color}")
                self.make_move(player)

    def make_move(self, player: Player):
        # 1 часть – выбрать пешку
        # 2 часть – куда её поставить
        print("Выберите пешку (D2)")
        start_pos = input()
        figure_start_pos = self.game_field.get_figure(start_pos)
        if figure_start_pos is None:
            raise RuntimeError("Неправильный выбор пешки")
        elif player.color != figure_start_pos.color:
            raise RuntimeError("Игрок выбрал чужую фигуру")

        print("Куда вы хотите поставить пешку?")
        end_pos = input()
        available_moves = figure_start_pos.get_available_moves(start_pos, self.game_field)
        if end_pos not in available_moves:
            raise RuntimeError("Ход недопустим")

        # end_pos_figure = self.game_field.get_figure(end_pos)
        self.game_field.remove_figure(start_pos)
        self.game_field.set_figure(end_pos, figure_start_pos)
        self.move_history.append(Move(start_pos, end_pos, figure_start_pos))


class Move:
    def __init__(self, start_pos, end_pos, moving_figure: Figure):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.moving_figure = moving_figure

    def validate_move(self, game_field: GameField):
        start = game_field.get_figure(self.start_pos)
        end = game_field.get_figure(self.end_pos)

    @staticmethod
    def check_syntax(move: str):
        if (len(move) != 4
                or move[0].upper() not in "ABCDEFGH"
                or move[2].upper() not in "ABCDEFGH"
                or move[1] not in "12345678"
                or move[3] not in "12345678"):
            return False
        return True

    def determine_move(self):
        """Определяет ход – обычный, рокировка, превращение пешки в королеву и тд"""
        pass


class MoveHistory:
    def __init__(self):
        self.history = []

    def undo(self, n):
        for _ in range(n):
            self.history.pop()
        print("Done!")


if __name__ == '__main__':
    game = GameController()
    game.start_game()
