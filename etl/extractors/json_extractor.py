from etl.extract import Extractor
import pandas as pd
from settings.settings import Settings


class JsonExtractor(Extractor):
    def __init__(self):
        self.file_path = Settings.PRJ_JSON_FILE_PATH

    def extract(self, *args, **kwargs):
        # TODO read json
        data = pd.read_csv(self.file_path)
        return data
