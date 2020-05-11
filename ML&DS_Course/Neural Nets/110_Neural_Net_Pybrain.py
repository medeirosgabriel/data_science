# -*- coding: utf-8 -*-
from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer, BiasUnit
from pybrain.structure import FullConnection

net = FeedForwardNetwork()

# Layers
inputLayer = LinearLayer(2) # The input values wonn't pass by a activation function. 2 is the number of neurons
holdLayer = SigmoidLayer(3)
outputLayer = SigmoidLayer(1)

# Bias
bias1 = BiasUnit()
bias2 = BiasUnit()

# Add the net pieces
net.addModule(inputLayer)
net.addModule(holdLayer)
net.addModule(outputLayer)
net.addModule(bias1)
net.addModule(bias2)

# Connections
holdInput = FullConnection(inputLayer, holdLayer)
holdOutput = FullConnection(holdLayer, outputLayer)
holdBias = FullConnection(bias1, holdLayer)
outputBias = FullConnection(bias2, outputLayer)

# Create a neural net
net.sortModules()

print(net)
print(holdInput.params)
print(holdOutput.params)
print(holdBias.params)
print(outputBias.params)

