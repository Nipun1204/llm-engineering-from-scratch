import math
max_logit=0
total=0
loss=0
def softmax(logits:list):
    prob=[]
    n=len(logits)
    max_logit=logits[0]
    for i in range(n): 
        if logits[i]>=max_logit:
            max_logit=logits[i]

    for i in range(n):
        logits[i]=logits[i]-max_logit
        
        prob.append(math.exp(logits[i]))

    total=sum(prob)
    for i in range(n):
     
        prob[i]=prob[i]/total
    
    return prob        


def crossentrophy(prob,target):
    n=len(prob)
    loss=-(math.log(prob[target]))
    return loss