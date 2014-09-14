#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Asks the great question."""


THE_GREAT_QUESTION = ('Michaelangelo. Leonardo. Rafael. Donatello. Turtles? '
                      'Creators of the great works? Both? You be the judge!')

# task 4
STATEMENTS = THE_GREAT_QUESTION.split('. ')
print STATEMENTS



# task 5: slice

ARTISTS = STATEMENTS[0:4]
print ARTISTS

# TAsk 6: length

CHARACTERS = len(ARTISTS)
print CHARACTERS

# TASK 7

HAS_CREATORS = 'Creators' in THE_GREAT_QUESTION
print HAS_CREATORS

# T7(2)
HAS_SPLINTER = 'Splinter' in ARTISTS
print HAS_SPLINTER