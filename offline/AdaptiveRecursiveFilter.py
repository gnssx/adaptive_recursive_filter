import numpy as np
import sys

from AddNoise import AddNoise


class AdaptiveRecursiveFilter(AddNoise):

	def __init__(self, params):
		self._M = params[0]
		self._delta = params[1]

	def offline_filter(self, noisy_data, noise):
		# setup filter parameters and apply recursive least squares (RLS) algorithm
		N = noisy_data.shape[0]		# number of data samples
		h = np.zeros((self._M,1))	# filter co-efficients
		error = np.zeros((N,1))		# error
		progress = np.zeros((N,1))	# 0th filter co-efficient progress
		for n in range(N - self._M):
			tmp = noise[n:n + self._M]
			error[n] = noisy_data[n] - np.dot(tmp.T, h)
			h += (self._delta * tmp * error[n]) # / np.linalg.norm(tmp)
			progress[n] = h[0]
		return error, progress
