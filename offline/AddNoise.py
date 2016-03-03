import numpy as np


class AddNoise:

	def gen_noise(self, data, noise_val, uniform=True):
		# if type 1 return uniform noise to data, else return Gaussian noise
		return ( np.random.uniform(-noise_val, noise_val+1, size=data.shape) \
				if uniform \
				else (noise_val * np.random.normal(size=data.shape)) \
				).astype(data.dtype)

	def add_noise(self, data, noise_val, uniform=True):
		return data + self.gen_noise(data, noise_val, uniform)
