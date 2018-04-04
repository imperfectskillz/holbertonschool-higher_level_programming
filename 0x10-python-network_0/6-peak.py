#!/usr/bin/python3
"""
returns peak
"""

def find_peak(list_of_integers):
   """
   finds peak
   """

    if list_of_integers is None:
       return None

   temp = []

   if (list_of_integers[0] >= list_of_integers[1]):
      temp.append(list_of_integers[0]

   i = 0
   while i < len(list_of_integers):
   if (list_of_integers[i - 1] <= list_of_integers[i] and list_of_integers[i + 1] <= list_of_integers[i]):
      temp.append(list_of_integer[i])
      i += 1

   return max(temp)

    
