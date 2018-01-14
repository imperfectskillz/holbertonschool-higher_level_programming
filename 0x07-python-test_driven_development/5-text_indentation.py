#!/usr/bin/python3
"""
Module for text indentation
"""


def text_indentation(text):
    """Function that adds new lines"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    space = False
    temp = ''
    for i in text:
        if space is True and i == ' ':
            space = False
            continue
        temp += i
        if i == '.' or i == ':' or i == '?':
            temp += ('\n\n')
            space = True
    print(temp)
