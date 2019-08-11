import alembic.config
import os

alembicArgs = ['--raiseerr', 'upgrade', 'head']

current_dir = os.getcwd()
migration_directory = "api/model"

os.chdir("api")
os.chdir("model")
alembic.config.main(argv=alembicArgs)
os.chdir(current_dir)
