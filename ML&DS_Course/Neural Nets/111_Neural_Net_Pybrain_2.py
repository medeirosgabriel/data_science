# -*- coding: utf-8 -*-

from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import SoftmaxLayer
from pybrain.structure.modules import SigmoidLayer

# Input Layer = 2 neurons ; Hold Layer = 3 neurons ; Ouput Layer = 2 neurons

'''net = buildNetwork(2, 3, 1, outclass = SoftmaxLayer, hiddenclass = SigmoidLayer, bias = False)

print(net['in']) # Input Layer
print(net['hidden0'])
print(net['out'])
print(net['bias'])'''

net = buildNetwork(2, 3, 1)
base = SupervisedDataSet(2,1) # 2 prevision attributes and 1 class
base.addSample((0,0), (0,))
base.addSample((0,1), (1,))
base.addSample((1,0), (1,))
base.addSample((1,1), (0,))

print(base['input'])
print(base['target'])

training = BackpropTrainer(net, dataset=base, learningrate=0.01, momentum=0.06)

for i in range(1, 30000):
    error = training.train()
    if i % 1000 == 0:
        print("Erro: %s" % error)

print(net.activate([0,0]))
print(net.activate([1,0]))
print(net.activate([0,1]))
print(net.activate([1,1]))

