from unittest.base_test import BaseTest
from etl.pipeline import Pipeline


class PipelineCreationTest(BaseTest):
    def __init__(self):
        self.pipe = None

    def test(self, *args, **kwargs):
        config = kwargs['config']

        self.test_pipeline_creation(config)
        self.test_components_name(self.pipe, config)

    def test_pipeline_creation(self, config):
        try:
            pipe = Pipeline()
            pipe.factory_construct(config)
            self.pipe = pipe
        except Exception as e:
            raise "Pipeline Creation Error"

    def test_components_name(self, pipe, config):
        assert pipe.extractor.get_name() == config['extractor']['name']
        assert pipe.transformer.get_name() == config['transformer']['name']
        assert pipe.loader.get_name() == config['loader']['name']
