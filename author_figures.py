from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from field import GameField

from figures import *


class Balloon(Figure):
    """Фигура "Воздушный шар" – 1 фигура на клетках B и G (вместо коней)
    – взлетает в небо и падает на фигуру противника (кроме короля и ферзя) – самоуничтожается при использовании
    – ходит куда угодно (кроме короля и ферзя)
    – при ходе рубит
    – самоуничтожается после хода
    """

    def __str__(self):
        return "⚪" if self.color == "white" else "⚫"

    def _get_moves(self, pos: str) -> list:
        moves = []
        for col in range(97, 104 + 1):
            for row in range(1, 8 + 1):
                moves.append(f"{chr(col)}{row}")
        moves.remove(pos)
        return moves

    def get_available_moves(self, pos: str, board: GameField) -> list:
        pos = pos.lower()
        moves = self._get_moves(pos)
        result = []
        for move in moves:
            figure_on_move = board.get_figure(move)
            if figure_on_move is None:
                result.append(move)
            else:
                if figure_on_move.color != self.color:
                    if not (isinstance(figure_on_move, King) or isinstance(figure_on_move, Queen)):
                        result.append(move)
        return result


class Tank(Figure):
    """Фигура "Танк (Рыцарь с огромным щитом перед ним)"
    – может передвигаться только по диагональным клеткам
    – рубит только спереди
    """

    def __str__(self):
        return "🏳" if self.color == "white" else "🏴"

    def _get_moves(self, pos: str) -> list:
        col = ord(pos[0])
        row = int(pos[1])

        if row == 8:
            return []

        moves = []
        left_move = chr(col - 1)
        if "a" <= left_move <= "h":
            moves.append(f"{left_move}{row + 1}")
        right_move = chr(col + 1)
        if "a" <= right_move <= "h":
            moves.append(f"{right_move}{row + 1}")

        return moves

    def get_available_moves(self, pos: str, board: GameField) -> list:
        pos = pos.lower()
        moves = self._get_moves(pos)

        result = []
        for move in moves:
            figure_on_move = board.get_figure(move)
            if figure_on_move is None:
                result.append(move)

        col = pos[0]
        row = int(pos[1])
        capture_move = f"{col}{row + 1}"
        figure_on_capture = board.get_figure(capture_move)
        if figure_on_capture is not None:
            if figure_on_capture.color != self.color:
                result.append(capture_move)

        return result


class PEKKA(Figure):
    """Фигура "ПЕККА"
    – ходит только вперёд на 1 ход
    – может рубить пешки на 1 и 2 клетки спереди
    """

    def __str__(self):
        return "✝" if self.color == "white" else "✞"

    def _get_moves(self, pos: str) -> list:
        col = pos[0]
        row = int(pos[1])
        if row == 8:
            return []

        return [f"{col}{row + 1}"]

    def get_available_moves(self, pos: str, board: GameField) -> list:
        pos = pos.lower()
        moves = self._get_moves(pos)
        result = []
        for move in moves:
            figure_on_move = board.get_figure(move)
            if figure_on_move is None:
                result.append(move)
            elif figure_on_move.color != self.color:
                result.append(move)

        col = pos[0]
        row = int(pos[1])
        capture_move = f"{col}{row + 2}"
        figure_on_capture = board.get_figure(capture_move)
        if figure_on_capture is not None:
            if figure_on_capture.color != self.color:
                result.append(capture_move)

        return result


CUSTOMIZED_FIELD = {
    "a": [Rook("white"), Pawn("white"), None, None, None, None, Pawn("black"), Rook("black")],
    "b": [Balloon("white"), Pawn("white"), None, None, None, None, Pawn("black"), Balloon("black")],
    "c": [Bishop("white"), Pawn("white"), None, None, None, None, Pawn("black"), Bishop("black")],
    "d": [Queen("white"), Tank("white"), None, None, None, None, Tank("black"), Queen("black")],
    "e": [King("white"), PEKKA("white"), None, None, None, None, PEKKA("black"), King("black")],
    "f": [Bishop("white"), Pawn("white"), None, None, None, None, Pawn("black"), Bishop("black")],
    "g": [Knight("white"), Pawn("white"), None, None, None, None, Pawn("black"), Knight("black")],
    "h": [Rook("white"), Pawn("white"), None, None, None, None, Pawn("black"), Rook("black")]
}

if __name__ == '__main__':
    for color in ("white", "black"):
        print(Balloon(color))
        print(Tank(color))
        print(PEKKA(color))
