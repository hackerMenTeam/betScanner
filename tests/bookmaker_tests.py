from .testing_config import BaseTestConfig
from application.model import Bookmaker


class TestBookmakers(BaseTestConfig):
    marathoneBet = Bookmaker('Marathonebet', 'marathonebet.ru', True, False)
    _1xbet = Bookmaker('1xbet', '1xbet.ru', True, False)
    vulkan = Bookmaker('Vulkan', 'vulkan.ru', True, True)
    pinacle = Bookmaker('Pinacle', 'pinacle.ru', False, False)

    all_bookmakers = [marathoneBet, _1xbet, vulkan, pinacle]
    enabled_bookmakers = [marathoneBet, _1xbet, vulkan]

    def test_list_all(self):
        self.given_bookmakers(self.all_bookmakers)
        self.assertEqual(Bookmaker.list_all(), self.all_bookmakers)

    def test_get_by_id(self):
        self.given_bookmakers(self.all_bookmakers)
        self.assertEqual(Bookmaker.get_by_id(2), self._1xbet)

    def test_list_enabled(self):
        self.given_bookmakers(self.all_bookmakers)
        criteria = Bookmaker.Criteria()
        criteria.is_enabled = True
        self.assertEqual(Bookmaker.list_by_criteria(criteria), self.enabled_bookmakers)

    def given_bookmakers(self, bookmakers):
        for bookmaker in bookmakers:
            self.given_bookmaker(bookmaker)

    def given_bookmaker(self, bookmaker):
        self.connect.execute("""INSERT INTO bookmakers 
                        (name, url, is_enabled, vpn_required) 
                        VALUES ('{name}', '{url}', {is_enabled}, {vpn_required})"""
                             .format(name=bookmaker.name, url=bookmaker.url, is_enabled=bookmaker.is_enabled,
                                     vpn_required=bookmaker.vpn_required))
