import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal as window

class SignalMeu(object):
    def __init__(self):
        self.init = 0
        self.fs = 0

    def __init__(self):
        self.init = 0

    def generateSin(self, freq, amplitude, time, fs):
        n = time*fs
        x = np.linspace(0.0, time, int(n))
        s = amplitude*np.sin(freq*x*2*np.pi)
        return (x, s)

    def calcFFT(self, signal):
        N  = len(signal)
        W = window.hamming(N)
        T  = 1/self.fs
        xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
        yf = fft(signal*W)
        return(xf, np.abs(yf[0:N//2]))

    def plotFFT(self, signal, title):
        x,y = self.calcFFT(signal)
        # lim = [1e3,22e3,-1000, 2e3]
        # plt.axis(lim)
        plt.figure(title)
        plt.plot(x, np.abs(y))
        plt.title(title)
