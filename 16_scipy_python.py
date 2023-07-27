from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 10)
y = x ** 2
plt.scatter(x, y)

##################### INTERPOLATION ##################################
f = interp1d(x, y, kind='linear')

new_x = np.linspace(0, 10, 30)
result = f(new_x)

plt.scatter(x, y)
plt.scatter(new_x, result, c='r')


######################## OPTIMISATION ##############################

def f(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d


from scipy import optimize

print(optimize.curve_fit(f, x, y))

plt.scatter(x, y)
# plt.plot(x, f(x, params[0], params[1], params[2], params[3]), c='g', lw=3)

plt.show()

##################### SIGNAL/PROCESSING ########################
"""
from scipy import signal

new_y = signal.detrend(y)

plt.plot(x, y)
plt.plot(x, new_y)
"""
from scipy import fftpack

fourier = fftpack.fft(y)
power = np.abs(fourier)
frequences = fftpack.fftfreq(y.size)
plt.plot(np.abs(frequences), power)

filtered_signal = fftpack.ifft(fourier)

plt.figure(figsize=(12, 8))
plt.plot(x, y, lw=0.5)
plt.plot(x, filtered_signal, lw=3)

plt.show()


##################### NDIMAGE #################################



