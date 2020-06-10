import sys
from command_executor import CommandExecutor


if len(sys.argv) < 2:
    print(r'Usage: C:\Python27\python -m BeforeCommand <command>')
    print('Commands:')
    print('    CreateOrder')
    print('    UpdateQuantity number')
    print('    ShipOrder')
    exit()

executor = CommandExecutor()
print('控制台参数列表： ' + ', '.join(sys.argv))
executor.execute_command(sys.argv[1:])
