"""Classification: Creational"""

from person import Person
from mycomputer_builder import MyComputerBuilder
from budget_box_builder import BudgetBoxBuilder

print('=====================================')
mcBuilder = MyComputerBuilder()
mcBuilder.build_computer()
computer = mcBuilder.get_computer()
computer.display()
print('=====================================')
bbBuilder = BudgetBoxBuilder()
bbBuilder.build_computer()
computer = bbBuilder.get_computer()
computer.display()

