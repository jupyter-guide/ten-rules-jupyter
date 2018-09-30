import numpy as np
from sklearn.preprocessing import normalize

def ngrammer(s,n):
    '''split sequence into n-grams
    
    Attributes:
       s (string): sequence of amino acid
       n (int): number of character in n-gram
    '''
    ngram = []                                                                                
    i = 0                                                                                     
    if len(s) < 1:                                                                            
        return []                                                                             
    while i < len(s) - n + 1:                                                                 
        ngram.append(s[i: i + n])                                                             
        i += 1                                                                                
    return ngram

def average_word_vec(ngrams, word_vec):
    ave_vec = np.zeros(word_vec.vector_size)
    count = 0
    
    for ng in ngrams:
        try:
            ave_vec = ave_vec + word_vec.word_vec(ng)
            count = count + 1
        except:
            pass
            

    ave_vec = ave_vec/count
    
    return ave_vec

def average_word_vec_scaled(ngrams, word_vec):
    vec = np.zeros(word_vec.vector_size)
    
    for ng in ngrams:
        try:
            vec = vec + word_vec.word_vec(ng)
        except:
            pass
            
    vec = vec - vec.mean()
    vec = vec / vec.std()
    
    return vec


