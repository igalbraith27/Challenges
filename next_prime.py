inputed = input("Next prime y/n?")
prime = 1

def is_prime(n):
	if n % 2 == 0:
		return False

	for i in range(3, int(n**0.5) + 1):
		if n % i == 0:
			return False

	return True

while inputed.lower() == 'y':
	prime += 1

	while !is_prime(prime):
		prime += 1

	print "Next prime is: " + str(prime)
	inputed = raw_input("Continue y/n?")
