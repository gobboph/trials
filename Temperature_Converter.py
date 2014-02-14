#!/usr/bin/env python

import string
import numpy

def CtoF(Tc):
	return (9.0/5)*Tc+32
def FtoC(Tf):
	return (5.0/9)*(Tf-32)

T_in = float(raw_input("What's the temperature you want to convert? "))
scale = raw_input("Do you want to convert it in (C)elsius or (F)arenheit? ")

if scale == "C":
	print "%.2f F = %.2f C" %(T_in, FtoC(T_in))

if scale == "F":
	print "%.2f C = %.2f F" %(T_in, CtoF(T_in))