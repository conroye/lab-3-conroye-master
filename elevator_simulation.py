#! /usr/bin/env python3.7

"""
This program allows the user to run an elevator simulation.

The simulation takes input from the user for number of floors
and number of customers in a building, and creates a theoretical
building in which customers get on and off an elevator according to
their random current floors and destination floors. It uses the
Building, Elevator, and Deck classes.

Elise Conroy
"""

from building import Building


def main():
    """Driver code."""
    try:
        floors = int(input('Number of floors: '))
        customers = int(input('Number of customers: '))
        building = Building(floors, customers)

    except ValueError:
        print('Not a valid integer.')
        main()


if __name__ == "__main__":
    main()
