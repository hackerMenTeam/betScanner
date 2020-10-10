from application.findFork import find_forks
from application.model import *
import unittest
import time


class TestFindFork(unittest.TestCase):
    MATCH = Match('match1', 'tennis', 'championship')
    _1xbet = Bookmaker('1xbet', 'https://1xstavka.ru', True, False)
    marathonbet = Bookmaker('marathonbet', 'https://marathonbet.ru', True, False)
    vulkan = Bookmaker('vulkan', 'https://vulkan.ru', True, False)
    ggbet = Bookmaker('ggbet', 'https://ggbet.ru', True, False)
    azino = Bookmaker('azino', 'https://azino.ru', True, False)
    _1xbet_win_1 = Bet(MATCH, _1xbet, 'win_1', 2.5)
    _1xbet_win_2 = Bet(MATCH, _1xbet, 'win_2', 1.3)
    _1xbet_draw = Bet(MATCH, _1xbet, 'draw', 5.7)
    marathonbet_win_1 = Bet(MATCH, marathonbet, 'win_1', 2.9)
    marathonbet_win_2 = Bet(MATCH, marathonbet, 'win_2', 2.7)
    marathonbet_draw = Bet(MATCH, marathonbet, 'draw', 3.3)
    vulkan_win_1 = Bet(MATCH, vulkan, 'win_1', 2.6)
    vulkan_win_2 = Bet(MATCH, vulkan, 'win_2', 2.5)
    vulkan_draw = Bet(MATCH, vulkan, 'draw', 3.9)
    _1xbet_win_2_2_exoduses = Bet(MATCH, _1xbet, 'win_2', 5.7)
    marathonbet_win_1_2_exoduses = Bet(MATCH, marathonbet, 'win_1', 1.24)
    marathonbet_win_2_2_exoduses = Bet(MATCH, marathonbet, 'win_2', 3.92)
    vulkan_win_1_2_exoduses = Bet(MATCH, vulkan, 'win_1', 1.127)
    vulkan_win_2_2_exoduses = Bet(MATCH, vulkan, 'win_2', 5.3)
    ggbet_win_1_2_exoduses = Bet(MATCH, ggbet, 'win_1', 4)
    ggbet_win_2_2_exoduses = Bet(MATCH, ggbet, 'win_2', 8.9)
    azino_win_1_2_exoduses = Bet(MATCH, azino, 'win_1', 1.125)
    azino_win_2_2_exoduses = Bet(MATCH, azino, 'win_2', 1.5)
    
    bets_2_exoduses = [[Bet(MATCH, _1xbet, 'win_1', 1.125), _1xbet_win_2_2_exoduses],
                       [marathonbet_win_1_2_exoduses, marathonbet_win_2_2_exoduses],
                       [vulkan_win_1_2_exoduses, vulkan_win_2_2_exoduses],
                       [ggbet_win_1_2_exoduses, ggbet_win_2_2_exoduses],
                       [azino_win_1_2_exoduses, azino_win_2_2_exoduses]]

    bets_2_exoduses_no_forks = [[Bet(MATCH, _1xbet, 'win_1', 1.125), Bet(MATCH, _1xbet, 'win_2', 2.5)],
                                [marathonbet_win_1_2_exoduses, Bet(MATCH, marathonbet, 'win_2', 3.02)],
                                [vulkan_win_1_2_exoduses, Bet(MATCH, vulkan, 'win_2', 2.3)],
                                [Bet(MATCH, ggbet, 'win_1', 1.45), Bet(MATCH, ggbet, 'win_2', 2.9)],
                                [azino_win_1_2_exoduses, azino_win_2_2_exoduses]]

    bets_3_exoduses = [
        [_1xbet_win_1, _1xbet_win_2, _1xbet_draw], [marathonbet_win_1, marathonbet_win_2, marathonbet_draw],
        [vulkan_win_1, vulkan_win_2, vulkan_draw]]

    bets_3_exoduses_no_forks = [
        [_1xbet_win_1, _1xbet_win_2, Bet(MATCH, _1xbet, 'draw', 1.7)],
        [marathonbet_win_1, Bet(MATCH, marathonbet, 'win_2', 1.7), Bet(MATCH, marathonbet, 'draw', 2.3)],
        [vulkan_win_1, vulkan_win_2, Bet(MATCH, vulkan, 'draw', 1.9)]]

    expected_forks_with_2_exoduses = [
        Fork([ggbet_win_1_2_exoduses, _1xbet_win_2_2_exoduses], time.time()),
        Fork([marathonbet_win_1_2_exoduses, _1xbet_win_2_2_exoduses], time.time()),
        Fork([marathonbet_win_1_2_exoduses, vulkan_win_2_2_exoduses], time.time()),
        Fork([marathonbet_win_1_2_exoduses, ggbet_win_2_2_exoduses], time.time()),
        Fork([ggbet_win_1_2_exoduses, marathonbet_win_2_2_exoduses], time.time()),
        Fork([vulkan_win_1_2_exoduses, ggbet_win_2_2_exoduses], time.time()),
        Fork([ggbet_win_1_2_exoduses, azino_win_2_2_exoduses], time.time()),
        Fork([ggbet_win_1_2_exoduses, vulkan_win_2_2_exoduses], time.time())]

    expected_forks_with_3_exoduses = [
        Fork([_1xbet_win_1, vulkan_win_2, _1xbet_draw], time.time()),
        Fork([_1xbet_win_1, marathonbet_win_2, _1xbet_draw], time.time()),
        Fork([marathonbet_win_1, marathonbet_win_2, _1xbet_draw], time.time()),
        Fork([marathonbet_win_1, marathonbet_win_2, vulkan_draw], time.time()),
        Fork([marathonbet_win_1, vulkan_win_2, _1xbet_draw], time.time()),
        Fork([vulkan_win_1, marathonbet_win_2, _1xbet_draw], time.time()),
        Fork([vulkan_win_1, vulkan_win_2, _1xbet_draw], time.time())]

    def test_find_all_forks_3_exoduses(self):
        self.assertEqual(sorted(find_forks(self.bets_3_exoduses)), sorted(self.expected_forks_with_3_exoduses))

    def test_find_all_forks_2_exoduses(self):
        self.assertEqual(sorted(find_forks(self.bets_2_exoduses)), sorted(self.expected_forks_with_2_exoduses))

    def test_find_all_forks_no_forks_2_exoduses(self):
        self.assertEqual(sorted(find_forks(self.bets_2_exoduses_no_forks)), [])

    def test_find_all_forks_no_forks_3_exoduses(self):
        self.assertEqual(sorted(find_forks(self.bets_3_exoduses_no_forks)), [])
