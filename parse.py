import os, sys


def read_graph_search_problem(file_path):
    # read the problem file and handle data
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        start_state = lines[0].split()[1]
        goal_states = lines[1].split()[1:]
        heuristic_dic = {}
        state_graph_dic = {}
        cost_dic = {}
        for line in lines[2:]:
            elements = line.split()
            # ex. Ar 0
            if len(elements) == 2:
                heuristic_dic[elements[0]] = int(elements[1])
            # ex. Ar B 1.0
            else:
                if elements[0] not in state_graph_dic:
                    state_graph_dic[elements[0]] = []
                    cost_dic[elements[0]] = []
                state_graph_dic[elements[0]].append(elements[1])
                cost_dic[elements[0]].append((float(elements[2]), elements[1]))
    problem = {'start_state': start_state,
               'goal_states': goal_states,
               'heuristic_dic': heuristic_dic,
               'state_graph_dic': state_graph_dic,
               'cost_dic': cost_dic}
    return problem


def read_8queens_search_problem(file_path):
    board = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            line = line.strip().replace(' ', '')
            board.append(list(line))
    problem = [0 for _ in range(8)]
    # use col as index and record the row of each queen, simplify the board
    for row in range(8):
        for col in range(8):
            if board[row][col] == 'q':
                problem[col] = row
    return problem


if __name__ == "__main__":
    if len(sys.argv) == 3:
        problem_id, test_case_id = sys.argv[1], sys.argv[2]
        if int(problem_id) <= 5:
            problem = read_graph_search_problem(os.path.join('test_cases', 'p' + problem_id, test_case_id + '.prob'))
        else:
            problem = read_8queens_search_problem(os.path.join('test_cases', 'p' + problem_id, test_case_id + '.prob'))
        print(problem)
    else:
        print('Error: I need exactly 2 arguments!')
