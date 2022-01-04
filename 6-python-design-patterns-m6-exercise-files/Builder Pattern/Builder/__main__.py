"""Classification: Creational"""

from person import Person
from mycomputer_builder import MyComputerBuilder
from budget_box_builder import BudgetBoxBuilder

computer_builder = Person(MyComputerBuilder())
computer_builder.build_computer()
computer = computer_builder.get_computer()
computer.display()

computer_builder = Person(BudgetBoxBuilder())
computer_builder.build_computer()
computer = computer_builder.get_computer()
computer.display()

