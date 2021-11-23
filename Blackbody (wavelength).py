#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 20:18:30 2021

@author: Viktor Sumida
"""

#####################################################
## Blackbody radiation as a function of wavelength ##
#####################################################

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

fig = plt.figure()
visivel = fig.add_subplot(111)
rect1 = patches.Rectangle((0.4, 0), 0.35, 1e15, alpha=0.8, color='xkcd:cyan')
visivel.add_patch(rect1)

h = 6.62607015e-34
c = 3.0e+8
k = 1.38064852e-23

def planck(wave, T):
    a = 2*h*c**2
    comp_onda = wave * 1.e-6
    b = h*c/(comp_onda*k*T)
    intensity = a/((comp_onda**5) * (math.e**b - 1.0))
    return intensity

wavelengths_low = np.linspace(0.001, 1000, 1000000)
wavelengths_high = np.linspace(0.01, 1000, 1000000)

intensity_O = planck(wavelengths_low, 40000.0)
intensity_B = planck(wavelengths_low, 20000.0)
intensity_A = planck(wavelengths_high, 9000.0)
intensity_F = planck(wavelengths_high, 7000.0)
intensity_G = planck(wavelengths_high, 5500.0)
intensity_K = planck(wavelengths_high, 4500.0)
intensity_M = planck(wavelengths_high, 3000.0)

plt.loglog(wavelengths_low, intensity_O * 1e-06, 'r-')
plt.loglog(wavelengths_low, intensity_B * 1e-06, 'g-')
plt.loglog(wavelengths_high, intensity_A * 1e-06, 'b-')
plt.loglog(wavelengths_high, intensity_F * 1e-06, 'c-')
plt.loglog(wavelengths_high, intensity_G * 1e-06, 'm-')
plt.loglog(wavelengths_high, intensity_K * 1e-06, 'y-')
plt.loglog(wavelengths_high, intensity_M * 1e-06, 'xkcd:sky blue')

plt.title ('Espectro de corpo negro', fontsize=20)

plt.legend(['O (40000K)', 'B (20000K)', 'A (9000K)', 'F (7000K)', 'G (5500K)', 'K (4500K)',
            'M (3000K)', 'Visível'], loc=0)

plt.xlabel('Comprimento de onda [\u03BCm]', fontsize=15)
plt.ylabel('Intensidade [W/(m$^2$ \u03BCm sr)]', fontsize=15)

plt.grid(True, which="both")
plt.xlim(3e-03, 3e+03)
plt.ylim(1e-03, 1e+13)

plt.show()