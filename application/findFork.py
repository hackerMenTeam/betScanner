from application.model import *
import time


def sort_fork(bet_list):
    for i in bet_list:
        if i.exodus == 'win_1':
            first = i
        elif i.exodus == 'win_2':
            second = i
        else:
            third = i
    return [first, second, third]


def find_forks(bets):
    forks = []
    for first_bet in bets:
        for second_bet in bets:
            if len(first_bet) < 3:
                if first_bet[0].bookmaker != second_bet[1].bookmaker:
                    if 1 / first_bet[0].coef + 1 / second_bet[1].coef < 1:
                        forks.append(Fork([first_bet[0], second_bet[1]], time.time()))
            else:
                for third_bet in bets:
                    if not(first_bet[0].bookmaker == second_bet[1].bookmaker == third_bet[2].bookmaker):
                        if 1 / first_bet[0].coef + 1 / second_bet[1].coef + 1 / third_bet[2].coef < 1:
                            forks.append(Fork(sort_fork([first_bet[0], second_bet[1], third_bet[2]]), time.time()))
    return flat_list(forks)


def flat_list(array, new_list=None):
    if new_list is None:
        new_list = []
    for i in array:
        if type(i) != list:
            new_list.append(i)
        else:
            flat_list(i, new_list)
    return new_list
