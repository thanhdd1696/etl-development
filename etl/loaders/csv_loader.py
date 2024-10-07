from etl.load import Loader
from settings.settings import Settings


class CsvLoader(Loader):
    def __init__(self):
        self.outfile_path = Settings.PRJ_CSV_FILE_PATH

    def get_name(self):
        return "CsvLoader"

    def load(self, df, *args, **kwargs):
        df.to_csv(self.outfile_path, index=False)

