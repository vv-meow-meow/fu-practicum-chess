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
        moves = []
        col = pos[0]
        row = int(pos[1]) - 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dcol, drow in directions:
            i = 0
            while True:
                new_col = ord(col) + dcol * i
                new_row = row + drow * i
                if new_col < ord('a') or new_col > ord('h') or new_row < 0 or new_row > 7:
                    break
                moves.append(f"{chr(new_col)}{new_row + 1}")
                i += 1
        return moves

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
        moves = []
        col = pos[0]
        row = int(pos[1]) - 1
        knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                        (1, 2), (1, -2), (-1, 2), (-1, -2)]
        for dcol, drow in knight_moves:
            new_col = ord(col) + dcol
            new_row = row + drow
            if new_col >= ord('a') and new_col <= ord('h') and new_row >= 0 and new_row <= 7:
                moves.append(f"{chr(new_col)}{new_row + 1}")
        return moves

    def get_available_moves(self, pos: str, board: GameField) -> list:
        moves = self._get_moves(pos)
        result = []
        for move in moves:
            figure = board.get_figure(move)
            if figure is None:
                result.append(move)
        return result


class Bishop(Figure):
    def __str__(self):
        return "♗" if self.color == "white" else "♝"

    def _get_moves(self, pos: str) -> list:
        moves = []
        col = pos[0]
        row = int(pos[1]) - 1
        directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dcol, drow in directions:
            i = 0
            while True:
                new_col = ord(col) + dcol * i
                new_row = row + drow * i
                if new_col < ord('a') or new_col > ord('h') or new_row < 0 or new_row > 7:
                    break
                moves.append(f"{chr(new_col)}{new_row + 1}")
                i += 1
        return moves

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
        moves = []
        col = pos[0]
        row = int(pos[1]) - 1
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (-1, -1), (1, -1), (-1, 1)
        ]
        for dcol, drow in directions:
            i = 0
            while True:
                new_col = ord(col) + dcol * i
                new_row = row + drow * i
                if new_col < ord('a') or new_col > ord('h') or new_row < 0 or new_row > 7:
                    break
                moves.append(f"{chr(new_col)}{new_row + 1}")
                i += 1
        return moves

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
        moves = []
        col = pos[0]
        row = int(pos[1]) - 1
        directions = [
            (0, 1), (0, -1), (1, 0), (1, 1),
            (1, -1), (-1, 0), (-1, 1), (-1, -1)
        ]
        for dcol, drow in directions:
            new_col = ord(col) + dcol
            new_row = row + drow
            if new_col < ord('a') or new_col > ord('h') or new_row < 0 or new_row > 7:
                continue
            moves.append(f"{chr(new_col)}{new_row + 1}")
        return moves

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
        file = pos[0]
        moves = []
        if self.color == "white":
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6
        next_row = row + direction
        if 0 <= next_row <= 7:
            moves.append(f"{file}{next_row + 1}")
            if row == start_row:
                next_row2 = row + 2 * direction
                if 0 <= next_row2 <= 7:
                    moves.append(f"{file}{next_row2 + 1}")
        return moves

    def get_available_moves(self, pos: str, board: GameField) -> list:
        moves = self._get_moves(pos)
        result = []
        for pos in moves:
            figure = board.get_figure(pos)
            if figure is None:
                result.append(pos)
        return result
