from HanoiTowerRobotic import return_first_index_by_column


class Node:
    """A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state. Also includes the action that got us to this state, and
    the total path_cost (also known as g) to reach the node. Other functions
    may add an f and h value; see best_first_graph_search and astar_search for
    an explanation of how the f and h values are handled. You will not need to
    subclass this class."""

    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Create a search tree Node, derived from a parent by an action."""
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        strToReturn = ""
        if self.depth == 0:
            strToReturn += "Hanoi Tower with 4 Robots \nInitial State:\n"
        else:
            strToReturn += "\n"
        for x in range(4, -1, -1):
            for y in range(0, 3):
                if y == 1:
                    strToReturn += "  " + str(self.state[x + y * 5]) + "  "
                else:
                    strToReturn += "|  " + str(self.state[x + y * 5]) + "  |"
            strToReturn += "\n"
        if self.depth > 0:
            strToReturn += "Robot " + str(self.depth % 4 + 1) + " in movement number {}\n".format(self.depth)
            steps = self.action.split('TO')
            strToReturn += "moved block {} ".format(self.state[return_first_index_by_column(self.state, steps[1])])
            strToReturn += "from column {} to col {}.\n".format(steps[0], steps[1])
            strToReturn += "The accumulated cost is: {}\n".format(int(self.path_cost))
        return strToReturn

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        """List the nodes reachable in one step from this node."""
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        """[Figure 3.10]"""
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action,
                         problem.path_cost(self.path_cost, self.state, action, next_state, self.depth + 1))
        return next_node

    def solution(self):
        """Return the sequence of actions to go from the root to this node."""
        return [node.action for node in self.path()[1:]]

    def path(self):
        """Return a list of nodes forming the path from the root to this node."""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    # We want for a queue of nodes in breadth_first_graph_search or
    # astar_search to have no duplicated states, so we treat nodes
    # with the same state as equal. [Problem: this may not be what you
    # want in other contexts.]

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        # We use the hash value of the state
        # stored in the node instead of the node
        # object itself to quickly search a node
        # with the same state in a Hash Table
        return hash(self.state)
