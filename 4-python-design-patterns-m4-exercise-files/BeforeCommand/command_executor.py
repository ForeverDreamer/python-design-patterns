class CommandExecutor:

    def __init__(self):
        self._val = 0

    def execute_command(self, args):
        if args[0] == "CreateOrder":
            self.create_order()
        elif args[0] == "UpdateQuantity":
            self.update_quantity(args[1])
        elif args[0] == "ShipOrder":
            self.ship_order()
        else:
            print("Unrecognized command: " + args[0])

    def create_order(self):
        pass

    def update_quantity(self, val):
        old_val = self._val
        self._val = val
        print("Database Updated")
        print("Logging updated quantity from %s to %s" % (old_val, val))

    def ship_order(self):
        pass
