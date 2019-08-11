from sqlalchemy import create_engine
from tornado.options import define, options, parse_config_file
from os import path

config_file = '../../config.ini'
config_file_path = path.join(path.dirname(__file__), config_file)


# Get the database URL from the configuration file.
def get_database_url():
    define('database_user', type=str, group='application', help='Database name.')    
    define('database_port', type=str, group='application', help='Database port.')
    define('database_password', type=str, group='application', help='Database password.')
    parse_config_file(config_file_path)
    user = options.database_user
    port = options.database_port
    password = options.database_password
    
    return 'postgresql+psycopg2://' + user + ":" + password + "@localhost:" + port


def get_database_name():
    define('database_name', type=str, group='application', help='Database name.')
    parse_config_file(config_file_path)
    return options.database_name


def create_database():
    connection_string = get_database_url() 
    database_name = get_database_name()
    engine = create_engine(connection_string)
    conn = engine.connect()
    conn.execute("commit")
    conn.execute("create database " + database_name)
    conn.close()


create_database()
