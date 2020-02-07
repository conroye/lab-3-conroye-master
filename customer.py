#! /usr/bin/env python3.7

"""
Customer class.

Elise Conroy
"""

import random


class Customer:
    """
    Customer of simulation.

    Contains customer information and randomizes
    customer current floor and destination floor.
    """

    current_floor = 0
    destination_floor = 0
    customer_id = 0
    in_elevator = False
    finished = False
    customer_direction = 0

    def __init__(self, customer_id, floors):
        """Randomize customer current floor and destination floor."""
        self.customer_id = customer_id
        self.current_floor = random.randint(1, floors)
        self.destination_floor = random.randint(1, floors)
        while self.destination_floor == self.current_floor:
            self.destination_floor = random.randint(1, floors)
        if self.current_floor < self.destination_floor:
            self.customer_direction = 1
        else:
            self.customer_direction = -1
