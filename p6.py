import sys, parse, grader


def calculate_attacks_in_pos(queen_pos, row, col):
    # calculate the number of attacks for a single queen in one position
    attacks = 0
    # start from col+1 to make sure attacks are unique
    for i in range(col + 1, len(queen_pos)):
        # same row
        if queen_pos[i] == row:
            attacks += 1
        # same diagonal
        if abs(queen_pos[i] - row) == abs(i - col):
            attacks += 1
    return attacks


def calculate_attacks_matrix(problem):
    board_size = len(problem)
    sum_attacks_matrix = [[0] * board_size for _ in range(board_size)]

    for col in range(board_size):
        for row in range(board_size):
            # use the method list() to create a shallow copy so that it will change elements in list problem
            cur_pos = list(problem)
            cur_pos[col] = row
            # count attacks for current queen first
            sum_attack = calculate_attacks_in_pos(cur_pos, row, col)
            # sum the rest of queens' attacks, their positions are recorded in cur_pos
            for i in range(board_size):
                if i == col:
                    continue
                sum_attack += calculate_attacks_in_pos(cur_pos, cur_pos[i], i)
            sum_attacks_matrix[row][col] = sum_attack
    return sum_attacks_matrix


def number_of_attacks(problem):
    sum_attacks_matrix = calculate_attacks_matrix(problem)
    # f-string {num:2} means that num will be printed with a minimum width of 2 characters
    solution = '\n'.join(' '.join(f"{num:2}" for num in row) for row in sum_attacks_matrix)
    return solution


if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    problem_id = 6
    grader.grade(problem_id, test_case_id, number_of_attacks, parse.read_8queens_search_problem)
