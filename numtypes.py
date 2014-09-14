#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Number Types practice"""

import fractions
import decimal 

# L2 HW2 T15
FLOATVAR = 0.1
DECIMALVAR = decimal.Decimal("0.1")
FRACTIONVAR = fractions.Fraction("1/10")


print FLOATVAR,"\n", DECIMALVAR,"\n",FRACTIONVAR

# L2 HW2 T16
"""Testing Equality"""
DF_EQUALITY = DECIMALVAR==FRACTIONVAR
ARE_INEQUAL = DECIMALVAR!=FRACTIONVAR!=FRACTIONVAR
print DF_EQUALITY
print ARE_INEQUAL