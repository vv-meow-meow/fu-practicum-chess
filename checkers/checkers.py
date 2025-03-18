from __future__ import annotations
from typing import Literal, TYPE_CHECKING

from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from field import GameField


class Figure(ABC):
    def __init__(self, color: Literal["black", "white"]):
        """Initialize a Figure with a specified color.

        Args:
            color (Literal["black", "white"]): The color of the figure.
        """
        self.color: Literal["black", "white"] = color

    @abstractmethod
    def _get_moves(self, pos: str) -> list:
        """Return a list of basic moves for a figure from a given position.

        This method should not be used directly. Use get_available_moves for move validation.

        Args:
            pos (str): The current position in algebraic notation (e.g., 'a1').

        Returns:
            list: A list (or nested list for sliding pieces) of potential moves.
        """
        pass

    @abstractmethod
    def get_available_moves(self, pos: str, board: GameField) -> list:
        """Return a list of available moves for a figure from a given position.

        The method calculates legal moves based on basic moves and checks for possible captures.

        Args:
            pos (str): The current position in algebraic notation (e.g., 'a1').
            board (GameField): The game board containing the positions of all figures.

        Returns:
            list: A list of legal moves for the figure.
        """
        pass


class King(Figure):
    def __str__(self):
        return "KW" if self.color == "white" else "KB"

    def _get_moves(self, pos: str) -> list:
        col = ord(pos[0])
        row = int(pos[1])
        possible_moves = (
            f"{chr(col - 1)}{row + 1}",
            f"{chr(col + 1)}{row + 1}",
            f"{chr(col - 1)}{row - 1}",
            f"{chr(col + 1)}{row - 1}"
        )
        result = []
        for move in possible_moves:
            if "a" <= move[0] <= "h" and 1 <= int(move[1]) <= 8:
                result.append(move)
        return result

    def get_available_moves(self, pos: str, board: GameField) -> list:
        pos = pos.lower()
        pos_col = ord(pos[0])
        pos_row = int(pos[1])
        moves = self._get_moves(pos)

        result = []
        for move in moves:
            figure = board.get_figure(move)
            if figure is None:
                result.append(move)
                continue
            else:
                if figure.color != self.color:
                    move_col = ord(move[0])
                    move_row = int(move[1])
                    col_dir = move_col - pos_col
                    row_dir = move_row - pos_row
                    future_pos = f"{chr(move_col + col_dir)}{move_row + row_dir}"
                    future_move_figure = board.get_figure(future_pos)
                    if future_move_figure is None:
                        result.append(future_pos)
        print(f"Available moves: {result}")
        return result


class Man(Figure):
    def __str__(self):
        return "⚪" if self.color == "white" else "⚫"

    def _get_moves(self, pos: str) -> list:
        col = ord(pos[0])
        row = int(pos[1])
        if self.color == "white":
            possible_moves = (
                f"{chr(col - 1)}{row + 1}",
                f"{chr(col + 1)}{row + 1}"
            )
        else:
            possible_moves = (
                f"{chr(col - 1)}{row - 1}",
                f"{chr(col + 1)}{row - 1}"
            )
        result = []
        for move in possible_moves:
            if "a" <= move[0] <= "h" and 1 <= int(move[1]) <= 8:
                result.append(move)
        return result

    def get_available_moves(self, pos: str, board: GameField) -> list:
        pos = pos.lower()
        pos_col = ord(pos[0])
        pos_row = int(pos[1])
        moves = self._get_moves(pos)

        result = []
        for move in moves:
            figure = board.get_figure(move)
            if figure is None:
                result.append(move)
                continue
            else:
                if figure.color != self.color:
                    move_col = ord(move[0])
                    move_row = int(move[1])
                    col_dir = move_col - pos_col
                    row_dir = move_row - pos_row
                    future_pos = f"{chr(move_col + col_dir)}{move_row + row_dir}"
                    future_move_figure = board.get_figure(future_pos)
                    if future_move_figure is None:
                        result.append(future_pos)
        print(f"Available moves: {result}")
        return result
