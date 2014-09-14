#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""flemish T11"""


import inquisition
from inquisition import SPANISH

FISHY = SPANISH.replace('surprise','haddock')
print FISHY

r ='Spanish'
rlen=len(r)

FLEMISH=FISHY[0:FISHY.index(r)]+'Flemish'+FISHY[FISHY.index(r)+rlen:]
print "\n",FLEMISH