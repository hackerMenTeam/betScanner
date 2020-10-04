from application.model import *
import time
import copy

bets = [
    [Bet(Match('match1', 'tennis', 'championship'), Bookmaker('1xbet', 'https://1xstavka.ru', True, False), 'win_1',
         1.125),
     Bet(Match('match1', 'tennis', 'championship'), Bookmaker('1xbet', 'https://1xstavka.ru', True, False),
         'win_2', 5.7)],
    [Bet(Match('match1', 'tennis', 'championship'), Bookmaker('marathonbet', 'https://marathonbet.ru', True, False),
         'win_1', 1.24),
     Bet(Match('match1', 'tennis', 'championship'), Bookmaker('marathonbet', 'https://marathonbet.ru', True, False),
         'win_2', 3.92)],
    [Bet(Match('match1', 'tennis', 'championship'), Bookmaker('vulkan', 'https://vulkan.ru', True, False),
         'win_1', 1.127),
     Bet(Match('match1', 'tennis', 'championship'), Bookmaker('vulkan', 'https://vulkan.ru', True, False),
         'win_2', 5.3)],
    [Bet(Match('match1', 'tennis', 'championship'), Bookmaker('ggbet', 'https://ggbet.ru', True, False),
         'win_1', 4),
     Bet(Match('match1', 'tennis', 'championship'), Bookmaker('ggbet', 'https://ggbet.ru', True, False),
         'win_2', 8.9)],
    [Bet(Match('match1', 'tennis', 'championship'), Bookmaker('azino', 'https://azino.ru', True, False),
         'win_1', 1.125),
     Bet(Match('match1', 'tennis', 'championship'), Bookmaker('azino', 'https://azino.ru', True, False),
         'win_2', 1.5)]]


def find_forks(bets):
    matches = copy.copy(bets)
    return flat_list(list(filter(lambda x: len(x) > 0, map(lambda bets: find_forks_for_bet(matches, bets), bets))))


def find_forks_for_bet(matches, current_match):
    fork = []
    for current_match_coef in current_match:
        for match in matches:
            for coef3 in matches:
                if len(coef3)==3:
                    print(1/current_match[0].coef+1/match[1]+1/coef3[3].coef)
                else:
                    break
            print(1 / current_match_coef.coef + 1 / match[1].coef)



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
