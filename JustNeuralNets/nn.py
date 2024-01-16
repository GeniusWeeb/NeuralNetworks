input = [1,2,3,2.5] # input to the neuron
# one bias per neuron -> we have 3 inputs for a single neuron
weight =[ [0.2,0.8,-0.5,1],[0.5,-0.91,0.26,-0.5],[-0.26,-0.27,0.17,0.87]]

bias =[2,3,0.5] 


layer_output = []


#for one neuron output,  the bias is added collectively




for nWeights,nBias in zip(weight,bias):
    nOutput = 0 
    for nInput, weight in zip(input,nWeights):
        nOutput +=nInput*weight
    # Since 1 bias per neuron we add all up the weigths* input in the neuron 
    # and then add the bias
    nOutput += nBias
    layer_output.append(nOutput)


print(layer_output)


# Dot product numpy


import numpy as np


input = [1.0,2.0,3.0,2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2.0

outputs = np.dot(weights ,input)  + bias
print(outputs)



#Layers of neurons

inputs = [1.0, 2.0, 3.0, 2.5]
weights = [[0.2, 0.8, -0.5, 1],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26 ,-0.27 ,0.17 , 0.87]]
biases = [2.0,3.0,0.5]

layer_output = np.dot(weights, input) + biases

print(layer_output)


a = [1,2,3]
b =[2,333,4]  

a  = np.array([a]) #Conver it into a matrix since its alrady in the list format , we discount the [] bracket for list
b  = np.array([b]).T #transposing to get the desired shape to perform the matrix product

print("dot is " ,np.dot(a,b))