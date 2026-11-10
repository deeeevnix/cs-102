import unittest
from pathlib import Path

from src.lab3.sudoku import (
    check_solution,
    find_possible_values,
    generate_sudoku,
    read_sudoku,
    solve,
)


PUZZLE_PATH = (
    Path(__file__).resolve().parents[2] / "src" / "lab3" / "puzzle1.txt"
)


class SudokuTestCase(unittest.TestCase):
    def test_find_possible_values(self):
        grid = read_sudoku(PUZZLE_PATH)

        self.assertEqual(find_possible_values(grid, (0, 2)), {"1", "2", "4"})

    def test_solve_puzzle(self):
        grid = read_sudoku(PUZZLE_PATH)
        original = [row.copy() for row in grid]

        solution = solve(grid)

        self.assertIsNotNone(solution)
        self.assertTrue(check_solution(solution))
        self.assertEqual(solution[0], list("534678912"))

        for row_index in range(9):
            for col_index in range(9):
                clue = original[row_index][col_index]
                if clue != ".":
                    self.assertEqual(solution[row_index][col_index], clue)

    def test_solve_returns_none_when_no_move_is_possible(self):
        grid = [["."] * 9 for row_index in range(9)]
        grid[0] = list("12345678.")
        grid[1][8] = "9"

        self.assertIsNone(solve(grid))

    def test_check_solution_rejects_duplicate(self):
        grid = read_sudoku(PUZZLE_PATH)
        solution = solve(grid)
        self.assertIsNotNone(solution)

        solution[0][0] = solution[0][1]

        self.assertFalse(check_solution(solution))

    def test_generate_sudoku_keeps_requested_number_of_clues(self):
        grid = generate_sudoku(40)
        filled_count = 0

        for row in grid:
            for cell in row:
                if cell != ".":
                    filled_count += 1

        self.assertEqual(filled_count, 40)
        self.assertTrue(check_solution(solve(grid)))