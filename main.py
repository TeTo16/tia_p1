# This is a sample Python script.
from Block import Block
from HanoiTowerRobotic import HanoiTowerRobotic
from rbfs import recursive_best_first_search
from WorkSpace import WorkSpace

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

initial_state = [1, 3, 5, 4, 2,
                 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print((2+2)%3)
    hanoi = HanoiTowerRobotic(initial=(1, 3, 5, 4, 2,
                                       0, 0, 0, 0, 0,
                                       0, 0, 0, 0, 0))
    recursive_best_first_search(hanoi)

    # print(recursive_best_first_search(initial_state))
