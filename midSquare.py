n = int(input("Enter the number of digits in the starting number. Number of digits should be even. "))
seed_number = int(input("Please enter a {0} number: ".format(n)))
number = seed_number
already_seen = set()
counter = 0

while number not in already_seen:
    counter += 1
    already_seen.add(number)
    number = int(str(number * number).zfill(2 * n)[n//2: (3*n)//2])
    print(f"{counter}: {number}")

print(f"{number} has appeared before in the sequence.")