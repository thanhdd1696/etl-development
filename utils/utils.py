import json
from datetime import datetime

import awswrangler as wr
from sqlalchemy import create_engine


def engine_creation(config):
    engine_conf = '{}://{}:{}@{}:{}/{}'.format(
        config['dialect'],
        config['user'],
        config['password'],
        config['host'],
        config['port'],
        config['database']
    )
    engine = create_engine(engine_conf)

    return engine


def wr_mysql_connection(connection_name):
    connection = wr.mysql.connect(connection_name)
    return connection


def read_config(config_file_path):
    f = open(config_file_path)
    conf = json.load(f)
    f.close()

    return conf


def time_to_string(t_str, fmt):
    pass


def string_to_time(t_str, fmt):
    pass
