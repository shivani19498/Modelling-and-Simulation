n = int(input('Enter the number of random numbers: '))

r = list(map(float, input('Enter {0} random numbers between 0 and 1\n'.format(n)).split()))

r.sort()

d = -1

for i in range(len(r)):
	ch = ((i + 1) / n) - r[i]
	cl = r[i] - (i / n)
	c = max(cl, ch)
	d = max(c, d)

# print('d = ', d)

d_alpha = float(input('Enter the critical value D-alpha: '))

if d <= d_alpha:
	print('The data is uniform.')
else:
	print('The data is not uniform.')

# 5
# 0.05 0.81 0.44 0.93 0.14
# 0.565