from etl.transform import Transformer


class SkipTransformer(Transformer):
    def __init__(self, *args, **kwargs):
        pass

    def get_name(self, *args, **kwargs):
        return "SkipTransformer"

    def transform(self, data, *args, **kwargs):
        return data
