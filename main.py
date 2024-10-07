from etl.pipeline import create_pipeline
from utils.utils import read_config


if __name__ == "__main__":
    pipeline_configs = read_config("pipeline_configs.json")

    pipe = create_pipeline(pipeline_configs)
    pipe.run()

