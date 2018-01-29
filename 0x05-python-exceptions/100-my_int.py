#!/usr/bin/python3
"""
Module contains class MyInt
"""


class MyInt(int):

    def __eq__(self, other):
        """
        returns opp boolean of equals
        """
        return not super().__eq__(other)

    def __ne__(self, other):
        """
        returns opp boolean of neg
        """
        return not super().__ne__(other)
