from tornado.options import define, options

def load_options(config_file):

    # General application settings
    define('port', type=int, group='application', help='Port to run the application from.')
    define('compress_response', type=bool, group='application', help='Whether or not to compress the response.')
    define('notifications_enabled', type=bool, group='application', help='Whether or not to enable notifications.')

    # Security options
    define('serve_https', type=bool, group='application', help='Whether to serve the application via HTTPS or not.')
    define('ssl_cert', type=str, group='application', help='Path to the SSL certificate.')
    define('ssl_key', type=str, group='application', help='Path to the SSL key.')
    define('cookie_secret', type=str, group='application', help='Cookie signing secret.')
    define('validate_user_email', type=bool, group='application', help='Whether to validate the user provided email.')

    define('max_login_tries', type=int, group='application', help='Maximum number of login tries.')
    define('login_delay_time_step', type=int, group='application', help='Delay time between logins.')
    define('lockout_time_window', type=int, group='application', help='Time window to lock the user out.')

    options.parse_config_file(config_file)

    return options.group_dict('application')
