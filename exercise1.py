a = raw_input("enter the marks of it")
b = raw_input("enter the marks of  dda")
c = raw_input("enter the marks of oop")
d = raw_input("enter the marks of sad")
e = raw_input("enter the marks of dl")
total = float(a) + float(b) + float(c) + float(d) + float(e)
percentage = (total/500) *100
print 'total = {}'.format(total)
print 'percentage = {:.2f} % '.format(percentage)

