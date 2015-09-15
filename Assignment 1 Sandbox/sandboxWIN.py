from sys import argv

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
safe

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
	print "Not A Valid File"
	exit(2)

#no exceptions
exec oFile

oFile.close()