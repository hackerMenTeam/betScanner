from application.findFork import find_forks
from application.model import *
import unittest
import time
import operator


class TestFindFork(unittest.TestCase):
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

        # Match(Bookmaker('1xbet', 'https://1xstavka.ru', True, False), 'match1', 'tennis', 'championship1', 1.125, 5.7),
        # Match(Bookmaker('marathonbet', 'https://marathonbet.ru', True, False), 'match1', 'tennis', 'championship1',
        #       1.24,
        #       3.92),
        # Match(Bookmaker('vulkan', 'https://vulkan.ru', True, False), 'match1', 'tennis', 'championship1', 1.127, 5.3),
        # Match(Bookmaker('ggbet', 'https://ggbet.ru', True, False), 'match1', 'tennis', 'championship1', 4, 8.9),
        # Match(Bookmaker('azino', 'https://azino.ru', True, False), 'match1', 'tennis', 'championship1', 1.125, 1.5)]

    # all_forks = [Fork(Match(Bookmaker('marathonbet', 'https://marathonbet.ru', True, False), 'match1', 'tennis',
    #                         'championship1', 1.24, 3.92), Match(Bookmaker('1xbet', 'https://1xstavka.ru', True, False),
    #                                                             'match1', 'tennis', 'championship1', 1.125, 5.7),
    #                   time.time()),
    #              Fork(Match(Bookmaker('ggbet', 'https://ggbet.ru', True, False), 'match1', 'tennis', 'championship1', 4,
    #                         8.9),
    #                   Match(Bookmaker('1xbet', 'https://1xstavka.ru', True, False), 'match1', 'tennis', 'championship1',
    #                         1.125, 5.7), time.time()),
    #              Fork(Match(Bookmaker('marathonbet', 'https://marathonbet.ru', True, False), 'match1', 'tennis',
    #                         'championship1', 1.24, 3.92),
    #                   Match(Bookmaker('vulkan', 'https://vulkan.ru', True, False), 'match1', 'tennis', 'championship1',
    #                         1.127, 5.3), time.time()),
    #              Fork(Match(Bookmaker('ggbet', 'https://ggbet.ru', True, False), 'match1', 'tennis', 'championship1', 4,
    #                         8.9),
    #                   Match(Bookmaker('marathonbet', 'https://marathonbet.ru', True, False), 'match1', 'tennis',
    #                         'championship1', 1.24, 3.92), time.time()),
    #              Fork(Match(Bookmaker('marathonbet', 'https://marathonbet.ru', True, False), 'match1', 'tennis',
    #                         'championship1', 1.24, 3.92),
    #                   Match(Bookmaker('ggbet', 'https://ggbet.ru', True, False), 'match1', 'tennis', 'championship1', 4,
    #                         8.9), time.time()),
    #              Fork(Match(Bookmaker('vulkan', 'https://vulkan.ru', True, False), 'match1', 'tennis', 'championship1',
    #                         1.127, 5.3),
    #                   Match(Bookmaker('ggbet', 'https://ggbet.ru', True, False), 'match1', 'tennis', 'championship1', 4,
    #                         8.9), time.time()),
    #              Fork(Match(Bookmaker('azino', 'https://azino.ru', True, False), 'match1', 'tennis', 'championship1',
    #                         1.125, 1.5),
    #                   Match(Bookmaker('ggbet', 'https://ggbet.ru', True, False), 'match1', 'tennis', 'championship1', 4,
    #                         8.9), time.time()),
    #              Fork(Match(Bookmaker('marathonbet', 'https://marathonbet.ru', True, False), 'match1', 'tennis',
    #                         'championship1', 1.24, 3.92),
    #                   Match(Bookmaker('ggbet', 'https://ggbet.ru', True, False), 'match1', 'tennis', 'championship1', 4,
    #                         8.9), time.time())
    #              ]

    def test_find_all_forks(self):
        # print(sorted(self.all_forks))
        find_forks(self.bets)
        #self.assertEqual(sorted(find_forks(self.bets)), sorted(self.all_forks))
