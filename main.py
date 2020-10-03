from application.app import app

app = app
from application import betScanner
scanner = betScanner.Scanner.get_scanner()
