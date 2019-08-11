from getpass import getpass
from api.model.sessionHelper import get_session
from tornado.options import define
from api.Utils import do_save_user

define('database_user', type=str, group='application', help='Database user.')
define('database_name', type=str, group='application', help='Database name.')
define('database_port', type=str, group='application', help='Database port.')
define('database_password', type=str, group='application', help='Database password.')

def add_user():

    username = input("Choose a username: ")
    password = getpass("Choose a password: ")
    email = input("Enter a valid email address: ")
    name = input("Choose a user name: ")
    print(password)

    user = {
      'username': username,
      'password': password,
      'email': email,
      'name': name,
      'failed_attempts': 0,
      'type': 'database'
    }

    session_object = get_session()
    session = session_object()
    do_save_user(user, session, is_valid=True)
