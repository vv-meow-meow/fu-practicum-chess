from __future__ import annotations
from typing import Literal, TYPE_CHECKING

from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from field import GameField


class Figure(ABC):
    def __init__(self, color: Literal["black", "white"]):
        self.color: Literal["black", "white"] = color

    @abstractmethod
    def _get_moves(self, pos: str) -> list:
        pass

    @abstractmethod
    def get_available_moves(self, pos: str, board: GameField) -> list:
        """Abstract method to get available moves for a figure

        It also checks if it can beat another figure
        """
        pass


class Rook(Figure):
    def __str__(self):
        return "♖" if self.color == "white" else "♜"

    def _get_moves(self, pos: str) -> list[list[str]]:
        moves = []
        col = pos[0]
        row = int(pos[1]) - 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dcol, drow in directions:
            moves_vector = []
            i = 1
            while True:
                new_col = ord(col) + dcol * i
                new_row = row + drow * i
                if new_col < ord('a') or new_col > ord('h') or new_row < 0 or new_row > 7:
                    break
                moves_vector.append(f"{chr(new_col)}{new_row + 1}")
                i += 1
            moves.append(moves_vector)
        return moves

    def get_available_moves(self, pos: str, board: GameField) -> list:
        moves = self._get_moves(pos)
        result = []
        for vector in moves:
            for move in vector:
                figure = board.get_figure(move)
                if figure is None:
                    result.append(move)
                    continue
                elif figure.color != self.color:
                    result.append(move)
                    break
                else:
                    break
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
            if ord('a') <= new_col <= ord('h') and 0 <= new_row <= 7:
                moves.append(f"{chr(new_col)}{new_row + 1}")
        return moves

    def get_available_moves(self, pos: str, board: GameField) -> list:
        moves = self._get_moves(pos)
        result = []
        for move in moves:
            figure = board.get_figure(move)
            if figure is None or figure.color != self.color:
                result.append(move)
        return result


class Bishop(Figure):
    def __str__(self):
        return "♗" if self.color == "white" else "♝"

    def _get_moves(self, pos: str) -> list[list[str]]:
        moves = []
        col = pos[0]
        row = int(pos[1]) - 1
        directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dcol, drow in directions:
            moves_vector = []
            i = 1
            while True:
                new_col = ord(col) + dcol * i
                new_row = row + drow * i
                if new_col < ord('a') or new_col > ord('h') or new_row < 0 or new_row > 7:
                    break
                moves_vector.append(f"{chr(new_col)}{new_row + 1}")
                i += 1
            moves.append(moves_vector)
        return moves

    def get_available_moves(self, pos: str, board: GameField) -> list:
        moves = self._get_moves(pos)
        result = []
        for vector in moves:
            for move in vector:
                figure = board.get_figure(move)
                if figure is None:
                    result.append(move)
                    continue
                elif figure.color != self.color:
                    result.append(move)
                    break
                else:
                    break
        return result


class Queen(Figure):
    def __str__(self):
        return "♕" if self.color == "white" else "♛"

    def _get_moves(self, pos: str) -> list[list[str]]:
        moves = []
        col = pos[0]
        row = int(pos[1]) - 1
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (-1, -1), (1, -1), (-1, 1)
        ]
        for dcol, drow in directions:
            moves_vector = []
            i = 1
            while True:
                new_col = ord(col) + dcol * i
                new_row = row + drow * i
                if new_col < ord('a') or new_col > ord('h') or new_row < 0 or new_row > 7:
                    break
                moves_vector.append(f"{chr(new_col)}{new_row + 1}")
                i += 1
            moves.append(moves_vector)
        return moves

    def get_available_moves(self, pos: str, board: GameField) -> list:
        moves = self._get_moves(pos)
        result = []
        for vector in moves:
            for move in vector:
                figure = board.get_figure(move)
                if figure is None:
                    result.append(move)
                    continue
                elif figure.color != self.color:
                    result.append(move)
                    break
                else:
                    break
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
        for move in moves:
            figure = board.get_figure(move)
            if figure is None:
                result.append(move)
            elif figure.color != self.color:
                result.append(move)
        return result


class Pawn(Figure):
    def __str__(self):
        return "♙" if self.color == "white" else "♟"

    def _get_moves(self, pos: str) -> list:
        row = int(pos[1]) - 1
        col = pos[0].lower()
        moves = []
        if self.color == "white":
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6
        next_row = row + direction
        if 0 <= next_row <= 7:
            moves.append(f"{col}{next_row + 1}")
            if row == start_row:
                next_row2 = row + 2 * direction
                if 0 <= next_row2 <= 7:
                    moves.append(f"{col}{next_row2 + 1}")
        return moves

    def get_available_moves(self, pos: str, board: GameField) -> list:
        moves = self._get_moves(pos)
        result = []
        for i in range(len(moves)):
            move = moves[i]
            move_col = move[0]
            move_row = move[1]
            if i == 0:
                diag_moves = []
                for num in (-1, 1):
                    if "a" <= chr(ord(move_col) + num) <= "h":
                        diag_moves.append(f"{chr(ord(move_col) + num)}{move_row}")

                figure = board.get_figure(move)
                if figure is None:
                    result.append(move)

                for diag_move in diag_moves:
                    figure = board.get_figure(diag_move)
                    if figure is None:
                        continue
                    elif figure.color != self.color:
                        result.append(diag_move)
            if i == 1:
                figure = board.get_figure(move)
                if figure is None:
                    result.append(move)

        return result
