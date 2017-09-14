import math

def my_abs(x):
	if not isinstance(x, (int, float)):
			raise TypeError('bad operand type')

	if x >= 0:
		return x
	else:
		return -x


def powerN(x, n = 2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s


# print(powerN(2))


def encroll(name, gender, age=6, city='Beijing'):
	print(name, gender, age, city)


def person(name, age, **kv):
	print(name, age, kv)

person('adam', 20, city='Beijing')

names = [1, 2, 4, 5]
print(names[-1])

L = list(range(100))

print(L[:10:2])


for x, y in [(1, 1), (2, 4), (3, 9)]:
	print(x, y)



LL = [x * x for x in range(1, 11) if x % 2 == 0]


print(LL)



g = (x * x for x in range(10000000000000))

print(next(g))

for n in g:
	print(n)







