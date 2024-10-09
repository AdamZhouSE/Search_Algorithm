import sys, grader, parse
import collections


def bfs_search(problem):
    start_state = problem['start_state']
    goal_states = problem['goal_states']
    state_graph_dic = problem['state_graph_dic']

    frontier = collections.deque([start_state])
    # print('Initial Frontier:', list(frontier))
    explored = set()
    # set does not maintain order, use another var to save the exploration order
    explored_in_order = []
    solution_path = ''
    while frontier:
        # We can't simply use node[-1] as node may consist of more than one letter. ex. Ar
        # the var nodes is a string contains the path separated by blank ex. Ar B C
        # popleft() first in first out
        nodes = frontier.popleft()
        node = nodes.split()[-1]
        if node in goal_states:
            solution_path = nodes
            break
        if node not in explored:
            # print('Exploring:', node, '...')
            explored.add(node)
            explored_in_order.append(node)
            # skip when the dic does not contain the node otherwise it will be an error
            if node not in state_graph_dic:
                continue
            for child in state_graph_dic[node]:
                # the path(nodes) appends a new node
                frontier.append(nodes + ' ' + child)
            # print(list(frontier))
            # print(explored)
            # input()
    solution = ' '.join(explored_in_order) + '\n' + solution_path
    # print(solution)
    return solution


if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    problem_id = 2
    grader.grade(problem_id, test_case_id, bfs_search, parse.read_graph_search_problem)