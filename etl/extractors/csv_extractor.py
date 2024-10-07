from etl.extract import Extractor
import pandas as pd
from settings.settings import Settings


class CsvExtractor(Extractor):
    def __init__(self):
        self.file_path = Settings.PRJ_CSV_FILE_PATH

    def get_name(self, *args, **kwargs):
        return "CsvExtractor"

    def extract(self, *args, **kwargs):
        data = pd.read_csv(self.file_path)
        return data


