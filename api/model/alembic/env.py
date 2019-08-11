from __future__ import with_statement
from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig
from tornado.options import define, options, parse_config_file


def get_database_url():
    config_file_path = "../../config.ini"
    define('database_user', type=str, group='application', help='Database name.')
    define('database_name', type=str, group='application', help='Database name.')
    define('database_port', type=str, group='application', help='Database port.')
    define('database_password', type=str, group='application', help='Database password.')
    parse_config_file(config_file_path)
    name = options.database_name
    user = options.database_user
    port = options.database_port
    password = options.database_password

    return 'postgresql+psycopg2://' + user + ":" + password + "@localhost:" + port + "/" + name

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = None

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    #url = config.get_main_option("sqlalchemy.url")
    url = get_database_url()
    
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)
    print("::::::")
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    config_section = config.get_section(config.config_ini_section)
    config_section["sqlalchemy.url"] = get_database_url()
    
    connectable = engine_from_config(
        config_section,
        prefix='sqlalchemy.',
        poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
