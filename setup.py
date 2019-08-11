from api.scripts.installtools import setup

scripts = [
     'create_database.py', 
     'run_migrations.py'
]

setup("Morpheus", "requirements.txt", scripts)