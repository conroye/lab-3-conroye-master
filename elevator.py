#! /usr/bin/env python3.7

"""
Elevator class.

Elise Conroy
"""


class Elevator:
    """
    Elevator of simulation.

    Contains number of floors as well as register list and the
    current floor, can also cancel customers.
    """

    number_of_floors = 0
    register_list = []
    current_floor = 0
    up = 1
    down = -1

    def __init__(self, number_of_floors, register_list):
        """Initialize number of floors and register list."""
        self.number_of_floors = number_of_floors
        self.register_list = register_list

    def move(self):
        """Move functionality."""
        # pass

    def register_customer(self, customers):
        """Add customer to register."""
        for reg in customers:
            self.register_list.append(reg)

    def cancel_customer(self, customers):
        """Cancel customer functionality."""
        # pass
