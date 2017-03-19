equation=raw_input('Enter an equation of line in the form y=mx+c')
a=equation.split("+")
print('intercept={}'.format(a[1]))
b=equation.split("+")[0].split("=")
c=b[1]
d=c.replace('x','')
e=d.strip("")
print ('slope={}'.format(e))
