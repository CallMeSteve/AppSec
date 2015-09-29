#!/usr/bin/python
# -*- coding: ascii -*

"""
Abdullah Sarwar
CS-UY 4753
Professor Justin Cappos
Main sandbox file for Linux.
Whitelist approach #2

New:
	- Removed arbritrary memory limit
	- Added RuntimeError exception handling
	- Added SystemExit to Whitelist
"""

from sys import argv
import resource

num_arg = len(argv)

safe = __builtins__.__dict__.keys()

safe.remove('open')
safe.remove('Exception')
safe.remove('IOError')
safe.remove('ImportError')
safe.remove('NameError')
safe.remove('exit')
safe.remove('print')
safe.remove('True')
safe.remove('raw_input')
safe.remove('range')
safe.remove('str')
safe.remove('RuntimeError')
safe.remove('reload')
safe.remove('SystemExit')

for not_safe in safe:
	del __builtins__.__dict__[not_safe]

if (num_arg) == 2:
	pass
else:
	raise Exception("Only 2 Arguments Allowed")	
	exit(1)

filename = argv[1]

try:
	oFile = open(filename, 'r')
except IOError:
	print "Not A Valid File, try again!"
	exit(2)

try:
	exec oFile
except RuntimeError:
	print "Runtime Error, try again!"
	exit(3)

oFile.close()
