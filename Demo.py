def safe_float(obj):
	try:
		retval=float(obj)
	except ValueError:
		retval='could not convert non-number to float'
	except TypeError:
		retval='object type cannot be convert to float'
	return retval