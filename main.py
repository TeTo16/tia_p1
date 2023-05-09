# This is a sample Python script.
from HanoiTowerRobotic import HanoiTowerRobotic
from algorithms import breadth_first_graph_search, best_first_graph_search
from dfgs import depth_first_graph_search
from rbfs import recursive_best_first_search
from WorkSpace import WorkSpace

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

initial_state = [1, 3, 5, 4, 2,
                 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    hanoi = HanoiTowerRobotic(initial=(1, 3, 5, 4, 2,
                                       0, 0, 0, 0, 0,
                                       0, 0, 0, 0, 0))

    # node = depth_first_graph_search(hanoi)
    # print(*depth_first_graph_search(hanoi).path())
    print(*breadth_first_graph_search(hanoi).path())
    # print(*best_first_graph_search(hanoi, lambda node: node.path_cost, display=False).path())
