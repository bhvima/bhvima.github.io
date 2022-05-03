from math import comb

J = 1
mu = 1.1

def N(n, r, k):
	return (comb(n - r - 1, k - 1) * comb(r - 1, k - 1) * n)//k

def E(n, r, k):
	return -J * (n - 4 * k) + mu * (n - 2 * r)

def compute_average_energy(n):
	for r in range(1, n):
		for k in range(1, r):
			


compute_average_energy(10)
