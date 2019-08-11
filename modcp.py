from api.scripts.add_user import add_user
from tornado.options import define, options, parse_command_line

if __name__ == "__main__":

    # Configuration options.
    define("command", default="User", help="Configuration option to execute.")
    parse_command_line()

    command = None
    prompt = ''
    continue_execution = True
    command_heading = ''

    if options.command == "User":
        command = add_user
        prompt = "Do you wish to continue adding users?" + " (Y/N) "
        command_heading = "Adding a user"

    print(command_heading)
    print("====================================")

    # Execute command in a loop until the user is done
    while continue_execution:
        command()
        confirmation = input(prompt)
        if confirmation is "N":
            continue_execution = False
    