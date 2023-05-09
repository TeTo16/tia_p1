from Block import blocks
from abstract_classes.Problem import Problem


class HanoiTowerRobotic(Problem):
    goal_state = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0,
                  1, 2, 3, 4, 5]

    def __init__(self, initial, goal=(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5)):
        """ Define goal state and initialize a problem """
        super().__init__(initial, goal)

    def actions(self, state):
        possible_actions = ['1TO2', '2TO1', '2TO3', '3TO2', '3TO1', '1TO3']
        firsts_blocks_in_columns = find_first_blocks(state)

        block_to_move = firsts_blocks_in_columns[0]
        if block_to_move is None:
            actions_to_remove = {'1TO2', '1TO3'}
            possible_actions = [ele for ele in possible_actions if ele not in actions_to_remove]
        else:
            block_checking = firsts_blocks_in_columns[1]
            if block_checking is not None and not (block_checking[1] <= 4 and block_checking[0] < block_to_move[0]):
                possible_actions.remove('1TO2')
            block_checking = firsts_blocks_in_columns[2]
            if block_checking is not None and not (block_checking[1] <= 4 and block_checking[0] < block_to_move[0]):
                possible_actions.remove('1TO3')

        block_to_move = firsts_blocks_in_columns[1]
        if block_to_move is None:
            actions_to_remove = {'2TO1', '2TO3'}
            possible_actions = [ele for ele in possible_actions if ele not in actions_to_remove]
        else:
            block_checking = firsts_blocks_in_columns[0]
            if block_checking is not None and not (block_checking[1] <= 4 and block_checking[0] < block_to_move[0]):
                possible_actions.remove('2TO1')
            block_checking = firsts_blocks_in_columns[2]
            if block_checking is not None and not (block_checking[1] <= 4 and block_checking[0] < block_to_move[0]):
                possible_actions.remove('2TO3')

        block_to_move = firsts_blocks_in_columns[2]
        if block_to_move is None:
            actions_to_remove = {'3TO2', '3TO1'}
            possible_actions = [ele for ele in possible_actions if ele not in actions_to_remove]
        else:
            block_checking = firsts_blocks_in_columns[0]
            if block_checking is not None and not (block_checking[1] <= 4 and block_checking[0] < block_to_move[0]):
                possible_actions.remove('3TO1')
            block_checking = firsts_blocks_in_columns[1]
            if block_checking is not None and not (block_checking[1] <= 4 and block_checking[0] < block_to_move[0]):
                possible_actions.remove('3TO2')

        return possible_actions

    def result(self, state, action):
        new_state = list(state)
        steps = action.split('TO')

        idx_to_move = return_first_index_by_column(new_state, steps[0])
        idx_move_to = return_free_index_by_column(new_state, steps[1])

        new_state[idx_to_move], new_state[idx_move_to] = new_state[idx_move_to], new_state[idx_to_move]
        return tuple(new_state)

    def path_cost(self, c, state1, action, state2, num_move):
        path_cost = c
        steps = action.split('TO')
        distance = abs(int(steps[0]) - int(steps[1]))

        idx_of_block = return_first_index_by_column(state1, steps[0])
        block = next((obj for obj in blocks if obj.id == state1[idx_of_block]), None)

        path_cost += distance * block.weight * num_move
        return path_cost

    def h(self, node):
        """ Return the heuristic value for a given state."""

        # Manhattan Heuristic Function

        return 0


def find_first_blocks(state):
    firsts_blocks = [None, None, None]

    for y in range(0, 3):
        for x in range(4, -1, -1):
            space = [state[(x + y * 5)], x + 1]
            if space[0] != 0:
                firsts_blocks[y] = space
                break
    # Return a 3D matrix that first index is the columns and in the list
    # puts the first id_block and the position in the column
    return firsts_blocks


def return_first_index_by_column(state, column):
    firsts_index = 0
    int_column = int(column) - 1
    for x in range(4, -1, -1):
        space = state[x + int_column * 5]
        if space != 0 or x == 0:
            firsts_index = x + int_column * 5
            break
    return firsts_index

def return_free_index_by_column(state, column):
    idx = 0
    int_column = int(column) - 1
    for x in range(0, 5):
        space = state[x + int_column * 5]
        if space == 0:
            idx = x + int_column * 5
            break
    return idx