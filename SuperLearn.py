from pylab import zeros, sin, cos, normal, random
from Tilecoder import numTilings, tilecode

#n =
# initialize weights appropriately here
theta =     [0.0]*968
alpha =     0.1 / 8# initialize step size parameter appropriately here
tileIndices = [-1]*numTilings # initialize your list of tile indices here

def f(in1,in2):
    # write your linear function approximator here (5 lines or so)
    tileIndices = [-1]*numTilings # initialize your list of tile indices here
    tilecode(in1,in2,tileIndices)
    rValue = 0
    for indicie in tileIndices:
        rValue+=theta[indicie]
        
    return rValue
        
    
def learn(in1,in2,target):
    # write your gradient descent learning algorithm here (3 lines or so)
    tileIndices = [-1]*numTilings # initialize your list of tile indices here
    tilecode(in1,in2,tileIndices)
    estimate = f(in1, in2)
    for indicie in tileIndices:
        theta[indicie]+= alpha * (target - estimate)
        
    
def targetFunction(in1, in2):
    return sin(in1 - 3.0) * cos(in2) + normal(0, 0.1)

def train(numSteps):
    for i in range(numSteps):
        in1 = random() * 6.0
        in2 = random() * 6.0
        target = targetFunction(in1, in2)
        learn(in1, in2, target)
    
def writeF(filename):
    fout = open(filename, 'w')
    steps = 50
    for i in range(steps):
        for j in range(steps):
            target = f(i * 6.0 / steps, j * 6.0 / steps)
            fout.write(repr(target) + ' ')
        fout.write('\n')
    fout.close()
        
def MSE(sampleSize):
    totalSE = 0.0
    for i in range(sampleSize):
        in1 = random() * 6.0
        in2 = random() * 6.0
        error = targetFunction(in1, in2) - f(in1, in2)
        totalSE = totalSE + error * error
    #print('The estimated MSE: ', (totalSE / sampleSize))
    
def test2():
    train(20)
    writeF('f20')
    MSE(10000)
    for i in range(10):
        train(1000)
        MSE(10000)
    writeF('f10000')


if __name__ == '__main__':
    test1()
