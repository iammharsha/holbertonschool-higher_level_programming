#!/usr/bin/python3
"""Definition and implementation of Class MyList inherited from list"""


class MyList(list):
    """
    Class definition of MyList inhereted from list class

    Public methods:
        print_sorted(): Prints list, sorted in ascending order
    """

    def print_sorted(self):
        """
        Function to sort the contents of list

        Returns:
            None
        """

        sorted_list = sorted(self)
        print(sorted_list)
