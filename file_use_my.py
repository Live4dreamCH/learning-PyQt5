import pickle
from oop import Point

output = open(file='class.data', mode='wb')
pickle.dump(obj=Point, file=output)
output.close()

infile = open(file='class.data', mode='rb')
saved_class = pickle.load(file=infile)

a = saved_class(y=1, x=2)
b = saved_class()
assert (a.dis(b) == b.dis(a))
a.print()
b.print()
print(a.dis(b))
