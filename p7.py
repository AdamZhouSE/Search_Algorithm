import sys, parse, grader
from p6 import calculate_attacks_matrix


def better_board(problem):
    attacks_matrix = calculate_attacks_matrix(problem)
    min_attacks = attacks_matrix[0][0]
    min_pos = [0, 0]
    for i in range(len(attacks_matrix)):
        for j in range(len(attacks_matrix[0])):
            if attacks_matrix[i][j] < min_attacks:
                min_attacks = attacks_matrix[i][j]
                min_pos = [i, j]
    problem[min_pos[1]] = min_pos[0]
    board = [['.'] * len(problem) for _ in range(len(problem))]
    for i in range(len(problem)):
        board[problem[i]][i] = 'q'
    solution = '\n'.join(' '.join(row) for row in board)
    return solution


if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    problem_id = 7
    grader.grade(problem_id, test_case_id, better_board, parse.read_8queens_search_problem)
