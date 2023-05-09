from action import action
from Block import blocks

class WorkSpace:
    goal_state = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0,
                  1, 2, 3, 4, 5]
    num_of_instances = 0
    heuristic = None
    evaluation_function= None

    def __init__(self, state, parent, action, path_cost, movement_num):
        self.state = state
        self.parent = parent
        self.action = action
        self.movement_num = movement_num + 1

        if parent:
            self.path_cost = parent.path_cost + path_cost
        else:
            self.path_cost = path_cost

        self.generate_heuristic()
        self.evaluation_function = self.heuristic + self.path_cost
        WorkSpace.num_of_instances += 1

    def __str__(self):
        return str(self.state[0:5]) + '\n' + str(self.state[5:10]) + '\n' + str(self.state[10:15]) + '\n\n'


    def generate_heuristic(self):
        self.heuristic = 0
        for num in range(1, 6):
            distance = abs(self.state.index(num) - self.goal_state.index(num))
            i = int(distance / 3)
            j = int(distance % 5)
            self.heuristic =self.heuristic + i + j


    def goal(self):
        if self.state == self.goal_state:
            return True
        return False

    def find_legal_actions(self):
        firsts_blocks = self.find_first_blocks()
        legal_actions = []

        for i in range(0, 3):
            space_checking = firsts_blocks[i]
            if space_checking is not None:
                for j in range(1, 3):
                    space_to_check = firsts_blocks[(i+j)%3] # This is good
                    if space_to_check is not None:
                        if space_checking[0] > space_to_check[0] and space_to_check[1] < 5:
                            block = next((obj for obj in blocks if obj.id == space_checking[0]), None)
                            cost = self.movement_num * j * block.weight
                            legal_actions.append(action(self.state.index(space_checking[0]), self.state.index(space_to_check[0])+1, cost))
                    else:
                        block = next((obj for obj in blocks if obj.id == space_checking[0]), None)
                        cost = self.movement_num * j * block.weight
                        legal_actions.append(action(self.state.index(space_checking[0]), (i+j)%3*5, cost))
        return legal_actions

    def find_first_blocks(self):
        firsts_blocks = [None, None, None]

        for y in range(0, 3):
            for x in range(4, -1, -1):
                space = [self.state[(x + y * 5)], x+1]
                if space[0] != 0:
                    firsts_blocks[y] = space
                    break
        # Return a 3D matrix that first index is the columns and in the list
        # puts the first id_block and the position in the column
        return firsts_blocks

    def generate_child(self):
        children = []
        legal_actions = self.find_legal_actions()

        for action in legal_actions:
            new_state = self.state.copy()
            new_state[action.pos_to_move], new_state[action.pos_moved_to] = new_state[action.pos_moved_to], new_state[action.pos_to_move]
            children.append(WorkSpace(new_state, self, action, action.cost, self.movement_num))
        return children


    def find_solution(self):
        solution = [self.action]
        path = self
        while path.parent != None:
            path = path.parent
            solution.append(path.action)
        solution = solution[:-1]
        solution.reverse()
        return solution