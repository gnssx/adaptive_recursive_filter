import numpy as np

from AdaptiveRecursiveFilter import AdaptiveRecursiveFilter


def main():
	print "[ adaptive recursive filter ]"

	# parameters
	N = 100			# number of data samples
	M = 1			# number fo filter co-efficients
	f = 5			# frequency of sine wave (Hz)
	delta = 0.01		# forgetting factor
	noise_val = 0.5		# noise value
	uniform = False		# noise type

	# online filter
	arf = AdaptiveRecursiveFilter([N, M, f, delta, noise_val, uniform])


if __name__ == "__main__":
	main()
