def process_corpus(words):
    corpus=[]

    for word in words:
        char=[]
        for chars in word:
            char.append(chars)
        corpus.append(char)
    return corpus


def get_pair_frequencies(corpus):
    pair_freq={}
    for word in corpus:
        for i in range(len(word)-1):
            pair=(word[i],word[i+1])
            if pair in pair_freq:
                pair_freq[pair]+=1
            else:
                pair_freq[pair]=1 
    return pair_freq           


def getmostfreq_pair(pair_freq):
    best_pair=None
    best_freq=-1            #any real freq would replace it
    for pair in pair_freq.items():
        if pair_freq[pair]>best_freq:
            best_freq=pair_freq[pair]
            best_pair=pair
    return best_pair

def merge_tokens(words,pair):
    new_corpus=[]

    for word in words:
        new_word= []
        i=0

        while i <= len(word)-1:
            if (word[i],word[i+1])==(pair):
                new_word.append(word[i],word[i+1])
                i+=2
            else:
                new_corpus.append(word[i])
                i+=1
        new_corpus.append(new_word)
    return  new_corpus
            