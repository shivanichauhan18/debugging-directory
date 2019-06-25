def string_both_ends(str):
	#print len(str)
	if len(str)>=2:
		return str[0:2] + str[-2:]
	else:
		return " "

print (string_both_ends("w3resource"))
print (string_both_ends("w3"))
print (string_both_ends("w"))
