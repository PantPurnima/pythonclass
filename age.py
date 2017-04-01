dob =input("Enter your date of birth in YYYY-MM-DD format.  ")
a=dob.split("-")

f=float(a[0]) + float(a[1])/12+ float(a[2])/365
g=2017 + (3/12) + (19/365)
age=g-f
i= str(age)
k=i.split(".")

print ("age= {}".format(k[0]))