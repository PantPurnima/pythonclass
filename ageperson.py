Age = raw_input ('enter your age ')
age=float(Age)
if age<=0:
	print "Invalid age"
elif 0<age<=1:
	print"Infant"
elif 1<age<=12:
	print"Kid"
elif 12<age<=19:
	print"Teenager"
elif 19<age<=45:
	print"Adult"
elif age<=60:
	print"middle aged"
elif age<=120:
	print "old"
else:
	print " You re too old to b still alive."