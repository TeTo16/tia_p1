class action:
    def __init__(self, pos_to_move, pos_moved_to, cost):
        self.pos_to_move = pos_to_move
        self.pos_moved_to = pos_moved_to
        self.cost = cost


    def __str__(self):
        return 'Initial pos: {}, final pos: {} with cost: {}'.format(self.pos_to_move, self.pos_moved_to, self.cost)