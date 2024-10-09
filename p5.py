import sys, parse, grader
from heapq import heappush, heappop


def astar_search(problem):
    start_state = problem['start_state']
    goal_states = problem['goal_states']
    heuristic_dic = problem['heuristic_dic']
    cost_dic = problem['cost_dic']

    frontier = []
    heappush(frontier, (heuristic_dic[start_state], start_state))
    # print('Initial Frontier:', list(frontier))
    explored = set()
    # set does not maintain order, use another var to save the exploration order
    explored_in_order = []
    solution_path = ''
    while frontier:
        # frontier ex. [(1, 'Ar B')]
        # We can't simply use node[1][-1] as node may consist of more than one letter. ex. Ar
        # heapq min-heap by default, which means the smallest element is always at the front
        element = heappop(frontier)
        cost = element[0]
        # the var nodes is a string contains the path separated by blank ex. Ar B C
        nodes = element[1]
        node = nodes.split()[-1]
        if node in goal_states:
            solution_path = nodes
            break
        if node not in explored:
            # print('Exploring:', node, '...', 'at cost', cost)
            explored.add(node)
            explored_in_order.append(node)
            # skip when the dic does not contain the node otherwise it will be an error
            if node not in cost_dic:
                continue
            for child in cost_dic[node]:
                # A* backward cost + forward cost
                # the path(nodes) appends a new node
                heappush(frontier,
                         (cost + child[0] - heuristic_dic[node] + heuristic_dic[child[1]], nodes + ' ' + child[1]))
            # print(list(frontier))
            # print(explored)
            # input()
    solution = ' '.join(explored_in_order) + '\n' + solution_path
    # print(solution)
    return solution


if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    problem_id = 5
    grader.grade(problem_id, test_case_id, astar_search, parse.read_graph_search_problem)
