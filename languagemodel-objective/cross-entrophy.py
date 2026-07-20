import math
from softmax import softmax
logits=[1,4,6,8,3]

def crossentrophy(prob,target):
    n=len(prob)
    loss=-(math.log(prob[target]))
    return loss


prob=softmax(logits)
print(crossentrophy(prob,2))