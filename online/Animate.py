from matplotlib import animation as animation
from matplotlib import pyplot as plt


class Animate:

	_fontsize = 15

	def __init__(self, params):
		# setup
		self._setup_params(params)
		self._create_data()
		self._setup_plot()
		self._setup_axes()
		# start animation
		self._anim = animation.FuncAnimation(self._fig, self._animate, \
							init_func=self._init, \
							repeat=True, \
							interval=30, \
							blit=True)
		plt.show()

	def _init(self):
		# initialize animation
		self._line_noisy_data.set_data(self._t, 0)
		self._line_result.set_data(self._t, 0)
		return self._line_noisy_data, self._line_result,

	def _animate(self, frame_num):
		# calculate at every frame
		self._online_filter(frame_num)
		return self._update_plot()

	def _setup_params(self, params):
		pass

	def _create_data(self):
		pass

	def _setup_plot(self):
		self._fig, self._ax1 = plt.subplots(nrows=1, ncols=1)
		self._fig.tight_layout(pad=3, w_pad=0, h_pad=0)
		self._fig.suptitle("Online Adaptive Recursive Filter", \
							fontsize=self._fontsize)
		self._fig.canvas.set_window_title("Online Adaptive Recursive Filter")

	def _setup_axes(self):
		self._ax1.axis([0, self._N, -2, 2])
		self._ax1.set_xlabel("samples", fontsize=self._fontsize)
		self._ax1.set_ylabel("amplitude", fontsize=self._fontsize)	
		self._line_noisy_data, = self._ax1.plot([], [], "r")
		self._line_result, = self._ax1.plot([], [], "b")

	def _update_plot(self):
		self._line_noisy_data.set_ydata(self._noisy_data)
		self._line_result.set_ydata(self._error)
		return self._line_noisy_data, self._line_result,
