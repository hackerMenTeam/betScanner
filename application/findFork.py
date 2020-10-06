from application.model import *
import time
import copy

bets = [
    [Bet(Match('match1', 'tennis', 'championship'), Bookmaker('1xbet', 'https://1xstavka.ru', True, False), 'win_1',
         2.5),
     Bet(Match('match1', 'tennis', 'championship'), Bookmaker('1xbet', 'https://1xstavka.ru', True, False),
         'win_2', 1.3),
     Bet(Match('match1', 'tennis', 'championship'), Bookmaker('1xbet', 'https://1xstavka.ru', True, False),
         'draw', 5.7)],
    [Bet(Match('match1', 'tennis', 'championship'), Bookmaker('marathonbet', 'https://marathonbet.ru', True, False),
         'win_1', 2.9),
     Bet(Match('match1', 'tennis', 'championship'), Bookmaker('marathonbet', 'https://marathonbet.ru', True, False),
         'win_2', 2.7),
     Bet(Match('match1', 'tennis', 'championship'), Bookmaker('marathonbet', 'https://marathonbet.ru', True, False),
         'draw', 3.3)],
    [Bet(Match('match1', 'tennis', 'championship'), Bookmaker('vulkan', 'https://vulkan.ru', True, False),
         'win_1', 2.6),
     Bet(Match('match1', 'tennis', 'championship'), Bookmaker('vulkan', 'https://vulkan.ru', True, False),
         'win_2', 2.5),
     Bet(Match('match1', 'tennis', 'championship'), Bookmaker('vulkan', 'https://vulkan.ru', True, False),
         'draw', 3.9)]]


def sort_fork(list):
    for i in list:
        if i.exodus=='win_1':
            first=i
        elif i.exodus=='win_2':
            second=i
        else:
            third=i
    return [first,second,third]

def find_forks(bets):
    a = []
    for current_match in bets:
        round = 0
        fork = []
        for i in range(3):
            if round == 0:
                coef_1 = 0
                coef_2 = 1
                coef_3 = 2
            elif (round == 2):
                coef_1 = 1
                coef_2 = 2
                coef_3 = 0
            else:
                coef_1 = 2
                coef_2 = 0
                coef_3 = 1
            for second_bet in bets:
                if len(current_match) < 3:
                    if current_match[coef_1].bookmaker != second_bet[coef_2].bookmaker:
                        if (1 / current_match[coef_1].coef + 1 / second_bet[coef_2].coef < 1):
                            fork.append(Fork([current_match[coef_1], second_bet[coef_2]], time.time()))
                else:
                    for third_bet in bets:
                        if (current_match[coef_1].bookmaker != second_bet[coef_2].bookmaker != third_bet[
                            coef_3].bookmaker):
                            if (1 / current_match[coef_1].coef + 1 / second_bet[coef_2].coef + 1 / third_bet[
                                coef_3].coef < 1):
                                fork.append(
                                    Fork(sort_fork([current_match[coef_1], second_bet[coef_2], third_bet[coef_3]]), time.time()))
            round += 1
            a.append(fork)
    a = flat_list(list(filter(lambda x: len(x) > 0, a)))
    print(len(a))
    print('a', a)
    res = []
    for i in a:
        if i not in res:
            res.append(i)
    print(len(res))
    for i in res:
        print(i)
    return fork
    # return flat_list(list(filter(lambda x: len(x) > 0, map(lambda bets: find_forks_for_bet(bets, bets), bets))))


def find_forks_for_bet(matches, current_match):
    print(matches)
    fork = []
    round = 0
    if round == 0:
        coef_1 = 0
        coef_2 = 1
        coef_3 = 2
    elif (round == 2):
        coef_1 = 1
        coef_2 = 2
        coef_3 = 0
    else:
        coef_1 = 2
        coef_2 = 0
        coef_3 = 1
    for second_bet in matches:
        if len(current_match) < 3:
            if current_match[coef_1].bookmaker != second_bet[coef_2].bookmaker:
                if (1 / current_match[coef_1].coef + 1 / second_bet[coef_2].coef < 1):
                    fork.append(Fork([current_match[coef_1], second_bet[coef_2]], time.time()))
        else:
            for third_bet in matches:
                if (current_match[coef_1].bookmaker != second_bet[coef_2].bookmaker != third_bet[coef_3].bookmaker):
                    if (1 / current_match[coef_1].coef + 1 / second_bet[coef_2].coef + 1 / third_bet[coef_3].coef < 1):
                        fork.append(
                            Fork([current_match[coef_1], second_bet[coef_2], third_bet[coef_3].coef], time.time()))

    # for match in matches:
    #
    #     if 1 / current_match[0].coef + 1 / match[1].coef < 1:
    #         if current_match[0].coef < match[1].coef:
    #             fork.append(Fork(current_match[0], time.time()))
    #             fork.append(Fork(match[1],time.time()))
    #             print(fork,'a')
    #         else:
    #             fork.append(Fork(match[0], time.time()))
    #             fork.append(Fork(current_match[1], time.time()))
    #     if 1 / current_match[1].coef + 1 / match[0].coef < 1:
    #         if current_match[1].coef < match[0].coef:
    #             fork.append(Fork(current_match[1], time.time()))
    #             fork.append(Fork(match[0], time.time()))
    #         else:
    #             print(match[1])
    #             fork.append(Fork([match[1], current_match[0]], time.time()))
    #             fork.append(Fork(current_match[0], time.time()))
    return fork


def flat_list(array, new_list=None):
    if new_list is None:
        new_list = []
    for i in array:
        if type(i) != list:
            new_list.append(i)
        else:
            flat_list(i, new_list)
    return new_list


find_forks(bets)
