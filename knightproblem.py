import random


class Cell:
    def __init__(self, row, column, occupied=None):
        self.occupied = False
        self.row = row
        self.column = column

class Board:
    def __init__(self):

        self.board = [[Cell(row=0, column=0), Cell(row=0, column=1), Cell(row=0, column=2), Cell(row=0, column=3),
                       Cell(row=0, column=4), Cell(row=0, column=5), Cell(row=0, column=6), Cell(row=0, column=7)],
                      [Cell(row=1, column=0), Cell(row=1, column=1), Cell(row=1, column=2), Cell(row=1, column=3),
                       Cell(row=1, column=4), Cell(row=1, column=5), Cell(row=1, column=6), Cell(row=1, column=7)],
                      [Cell(row=2, column=0), Cell(row=2, column=1), Cell(row=2, column=2), Cell(row=2, column=3),
                       Cell(row=2, column=4), Cell(row=2, column=5), Cell(row=2, column=6), Cell(row=2, column=7)],
                      [Cell(row=3, column=0), Cell(row=3, column=1), Cell(row=3, column=2), Cell(row=3, column=3),
                       Cell(row=3, column=4), Cell(row=3, column=5), Cell(row=3, column=6), Cell(row=3, column=7)],
                      [Cell(row=4, column=0), Cell(row=4, column=1), Cell(row=4, column=2), Cell(row=4, column=3),
                       Cell(row=4, column=4), Cell(row=4, column=5), Cell(row=4, column=6), Cell(row=4, column=7)],
                      [Cell(row=5, column=0), Cell(row=5, column=1), Cell(row=5, column=2), Cell(row=5, column=3),
                       Cell(row=5, column=4), Cell(row=5, column=5), Cell(row=5, column=6), Cell(row=5, column=7)],
                      [Cell(row=6, column=0), Cell(row=6, column=1), Cell(row=6, column=2), Cell(row=6, column=3),
                       Cell(row=6, column=4), Cell(row=6, column=5), Cell(row=6, column=6), Cell(row=6, column=7)],
                      [Cell(row=7, column=0), Cell(row=7, column=1), Cell(row=7, column=2), Cell(row=7, column=3),
                       Cell(row=7, column=4), Cell(row=7, column=5), Cell(row=7, column=6), Cell(row=7, column=7)]
                      ]

    def show_board(self):
        space = " "
        enter = "\n"

        for i in range(8):
            for j in range(8):
                print(f"{self.board[i][j].occupied}, ({self.board[i][j].row},"
                      f" {self.board[i][j].column})", end=f"{enter if j == 7 else space}")

            if i == 7: print(" ")


    @staticmethod
    def show_board_static(matrix):
        space = " "
        enter = "\n"

        for i in range(8):
            for j in range(8):
                print(f"[{matrix[i][j].occupied} ({matrix[i][j].row + 1},"
                      f" {matrix[i][j].column + 1})]", end=f"{enter if j == 7 else space}")

            if i == 7: print(" ")

    def run_knight_algorithm(self):
        start_position = (7, 1)

        board = Board()

        start_cell = board.board[start_position[0]][start_position[1]]

        current_cell = start_cell

        move_counter = 0

        moves = []

        moves.append((start_cell.row, start_cell.column))

        final_cell = None

        while True:
            current_cell.occupied = True

            self.board[current_cell.row][current_cell.column].occupied = True

            current_cell, prev_cell = board.check_neighbours(current_cell=current_cell)

            if current_cell is None or Board.is_board_full(self.board) is True:
                final_cell = prev_cell
                break

            moves.append((current_cell.row, current_cell.column))

            move_counter += 1

        return move_counter, moves, final_cell

    def check_neighbours(self, current_cell: Cell):

        valid_cells = []
        cell_to_move = None

        prev_cell = current_cell

        upper_left_move = (current_cell.row + 2, current_cell.column - 1)
        upper_right_move = (current_cell.row + 2, current_cell.column + 1)
        left_up_move = (current_cell.row + 1, current_cell.column - 2)
        left_down_move = (current_cell.row - 1, current_cell.column - 2)
        right_up_move = (current_cell.row + 1, current_cell.column + 2)
        right_down_move = (current_cell.row - 1, current_cell.column + 2)
        down_left_move = (current_cell.row - 2, current_cell.column - 1)
        down_right_move = (current_cell.row - 2, current_cell.column + 1)

        moves = [upper_left_move, upper_right_move, left_up_move, left_down_move,
                 right_up_move, right_down_move, down_left_move, down_right_move]

        for move in moves:
            if -1 < move[0] < 8 and -1 < move[1] < 8 and self.board[move[0]][move[1]].occupied is False:
                valid_cells.append(self.board[move[0]][move[1]])

        if len(valid_cells) == 1:
            cell_to_move = valid_cells[0]
        elif len(valid_cells) != 1 and len(valid_cells) != 0:
            cell_to_move = Board.get_best_cell_from_valid_cells(self.board, valid_cells)
            #Board.get_best_cell_from_valid_cells(self.board, valid_cells)
            #random.choice(valid_cells)
        return cell_to_move, prev_cell

    @staticmethod
    def get_best_cell_from_valid_cells(board, cells: []) -> []:

        cell_possible_moves = []

        for cell in cells:

            moves = [(cell.row + 2, cell.column - 1), (cell.row + 2, cell.column + 1),
                     (cell.row + 1, cell.column - 2), (cell.row - 1, cell.column - 2),
                     (cell.row + 1, cell.column + 2), (cell.row - 1, cell.column + 2),
                     (cell.row - 2, cell.column - 1), (cell.row - 2, cell.column + 1)]

            possible_move = 0

            for move in moves:
                if -1 < move[0] < 8 and -1 < move[1] < 8 and board[move[0]][move[1]].occupied is False:
                    possible_move += 1

            cell_possible_moves.append(possible_move)

        index = cell_possible_moves.index(min(cell_possible_moves))

        return cells[index]

    @staticmethod
    def is_board_full(board):

        for i in range(8):
            for j in range(8):
                if board[i][j].occupied is False:
                    return False

        return True

    def clear_board(self):
        for i in range(8):
            for j in range(8):
                self.board[i][j].occupied = False


if __name__ == "__main__":

    tryes = []

    TRYES_NUMBER = 10

    for _ in range(TRYES_NUMBER):
        board = Board()
        move_counter, moves, final_cell = board.run_knight_algorithm()
        tryes.append((move_counter, moves, board.board, final_cell, Board.is_board_full(board.board)))

    move_counters = []

    moves_history_from_tryes = []

    complites = []

    for try_ in tryes:
        move_counters.append(try_[0])
        moves_history_from_tryes.append(try_[1])
        complites.append(try_[4])

    yes = 0
    no = 0

    for complete_task in complites:
        if complete_task == True:
            yes += 1
        else:
            no += 1

    print(f"COMPLETED = {yes}, NOT COMPLETED = {no}")

    for move in moves_history_from_tryes[0:1]:
        for tuple_move in move:
            print(f"[{tuple_move[0] + 1}, {tuple_move[1] + 1}]", end=" -> ")

        print("\n---")

    print("end.")

