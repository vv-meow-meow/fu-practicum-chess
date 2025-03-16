from __future__ import annotations
from typing import Literal, TYPE_CHECKING

from abc import ABC

if TYPE_CHECKING:
    from field import GameField


class Figure(ABC):
    def __init__(self, color: Literal["black", "white"]):
        self.color: Literal["black", "white"] = color

    def _get_moves(self, pos: str) -> list:
        pass

    def get_available_moves(self, pos: str, board: GameField) -> list:
        """Abstract method to get available moves for a figure"""
        pass


class Rook(Figure):
    def __str__(self):
        return "♖" if self.color == "white" else "♜"

    def _get_moves(self, pos: str) -> list:
        result_moves = []
        col = pos[0]
        row = int(pos[1]) - 1
        # +1 0 >
        for i in range(8):
            new_col = ord(col) + i
            if new_col > ord('h') or new_col < ord('a'):
                continue
            result_moves.append(f"{chr(new_col)}{row + 1}")
        # -1 0 <
        for i in range(8):
            new_col = ord(col) - i
            if new_col > ord('h') or new_col < ord('a'):
                continue
            result_moves.append(f"{chr(new_col)}{row + 1}")
        # 0 +1 ^
        for i in range(8):
            new_row = row + i
            if new_row > 7 or new_row < 0:
                continue
            result_moves.append(f"{col}{new_row + 1}")
        # 0 -1 ⌄
        for i in range(8):
            new_row = row - i
            if new_row > 7 or new_row < 0:
                continue
            result_moves.append(f"{col}{new_row + 1}")

        return result_moves

    def get_available_moves(self, pos: str, board: GameField) -> list:
        moves = self._get_moves(pos)
        result = []
        for move in moves:
            figure = board.get_figure(move)
            if figure is None:
                result.append(move)
        return result


class Knight(Figure):
    def __str__(self):
        return "♘" if self.color == "white" else "♞"

    def _get_moves(self, pos: str) -> list:
        pass

    def get_available_moves(self, pos: str, board: GameField) -> list:
        pass


class Bishop(Figure):
    def __str__(self):
        return "♗" if self.color == "white" else "♝"

    def _get_moves(self, pos: str) -> list:
        result_moves = []
        col = pos[0]
        row = int(pos[1]) - 1
        # +1 +1
        for i in range(8):
            new_col = ord(col) + i
            new_row = row + i
            if (new_col > ord("h") or new_col < ord("a")
                    or new_row > 7 or new_row < 0):
                continue
            result_moves.append(f"{chr(new_col)}{new_row + 1}")

        # -1 -1
        for i in range(8):
            new_col = ord(col) - i
            new_row = row - i
            if (new_col > ord("h") or new_col < ord("a")
                    or new_row > 7 or new_row < 0):
                continue
            result_moves.append(f"{chr(new_col)}{new_row + 1}")

        # +1 -1
        for i in range(8):
            new_col = ord(col) + i
            new_row = row - i
            if (new_col > ord("h") or new_col < ord("a")
                    or new_row > 7 or new_row < 0):
                continue
            result_moves.append(f"{chr(new_col)}{new_row + 1}")

        # -1 +1
        for i in range(8):
            new_col = ord(col) - i
            new_row = row + i
            if (new_col > ord("h") or new_col < ord("a")
                    or new_row > 7 or new_row < 0):
                continue
            result_moves.append(f"{chr(new_col)}{new_row + 1}")

        return result_moves

    def get_available_moves(self, pos: str, board: GameField) -> list:
        moves = self._get_moves(pos)
        result = []
        for move in moves:
            figure = board.get_figure(move)
            if figure is None:
                result.append(move)
        return result


