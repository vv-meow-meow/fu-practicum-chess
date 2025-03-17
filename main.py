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

    def choose_figure(self, player: Player) -> tuple[Figure, str]:
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

    def make_move(self, player: Player):
        # 1 часть – выбрать пешку
        # 2 часть – куда её поставить
        chosen_figure, start_pos = self.choose_figure(player)

        available_moves = chosen_figure.get_available_moves(start_pos, self.game_field)
        print("Куда вы хотите поставить пешку?")
        end_pos = input()
        if end_pos not in available_moves:
            raise RuntimeError("Ход недопустим")

        # end_pos_figure = self.game_field.get_figure(end_pos)
        self.game_field.remove_figure(start_pos)
        self.game_field.set_figure(end_pos, chosen_figure)
        self.move_history.append(Move(start_pos, end_pos, chosen_figure))


class Move:
    def __init__(self, start_pos, end_pos, moving_figure: Figure):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.moving_figure = moving_figure

    @staticmethod
    def check_syntax(move: str):
        if (len(move) != 4
                or move[0].upper() not in "ABCDEFGH"
                or move[2].upper() not in "ABCDEFGH"
                or move[1] not in "12345678"
                or move[3] not in "12345678"):
            return False
        return True

    @staticmethod
    def check_first_move_syntax(move: str):
        if (len(move) != 2
                or move[0].upper() not in "ABCDEFGH"
                or move[1].upper() not in "12345678"):
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


if __name__ == "__main__":
    game = GameController()
    game.start_game()
