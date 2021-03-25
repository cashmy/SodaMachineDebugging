from dCC_Python_SodaMachine import user_interface
from dCC_Python_SodaMachine.customer import Customer
from dCC_Python_SodaMachine.soda_machine import SodaMachine


class Simulation:
    def __init__(self):
        self.run_simulation()


    def run_simulation(self):
        """The central method called in main.py."""
        customer = Customer()
        soda_machine = SodaMachine()
        will_proceed = True
        while will_proceed:
            user_option = user_interface.simulation_main_menu()
            if user_option == 0:
                soda_machine.begin_transaction(customer)
            elif user_option == 1:
                customer.check_coins_in_wallet()
            elif user_option == 2:
                customer.check_backpack()
            else:
                will_proceed = False
