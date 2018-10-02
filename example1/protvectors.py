import numpy as np


def read_protvectors(path):
    """Reads a ProtVec Model
    """
    vec = {}
    with open(path,'r') as tsv:
        for line in tsv:
            # remove quotes, and split by tab
            data = line.replace('"','').replace('\n','').split('\t') 
            vec[data[0]] = np.array(data[1:], dtype=np.float64)
        
    return vec

def apply_protvectors(ngrams, protvec):
    """Applies ProtVec model to a list of ngrams
    """
    v_len = len(protvec['AAA'])
    vec = np.zeros([v_len], dtype=np.float64)

    for ng in ngrams:
        if ng in protvec:
            vec = vec + protvec[ng]
            
    vec = vec - vec.mean()
    vec = vec / vec.std()
    
    return vec

def ngrammer(s, n):
    """Splits sequence into n-grams

    Parameters:
       s (string): sequence of amino acid
       n (int): number of character in n-gram
    """
    ngram = []                                                                                
    i = 0                                                                                     
    if len(s) < 1:                                                                            
        return []                                                                             
    while i < len(s) - n + 1:                                                                 
        ngram.append(s[i: i + n])                                                             
        i += 1

    return ngram
