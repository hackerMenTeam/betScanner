import copy
from application.findFork import find_forks
from model import Bet, Fork, Bookmaker
import unittest
import time
from flask_testing import TestCase
from .testing_config import BaseTestConfig


class TestFindFork(BaseTestConfig):
    bets = [
        Bet(Bookmaker('1xbet', 'https://1xstavka.ru', True, False), 'match1', 'tennis', 'championship1', 1.125, 5.7),
        Bet(Bookmaker('marathonbet', 'https://marathonbet.ru', True, False), 'match1', 'tennis', 'championship1', 1.24,
            3.92),
        Bet(Bookmaker('vulkan', 'https://vulkan.ru', True, False), 'match1', 'tennis', 'championship1', 1.127, 5.3),
        Bet(Bookmaker('ggbet', 'https://ggbet.ru', True, False), 'match1', 'tennis', 'championship1', 4, 8.9)]

    all_forks = [Fork(Bet(Bookmaker('marathonbet', 'https://marathonbet.ru', True, False), 'match1', 'tennis',
                          'championship1', 1.24, 3.92), Bet(Bookmaker('1xbet', 'https://1xstavka.ru', True, False),
                                                            'match1', 'tennis', 'championship1', 1.125, 5.7), time.time()),
                 Fork(Bet(Bookmaker('ggbet', 'https://ggbet.ru', True, False), 'match1', 'tennis', 'championship1', 4, 8.9),
                      Bet(Bookmaker('1xbet', 'https://1xstavka.ru', True, False), 'match1', 'tennis', 'championship1', 1.125, 5.7),time.time()),
                 Fork(Bet(Bookmaker('marathonbet', 'https://marathonbet.ru', True, False), 'match1', 'tennis', 'championship1', 1.24, 3.92),
                      Bet(Bookmaker('vulkan', 'https://vulkan.ru', True, False), 'match1', 'tennis', 'championship1', 1.127, 5.3),time.time()),
                 Fork(Bet(Bookmaker('ggbet', 'https://ggbet.ru', True, False), 'match1', 'tennis', 'championship1', 4, 8.9),
                      Bet(Bookmaker('marathonbet', 'https://marathonbet.ru', True, False), 'match1', 'tennis',
                          'championship1', 1.24,3.92),time.time()),
                 Fork(Bet(Bookmaker('marathonbet', 'https://marathonbet.ru', True, False), 'match1', 'tennis', 'championship1', 1.24, 3.92),
                      Bet(Bookmaker('ggbet', 'https://ggbet.ru', True, False), 'match1', 'tennis', 'championship1', 4, 8.9), time.time()),
                 Fork(Bet(Bookmaker('vulkan', 'https://vulkan.ru', True, False), 'match1', 'tennis', 'championship1', 1.127, 5.3),
                      Bet(Bookmaker('ggbet', 'https://ggbet.ru', True, False), 'match1', 'tennis', 'championship1', 4, 8.9), time.time()),
                 Fork(Bet(Bookmaker('ggbet', 'https://ggbet.ru', True, False), 'match1', 'tennis', 'championship1', 4, 8.9),
                      Bet(Bookmaker('vulkan', 'https://vulkan.ru', True, False), 'match1', 'tennis', 'championship1', 1.127, 5.3), time.time())]

    def test_find_all_forks(self):
        self.assertEqual(find_forks(self.bets), self.all_forks)

