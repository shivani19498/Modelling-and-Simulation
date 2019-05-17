m = int(input("Enter the modulus 'm' for the generator: "))
a = int(input("Enter the multiplier 'a' for the generator: "))
c = int(input("Enter the increment 'c': "))
x = int(input("Enter the initial seed: "))

initial_seed, count = x, 1
print(x, end = ' ')
x = (a * x + c) % m

while x != initial_seed: 
	print(x, end = ' ')
	count = count + 1
	x = (a * x + c) % m

print('')
print('Period of this generator is ', count)