import psycopg2
import fire


class Cli(object):

    def list_bookmakers(self):
        conn = psycopg2.connect(host="localhost", port=5432, database="bet_scanner", user="postgres", password="1234")
        cur = conn.cursor()
        cur.execute("""SELECT id, name, url, is_enabled, vpn_required FROM bookmakers""")
        query_results = cur.fetchall()
        print(query_results)

    def add_bookmaker(self, name, url, is_enabled, vpn_required):
        conn = psycopg2.connect(host="localhost", port=5432, database="bet_scanner", user="postgres", password="1234")
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO bookmakers (name, url, is_enabled, vpn_required) VALUES ('{name}', '{url}', {is_enabled}, {vpn_required})""".
                format(name=name, url=url, is_enabled=is_enabled, vpn_required=vpn_required))
        conn.commit()
        conn.close()


if __name__ == '__main__':
    fire.Fire(Cli)
