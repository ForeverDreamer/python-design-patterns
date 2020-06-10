from create_order import CreateOrder
from update_order import UpdateOrder
from ship_order import ShipOrder
from no_command import NoCommand
import sys


def get_commands():
    commands = (CreateOrder, UpdateOrder, ShipOrder)
    return {cls.name: cls for cls in commands}


def print_usage(commands):
    print('Usage: python -m Command CommandName [arguments]')
    print('Commands:')
    for cmd in commands.values():
        print('    {}'.format(cmd.name))


def parse_command(commands, args):
    print(type(args))
    print(args)
    cmd = commands.setdefault(args[0], NoCommand)
    return cmd(args)


comms = get_commands()
if len(sys.argv) < 2:
    print_usage(comms)
    exit()

# Find and execute the command
print(sys.argv)
command = parse_command(comms, sys.argv[1:])
command.execute()
