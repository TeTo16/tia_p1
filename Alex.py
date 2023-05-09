class Arm:
    def _init_(self, num):
        self.ID = "BRC" + num
        self.block = []

    def add_block(self, block):
        self.blocks.append(block)

    def remove_block(self):
        return self.blocks.pop()


class Block:
    def _init_(self, num, weight):
        self.ID = "BLC" + num
        self.weight = weight


class State:
    def _init_(self, arms):
        self.arms = arms
        self.num_moves = 0
        self.cost = 0

    def is_final_state(self, perfect_combination_arms):
        return self.arms == perfect_combination_arms


class Move:
    def _init_(self, arm_from, arm_to):
        self.arm_from = arm_from
        self.arm_to = arm_to


def get_possible_moves(state):
    possible_moves = []
    for arm_from in state.arms:
        for arm_to in state.arms:
            if arm_from != arm_to:
                if len(arm_from.blocks) > 0:
                    if len(arm_to.blocks) == 0 or arm_to.blocks[-1].weight > arm_from.blocks[-1].weight:
                        possible_moves.append(Move(arm_from, arm_to))
    return possible_moves


def get_new_state(state, move):
    new_arms = []
    for arm in state.arms:
        new_arm = Arm(arm.name)
        for block in arm.blocks:
            if block != move.arm_from.blocks[-1]:
                new_arm.add_block(block)
        new_arms.append(new_arm)
        if arm == move.arm_from:
            new_arm.remove_block()
        elif arm == move.arm_to:
            new_arm.add_block(move.arm_from.blocks[-1])
    new_state = State(new_arms)
    new_state.num_moves = state.num_moves + 1
    new_state.cost = new_state.num_moves * move.arm_from.blocks[-1].weight * len(state.arms)
    return new_state


def print_state(state):
    print("Moves:", state.num_moves)
    print("Cost:", state.cost)
    for arm in state.arms:
        print(arm.name + ": ", end="")
        for block in arm.blocks:
            print(str(block.weight) + " ", end="")
        print()


def train_arms(initial_arms, goal_arms):
    initial_state = State(initial_arms)
    goal_state = State(goal_arms)
    frontier = [initial_state]
    explored = set()
    while frontier:
        state = frontier.pop(0)
        explored.add(state)
        if state.is_goal_state(goal_state.arms):
            print("Goal state found!")
            print_state(state)
            return
        for move in get_possible_moves(state):
            new_state = get_new_state(state, move)
            if new_state not in explored and new_state not in frontier:
                frontier.append(new_state)
    print("No solution found.")