# Importing libraries
import pandas as pd
import numpy as np
import math
import operator
from sklearn import preprocessing

#### Start of STEP 1
# Importing data 
data = pd.read_csv('data.csv')
#cols_to_norm = ["tempo", "chroma_stft", "rmse", "spectral_centroid",
#                "spectral_bandwidth", "rolloff", "zero_crossing_rate"]
#data[cols_to_norm] = data[cols_to_norm].apply(lambda x: (x - x.min()) / (x.max() - x.min()))

data.head()
#### End of STEP 1

print(data.head(5)) 

# Defining a function which calculates euclidean distance between two data points
def euclideanDistance(data1, data2, length):
    distance = 0
    distance += ((1/7)*np.square(data1[0] - data2[0]))
    distance += ((1/5)*np.square(data1[1] - data2[1]))
    distance += ((1/4)*np.square(data1[2] - data2[2]))
    distance += ((1/2)*np.square(data1[3] - data2[3]))
    distance += ((1/3)*np.square(data1[4] - data2[4]))
    distance += np.square(data1[5] - data2[5])
    distance += ((1/6)*np.square(data1[6] - data2[6]))
    return np.sqrt(distance)

def manhattanDistance(data1, data2, length):
    distance = 0
    distance += ((1/7)*(data1[0] - data2[0]))
    distance += ((1/5)*(data1[1] - data2[1]))
    distance += ((1/4)*(data1[2] - data2[2]))
    distance += ((1/2)*(data1[3] - data2[3]))
    distance += ((1/3)*(data1[4] - data2[4]))
    distance += (data1[5] - data2[5])
    distance += ((1/6)*(data1[6] - data2[6]))
    return distance

def L3Distance(data1, data2, length):
    distance = 0
    distance += ((1/7)*np.power(data1[0] - data2[0], 3))
    distance += ((1/5)*np.power(data1[1] - data2[1], 3))
    distance += ((1/4)*np.power(data1[2] - data2[2], 3))
    distance += ((1/2)*np.power(data1[3] - data2[3], 3))
    distance += ((1/3)*np.power(data1[4] - data2[4], 3))
    distance += np.power(data1[5] - data2[5], 3)
    distance += ((1/6)*np.power(data1[6] - data2[6], 3))
    return np.cbrt(distance)

# Defining our KNN model
def knn(trainingSet, testInstance, k):
 
    distances = {}
    sort = {}
 
    length = testInstance.shape[1]
    
    #### Start of STEP 3
    # Calculating euclidean distance between each row of training data and test data
    for x in range(len(trainingSet)):
        
        #### Start of STEP 3.1
        dist = euclideanDistance(testInstance, trainingSet.iloc[x], length)

        distances[x] = dist[0]
        #### End of STEP 3.1
 
    #### Start of STEP 3.2
    # Sorting them on the basis of distance
    sorted_d = sorted(distances.items(), key=operator.itemgetter(1))
    #### End of STEP 3.2
 
    neighbors = []
    
    #### Start of STEP 3.3
    # Extracting top k neighbors
    for x in range(k):
        neighbors.append(sorted_d[x][0])
    #### End of STEP 3.3
    classVotes = {}
    
    #### Start of STEP 3.4
    # Calculating the most freq class in the neighbors
    for x in range(len(neighbors)):
        response = trainingSet.iloc[neighbors[x]][-1]
 
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    #### End of STEP 3.4

    #### Start of STEP 3.5
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return(sortedVotes[0][0], neighbors)
    #### End of STEP 3.5

def knnManhattan(trainingSet, testInstance, k):
 
    distances = {}
    sort = {}
 
    length = testInstance.shape[1]
    
    #### Start of STEP 3
    # Calculating euclidean distance between each row of training data and test data
    for x in range(len(trainingSet)):
        
        #### Start of STEP 3.1
        dist = manhattanDistance(testInstance, trainingSet.iloc[x], length)

        distances[x] = dist[0]
        #### End of STEP 3.1
 
    #### Start of STEP 3.2
    # Sorting them on the basis of distance
    sorted_d = sorted(distances.items(), key=operator.itemgetter(1))
    #### End of STEP 3.2
 
    neighbors = []
    
    #### Start of STEP 3.3
    # Extracting top k neighbors
    for x in range(k):
        neighbors.append(sorted_d[x][0])
    #### End of STEP 3.3
    classVotes = {}
    
    #### Start of STEP 3.4
    # Calculating the most freq class in the neighbors
    for x in range(len(neighbors)):
        response = trainingSet.iloc[neighbors[x]][-1]
 
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    #### End of STEP 3.4

    #### Start of STEP 3.5
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return(sortedVotes[0][0], neighbors)
    #### End of STEP 3.5

def knnL3(trainingSet, testInstance, k):
 
    distances = {}
    sort = {}
 
    length = testInstance.shape[1]
    
    #### Start of STEP 3
    # Calculating euclidean distance between each row of training data and test data
    for x in range(len(trainingSet)):
        
        #### Start of STEP 3.1
        dist = L3Distance(testInstance, trainingSet.iloc[x], length)
        distances[x] = dist[0]
        #### End of STEP 3.1
 
    #### Start of STEP 3.2
    # Sorting them on the basis of distance
    sorted_d = sorted(distances.items(), key=operator.itemgetter(1))
    #### End of STEP 3.2
 
    neighbors = []
    
    #### Start of STEP 3.3
    # Extracting top k neighbors
    for x in range(k):
        neighbors.append(sorted_d[x][0])
    #### End of STEP 3.3
    classVotes = {}
    
    #### Start of STEP 3.4
    # Calculating the most freq class in the neighbors
    for x in range(len(neighbors)):
        response = trainingSet.iloc[neighbors[x]][-1]
 
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    #### End of STEP 3.4

    #### Start of STEP 3.5
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return(sortedVotes[0][0], neighbors)
    #### End of STEP 3.5

#Using Metallica's "Master of Puppets"
testSet = [[103.36, 0.4437584, 0.12677296, 3010.24250384984, 2568.44524729123,
            5886.24836990299, 0.146207405879769]]
#testSet = preprocessing.normalize(testSet)
test = pd.DataFrame(testSet)

#### Start of STEP 2
# Setting number of neighbors = 10


print('\n\nWith 10 Nearest Neighbours \n\n')
k = 10
#### End of STEP 2
# Running KNN model
result,neigh = knn(data, test, k)

resultManhattan, neighManhattan = knnManhattan(data, test, k)

resultL3, neighL3 = knnL3(data, test, k)

# Predicted class
print('\nPredicted Class of the datapoint (Euclidean) = ', result)

print('\nPredicted Class of the datapoint (Manhattan) = ', resultManhattan)

print('\nPredicted Class of the datapoint (L3) = ', resultL3)

# Nearest neighbor
print('\nNearest Neighbour of the datapoints (Euclidean) = ',neigh)

print('\nNearest Neighbour of the datapoints (Manhattan) = ', neighManhattan)

print('\nNearest Neighbour of the datapoints (L3) = ', neighL3)
