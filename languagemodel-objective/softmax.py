import math
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



