from etl.load import Loader
from utils.utils import connect_to_postgres
from settings.settings import Settings


class PostgresLoader(Loader):
    def __init__(self, *args, **kwargs):
        self.dialect = kwargs['loader']['dialect']
        self.destination_table = kwargs['loader']['destination']

    def get_name(self):
        return "PostgresLoader"

    def connect(self):
        pg_conf = {
            "dialect": self.dialect,
            "user": Settings.PRJ_POSTGRES_USER,
            "password": Settings.PRJ_POSTGRES_PASSWORD,
            "host": Settings.PRJ_POSTGRES_HOST,
            "port": Settings.PRJ_POSTGRES_PORT,
            "database": Settings.PRJ_POSTGRES_DATABASE
        }
        engine = connect_to_postgres(pg_conf)

        return engine

    def load(self, df, *args, **kwargs):
        table_name = self.destination_table
        engine = self.connect()

        df.to_sql(table_name,
                  engine,
                  if_exists='replace',
                  method='multi'
                  )

