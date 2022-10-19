# Syarifah Saskia Aulia
# 21091397012

import numpy as np

# Layer input 10 features
inputs = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 1.0]
weights = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 0.1]

# Neuron 1
bias = 3.5

outputs = np.dot(weights, inputs) + bias
print(outputs)
