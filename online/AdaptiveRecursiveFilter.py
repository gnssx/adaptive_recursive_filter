import numpy as np

from Animate import Animate


class AdaptiveRecursiveFilter(Animate):

	def _online_filter(self, frame_num):
		n = frame_num % self._N
		# generate noise
		noise = np.random.uniform(-self._noise_val, self._noise_val) \
				if self._uniform \
				else  (self._noise_val * np.random.normal())
		self._noise = self._noise[1:]
		self._noise = np.append(self._noise, noise)
		# generate sample and add noise
		samp = np.sin(2 * np.pi * self._f * n / self._N) + noise
		self._noisy_data = self._noisy_data[1:]
		self._noisy_data = np.append(self._noisy_data, samp)
		# recursive least squares (RLS) algorithm
		for n in range(self._N - self._M):
			tmp = self._noise[n:n + self._M].reshape(self._M, 1)
			self._error[n] = self._noisy_data[n] - np.dot(tmp.T, self._h)
			self._h += (self._delta * tmp * self._error[n]) # / np.linalg.norm(tmp)

	def _setup_params(self, params):
		self._N = params[0]
		self._M = params[1]
		self._f = params[2]
		self._delta = params[3]
		self._noise_val = params[4]
		self._uniform = params[5]

	def _create_data(self):
		self._t = np.array([n for n in range(self._N)]).reshape(self._N, 1)
		self._noise = np.zeros((self._N,1))
		self._noisy_data = np.zeros((self._N,1))
		self._error = np.zeros((self._N,1))
		self._h = np.zeros((self._M,1))
