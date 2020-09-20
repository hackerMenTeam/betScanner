import psycopg2
import fire


class Cli(object):
    HOST = "localhost"
    PORT = 5432
    DATABASE = "bet_scanner"
    USER = "postgres"
    PASSWORD = "1234"

    def __init__(self):
        self.connect = psycopg2.connect(host=self.HOST, port=self.PORT, database=self.DATABASE, user=self.USER,
                                        password=self.PASSWORD)
        self.cursor = self.connect.cursor()

    def list_bookmakers(self):
        self.cursor.execute("""SELECT id, name, url, is_enabled, vpn_required FROM bookmakers""")
        query_results = self.cursor.fetchall()
        print(query_results)
        self.connect.close()

    def add_bookmaker(self, name, url, is_enabled, vpn_required):
        self.cursor.execute("""INSERT INTO bookmakers (name, url, is_enabled, vpn_required) VALUES ('{name}', '{url}', 
        {is_enabled}, {vpn_required})""".format(name=name, url=url, is_enabled=is_enabled, vpn_required=vpn_required))
        self.connect.commit()
        self.connect.close()


if __name__ == '__main__':
    fire.Fire(Cli)
