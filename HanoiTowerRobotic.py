from abstract_classes.Problem import Problem


def find_first_blocks(state):
    firsts_blocks = [None, None, None]

    for y in range(0, 3):
        for x in range(4, -1, -1):
            space = [state[(x + y * 5)], x+1]
            if space[0] != 0:
                firsts_blocks[y] = space
                break
    # Return a 3D matrix that first index is the columns and in the list
    # puts the first id_block and the position in the column
    return firsts_blocks


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
            if block_checking is not None and not(block_checking[1] <= 4 and block_checking[0] < block_to_move[0]):
                possible_actions.remove('1TO2')
            block_checking = firsts_blocks_in_columns[2]
            if block_checking is not None and not(block_checking[1] <= 4 and block_checking[0] < block_to_move[0]):
                possible_actions.remove('1TO3')

        block_to_move = firsts_blocks_in_columns[1]
        if block_to_move is None:
            actions_to_remove = {'2TO1', '2TO3'}
            possible_actions = [ele for ele in possible_actions if ele not in actions_to_remove]
        else:
            block_checking = firsts_blocks_in_columns[0]
            if block_checking is not None and not(block_checking[1] <= 4 and block_checking[0] < block_to_move[0]):
                possible_actions.remove('2TO1')
            block_checking = firsts_blocks_in_columns[2]
            if block_checking is not None and not(block_checking[1] <= 4 and block_checking[0] < block_to_move[0]):
                possible_actions.remove('2TO3')

        block_to_move = firsts_blocks_in_columns[2]
        if block_to_move is None:
            actions_to_remove = {'3TO2', '3TO1'}
            possible_actions = [ele for ele in possible_actions if ele not in actions_to_remove]
        else:
            block_checking = firsts_blocks_in_columns[0]
            if block_checking is not None and not(block_checking[1] <= 4 and block_checking[0] < block_to_move[0]):
                possible_actions.remove('3TO1')
            block_checking = firsts_blocks_in_columns[1]
            if block_checking is not None and not(block_checking[1] <= 4 and block_checking[0] < block_to_move[0]):
                possible_actions.remove('3TO2')

        print(possible_actions)
        return possible_actions

    def h(self, node):
        """ Return the heuristic value for a given state."""

        # Manhattan Heuristic Function

        return 0