class Queen(Figure):
    def __str__(self):
        return "♕" if self.color == "white" else "♛"

    def _get_moves(self, pos: str) -> list:
        result_moves = []
        col = pos[0]
        row = int(pos[1]) - 1
        # +1 +1
        for i in range(8):
            new_col = ord(col) + i
            new_row = row + i
            if (new_col > ord("h") or new_col < ord("a")
                    or new_row > 7 or new_row < 0):
                continue
            result_moves.append(f"{chr(new_col)}{new_row + 1}")
        # -1 -1
        for i in range(8):
            new_col = ord(col) - i
            new_row = row - i
            if (new_col > ord("h") or new_col < ord("a")
                    or new_row > 7 or new_row < 0):
                continue
            result_moves.append(f"{chr(new_col)}{new_row + 1}")
        # +1 -1
        for i in range(8):
            new_col = ord(col) + i
            new_row = row - i
            if (new_col > ord("h") or new_col < ord("a")
                    or new_row > 7 or new_row < 0):
                continue
            result_moves.append(f"{chr(new_col)}{new_row + 1}")
        # -1 +1
        for i in range(8):
            new_col = ord(col) - i
            new_row = row + i
            if (new_col > ord("h") or new_col < ord("a")
                    or new_row > 7 or new_row < 0):
                continue
            result_moves.append(f"{chr(new_col)}{new_row + 1}")
        # +1 0 >
        for i in range(8):
            new_col = ord(col) + i
            if new_col > ord('h') or new_col < ord('a'):
                continue
            result_moves.append(f"{chr(new_col)}{row + 1}")
        # -1 0 <
        for i in range(8):
            new_col = ord(col) - i
            if new_col > ord('h') or new_col < ord('a'):
                continue
            result_moves.append(f"{chr(new_col)}{row + 1}")
        # 0 +1 ^
        for i in range(8):
            new_row = row + i
            if new_row > 7 or new_row < 0:
                continue
            result_moves.append(f"{col}{new_row + 1}")
        # 0 -1 ⌄
        for i in range(8):
            new_row = row - i
            if new_row > 7 or new_row < 0:
                continue
            result_moves.append(f"{col}{new_row + 1}")

        return result_moves

    def get_available_moves(self, pos: str, board: GameField) -> list:
        moves = self._get_moves(pos)
        result = []
        for pos in moves:
            figure = board.get_figure(pos)
            if figure is None:
                result.append(pos)
        return result


class King(Figure):
    def __str__(self):
        return "♔" if self.color == "white" else "♚"

    def _get_moves(self, pos: str) -> list:
        col = pos[0]
        row = int(pos[1]) - 1
        result_moves = []
        for col_i, row_i in ((0, 1), (0, -1),
                             (1, 0), (1, 1), (1, -1),
                             (-1, 0), (-1, +1), (-1, -1)):
            new_col = ord(col) + col_i
            new_row = row + row_i
            if new_col > ord('h') or new_col < ord('a') or new_row > 7 or new_row < 0:
                continue
            result_moves.append(f"{chr(new_col)}{row + 1}")

        return result_moves

    def get_available_moves(self, pos: str, board: GameField) -> list:
        moves = self._get_moves(pos)
        result = []
        for pos in moves:
            figure = board.get_figure(pos)
            if figure is None:
                result.append(pos)
        return result


class Pawn(Figure):
    def __str__(self):
        return "♙" if self.color == "white" else "♟"

    def _get_moves(self, pos: str) -> list:
        row = int(pos[1]) - 1
        if self.color == "white":
            if row == 1:
                return [f"{pos[0]}3", f"{pos[0]}4"]
            elif row < 7:
                return [f"{pos[0]}{row + 2}"]
        elif self.color == "black":
            if row == 6:
                return [f"{pos[0]}6", f"{pos[0]}5"]
            elif row > 0:
                return [f"{pos[0]}{row + 2}"]
        return []

    def get_available_moves(self, pos: str, board: GameField) -> list:
        moves = self._get_moves(pos)
        result = []
        for pos in moves:
            figure = board.get_figure(pos)
            if figure is None:
                result.append(pos)
        return result
