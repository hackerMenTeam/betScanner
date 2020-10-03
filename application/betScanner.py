from application.ParsersFactory import create_pages


class Scanner:
    __instance = None

    def __init__(self):
        if Scanner.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Scanner.__instance = self
            self.pages = None

    @staticmethod
    def get_scanner():
        if Scanner.__instance is None:
            Scanner()
        return Scanner.__instance

    def open_pages(self):
        if self.pages is None:
            self.pages = create_pages()
        inactive_pages = list(filter(lambda page: not page.isRunning, self.pages))
        # TODO: run this asynchronously
        for page in inactive_pages:
            page.load_page()

    def scan(self):
        all_matches = []
        # TODO: run this asynchronously
        for page in self.pages:
            all_matches.extend(page.get_matches())
        return all_matches

    def shut_down(self):
        running_pages = list(filter(lambda page: page.isRunning, self.pages))
        for page in running_pages:
            page.shut_down()
