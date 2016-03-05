import numpy as np

from AdaptiveRecursiveFilter import AdaptiveRecursiveFilter
from matplotlib import pyplot as plt


# plot data with title at corresponding subplot given by ax
def plot(data, ax, title):
	font_size = 15
	ax.plot(data)
	ax.grid()
	ax.axis([0, data.shape[0], -2, 2])
	ax.set_xlabel("samples", fontsize=font_size)
	ax.set_ylabel("amplitude", fontsize=font_size)
	ax.set_title(title, fontsize=font_size)


def main():
	print "[ adaptive recursive filter ]"

	# parameters
	N = 1000		# number of data samples
	M = 1			# number fo filter co-efficients
	f = 5			# frequency of sine wave (Hz)
	delta = 0.01		# forgetting factor
	noise_val = 0.5		# noise value
	uniform = False		# noise type
	params = [M, delta]

	# setup offline adaptive recursive filter
	arf = AdaptiveRecursiveFilter(params)

	# setup plotting
	fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)
	fig.tight_layout(pad=3, w_pad=3, h_pad=3)
	fig.suptitle("Adaptive Recursive Filter - Recursive Least Squares (RLS) Algorithm", fontsize=15)

	# generate original data
	data = np.array([np.sin(2 * np.pi * f * n / N)
		for n in range(N)]).reshape(N, 1)
	plot(data, ax1, "original data")
	
	# generate noise and add noise to data to get noisy data
	noise = arf.gen_noise(data, noise_val, uniform)
	noisy_data = data + noise
	plot(noisy_data, ax2, "noisy data")
	
	# apply offline adaptive recursive filter
	error, progress = arf.offline_filter(noisy_data, noise)
	
	# plot error and progress
	plot(error, ax3, "filtered data")
	plot(progress, ax4, "0th filter co-efficient")
	plt.show()


if __name__ == "__main__":
	main()
