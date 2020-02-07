#! /usr/bin/env python3.7

"""
Building class.

Elise Conroy
"""

from elevator import Elevator
from customer import Customer


class Building:
    """
    Building of simulation.

    Contains number of floors as well as customer list and the
    functionality of elevator picking up and dropping off customers.
    """

    number_of_floors = 0
    customer_list = []
    elevator = 0
    max_floor = 0

    def __init__(self, floors, customers):
        """Initialize floors and customers."""
        self.number_of_floors = floors
        for customer_id in range(1, customers + 1):
            new = Customer(customer_id, self.number_of_floors)
            self.customer_list.append(new)
        # anonymous function - coe tutor
        self.customer_list.sort(key=lambda x: x.current_floor)
        self.elevator = Elevator(floors, self.customer_list)
        self.max_floor = self.maxfloor()
        self.run()

    def run(self):
        """Begin running simulation."""
        print('-------------------BEGIN ELEVATOR SIMULATION---------------')
        # number_of_customers = len(self.customer_list)
        self.output()

    def output(self):
        """Move the elevator up and down and remove customers."""
        for customer in self.customer_list:
            print("Customer", customer.customer_id, "is on floor ", end='')
            print(customer.current_floor, "and wants to go to ", end='')
            print(customer.destination_floor)

        # ELEVATOR MOVING UP LOOP
        while self.elevator.current_floor < self.max_floor:
            self.elevator.current_floor += 1
            print('ELEVATOR MOVING UP')
            print(len(self.customer_list), 'Customers in elev.')
            print('----------------------------------------------------')
            print('FLOOR', self.elevator.current_floor)

            for customer in self.customer_list:
                if self.elevator.current_floor == customer.current_floor:
                    customer.in_elevator = True  # picks them up
                    print('Customer', customer.customer_id, end='')
                    print(' has entered the elev')
                if self.elevator.current_floor == customer.destination_floor:
                    if customer.in_elevator:
                        customer.in_elevator = False
                        customer.finished = True
                        # self.customer_list.remove(customer)
                        print(customer.customer_id, 'has reached', end='')
                        print(' their destination')

            self.customer_list = [i for i in self.customer_list if not customer.finished]

        # ELEVATOR MOVING DOWN LOOP
        while self.elevator.current_floor > 1:
            self.elevator.current_floor -= 1
            print(len(self.customer_list), 'Customers in elev.')
            print('ELEVATOR MOVING DOWN')
            print('----------------------------------------------------')
            print('FLOOR', self.elevator.current_floor)

            for customer in self.customer_list:
                if customer.in_elevator:
                    customer.current_floor = self.elevator.current_floor
                if self.elevator.current_floor == customer.destination_floor:
                    if customer.in_elevator:
                        # customer.in_elevator = False
                        customer.finished = True
                        customer.in_elevator = False
                        # self.customer_list.remove(customer)
                        print('Customer', customer.customer_id, end='')
                        print(' has reached their destination')

            self.customer_list = [i for i in self.customer_list if not customer.finished]

    def maxfloor(self):
        """Find max floor of customer destinations."""
        max_floor = 2
        for c_c in self.customer_list:
            customer_max = max(c_c.current_floor, c_c.destination_floor)
            max_floor = max(customer_max, max_floor)
        return max_floor
