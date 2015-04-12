try:
	float(['float() does not','like lists',2])
except TypeError,diag:#capture diagnostic info
	print 'Value Error'

