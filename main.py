x=[[1,"Rohan",1111],[2,"Raj",2222],[3,"Ravi",3333]]
print(x)
print(x[:2])
print(x[0:2])
print(x[0:])
import numpy
a = numpy.array(x)
print(a)
print(a[1])
print(a[1][2])
print(a[:][2])
print(a[][2])