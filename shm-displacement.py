"""
Simple Harmonic Motion's Displacement Equation in Action
Displacement equation: x = A sin(wt + Φ)
"""

import math
import time

# Main func
def shm(amplitude, frequency, phase, time):
    return amplitude * math.sin(frequency * time + phase)

# Adjust values for different patterns
amplitude = 10
frequency = 10
phase = 0

# 0.5ms time values for plotting (NOT TIME INTERVAL OF OSCILLIATION!)
time_values = [t*0.05 for t in range(1001)]

for t in time_values:
    displacement = int(shm(amplitude, frequency, phase, t))
    print(f'Time: {t:.3f}s {" " * (10 + displacement)}*') # The 10 is added to offset pattern for graph to fit in, instead of crashing down and not having space to move even below
    time.sleep(0.05)
