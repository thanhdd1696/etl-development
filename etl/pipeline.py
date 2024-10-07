# from etl.extract import Extractor
from etl.extractors.csv_extractor import CsvExtractor
from etl.extractors.json_extractor import JsonExtractor

# from etl.transform import Transformer
from etl.transformers.skip_transformer import SkipTransformer

# from etl.load import Loader
from etl.loaders.csv_loader import CsvLoader
from etl.loaders.postgres_loader import PostgresLoader


def create_pipeline(pipeline_config):
    print(pipeline_config)

    pipe = Pipeline()
    pipe.factory_construct(pipeline_config)

    return pipe


class Pipeline:
    def __init__(self):
        self.extractor = None
        self.transformer = None
        self.loader = None

    def factory_construct(self, config):
        extractor_name = config['extractor']['name']
        transformer_name = config['transformer']['name']
        loader_name = config['loader']['name']

        extractor_constructor = globals()[extractor_name]
        transformer_constructor = globals()[transformer_name]
        loader_constructor = globals()[loader_name]

        self.extractor = extractor_constructor(config)
        self.transformer = transformer_constructor(config)
        self.loader = loader_constructor(config)

    def run(self):
        extract_data = self.extractor.extract()
        transformed_data = self.transformer.transform(extract_data)
        self.loader.load(transformed_data)
