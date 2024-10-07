from etl.extract import Extractor
import pandas as pd

import awswrangler as wr

from settings.settings import Settings


class SqlExtractor(Extractor):
    def __init__(self,
                 name='SqlExtractor'):
        self.file_path = Settings.PRJ_JSON_FILE_PATH
        self.name = name

    def get_name(self, *args, **kwargs):
        return self.name

    def extract(self, connection, query):
        df = wr.mysql.read_sql_query(
            sql=query,
            con=connection
        )
        return df

