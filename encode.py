from suaBibSignal import SignalMeu
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf
import funcoes_LPF as utils

file, samplerate = sf.read("afew.wav")
s = SignalMeu()
s.fs = 44100
sd.default.samplerate = s.fs
sd.default.channels = 1

sinal = file[:,1]
lenSinal = len(sinal)
t = np.linspace(0, lenSinal/s.fs, lenSinal)

#Para comecar em 0, construiremos a onda de tal forma:
fp = 14000
portadora = np.cos(fp*2*np.pi*t)

#Normalizar:
max_value = max(sinal)

norm = [s/max_value for s in sinal]

plt.figure('Sinal Normalizado')
plt.plot(t, norm)
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Sinal Normalizado')
sd.play(norm)
sd.wait()






filtered = utils.filtro(norm, s.fs, 4000)

plt.figure('Sinal Filtrado')
plt.plot(t, filtered)
plt.xlabel('Tempo ()')
plt.ylabel('Amplitude')
plt.title('Sinal filtrado')

s.plotFFT(filtered, 'FFT filtrado')

sd.play(filtered)
sd.wait()





sinal_modulado = filtered*portadora

plt.figure('Sinal Modulado')
plt.plot(t, sinal_modulado)
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Sinal Modulado')

s.plotFFT(sinal_modulado, 'FFT Modulado')

sd.play(sinal_modulado)
sd.wait()

sf.write("afew_modulado.wav", sinal_modulado, s.fs)

plt.show()








