# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
#
# modified for use in UJ python course
"""
opisanie losowanie
"""

import random

class SelectionSort(object):
    """
    The selection sort
    """

    def __call__(self, lista):
        # Loop through the entire array
        for position in range(len(lista)):
            # Find the position that has the smallest number
            # Start with the current position
            minimal_position = position
            # Scan left to right (end of the list)
            for scanning_position in range(position+1, len(lista)):
                # Is this position smallest?
                if lista[scanning_position] < lista[minimal_position]:
                    # It is, mark this position as the smallest
                    minimal_positions = scanning_position
            # Swap the two values
            temp = lista[minimal_positions]
            lista[minimal_position] = lista[position]
            lista[position] = temp



class InsertionSort(object):
    """
    The insertion sort
    """

    def __call__(self, lista):
        # Start at the second element (pos 1).
        # Use this element to insert into the
        # list.
        for key_pos in range(1, len(lista)):

            # Get the value of the element to insert
            key_value = lista[key_pos]

            # Scan from right to the left (start of list)
            scan_pos = key_pos - 1

            # Loop each element, moving them up until
            # we reach the position the
            while (scan_pos >= 0) and (lista[scan_pos] > key_value):
                lista[scan_pos + 1] = lista[scan_pos]
                scan_pos = scan_pos - 1

            # Everything's been moved out of the way, insert
            # the key into the correct location
            lista[scan_pos +  1] = key_value


# This will point out a list
def print_list(lista):
    """
    Cos printuje sobie
    """
    for item in lista:
        print "%3d" % item,
    print "\n"

if __name__ == '__main__':
    # Create two lists of the same random numbers
    FIRST_LIST = []
    SECOND_LIST = []
    LIST_SIZE = 10
    for i in range(LIST_SIZE):
        new_number = random.randrange(100)
        FIRST_LIST.append(new_number)
        SECOND_LIST.append(new_number)

    # Print the original list
    print_list(FIRST_LIST)

    # Use the selection sort and print the result
    print "Selection Sort"
    SelectionSort()(FIRST_LIST)
    print_list(FIRST_LIST)

    # Use the insertion sort and print the result
    print "Insertion Sort"
    InsertionSort()(SECOND_LIST)
    print_list(SECOND_LIST)
