N = int(input('Enter sample size: '))
n = int(input('Enter the number of intervals: '))

e = N / n

print('Expected value in each interval: ', e)

o = list(map(int, input('Enter number of observations in {0} intervals '.format(n)).split()))

print('Interval\t\Observed (O)\tExpected (E)\t(O - E)\t(O - E)^2\t100(O - E)^2 / E')

a = []

for i in range(n):
	r = o[i] - e
	a.append((r ** 2) / e)
	print(i, o[i], e, r, r ** 2, a[i], sep = '\t\t\t')
	print('')

chi = sum(a)

print('chi = ', chi)

chi_critical = float(input('Enter the critical value for chi square: '))

if chi <= chi_critical:
	print('Null hypothesis accepted.')
else:
	print('Null hypothesis rejected.')