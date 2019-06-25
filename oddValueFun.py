def odd_values_string(Str):
	result = ""
	i=0
	k=1
	while i<len(Str):
		if k % 2 == 1: # give this error TypeError: range() integer end argument expected, got type.

			result = result + Str[i]
		i=i+1
		k=k+1
	return result

print(odd_values_string('abcdef'), odd_values_string('python'))


#ERROR THIS TYPE WHEN WE PUT Str HAVE PUT RANGE

#TypeError: range() integer end argument expected, got type.
#TypeError: 'str' object is not callable
