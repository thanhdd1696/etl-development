from unittest.pipeline_creation import PipelineCreationTest
from etl.pipeline import Pipeline
from utils.utils import read_config


def pipeline_creation_test(config):
    etl_test = PipelineCreationTest()
    etl_test.test(config=config)


if __name__ == "__main__":
    pipeline_creation_test(read_config("pipeline_configs.json"))

    print("All tests passed")
