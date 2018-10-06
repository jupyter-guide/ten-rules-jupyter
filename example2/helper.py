#!/usr/bin/env python3
'''
Helper functions for Example 2: "Simulate Phylogenetic Trees and Sequences"
'''
from math import log

def read_FASTA(filename):
    '''
    Given the name of a FASTA file, parse the contents of the FASTA file and return a dictionary in which keys are identifiers and values are sequences.
    '''
    seqs = {}
    name = None
    seq = ''
    f = open(filename)
    for line in f:
        l = line.strip()
        if len(l) == 0:
            continue
        if l[0] == '>':
            if name is not None:
                assert len(seq) != 0, "Malformed FASTA"
                seqs[name] = seq
            name = l[1:]
            assert name not in seqs, "Duplicate sequence ID: %s" % name
            seq = ''
        else:
            seq += l
    f.close()
    assert name is not None and len(seq) != 0, "Malformed FASTA"
    seqs[name] = seq
    return seqs

def distance_matrix_to_list(dm):
    '''
    Convert an n-by-n pairwise distance matrix (dictionary of dictionaries) into a list of n(n-1)/2 pairwise distances. Sorts keys in ascending order.
    '''
    keys = sorted(dm.keys())
    return [dm[keys[i]][keys[j]] for i in range(len(keys)-1) for j in range(i+1,len(keys))]

def hamming(u,v):
    '''
    Given a pair of sequences u and v with equal lengths, compute the Hamming distance between u and v (as a proportion, not a count).
    '''
    return sum(u[i] != v[i] for i in range(len(u)))/float(len(u))

def compute_hamming_distance_matrix(sequences):
    '''
    Given a dictionary of n sequences in which keys are identifiers and values are sequences, return an n-by-n pairwise distance matrix (dictionary of dictionaries) of Hamming distances.
    '''
    return {u:{v:hamming(sequences[u],sequences[v]) for v in sequences} for u in sequences}

def jc69_correction(h):
    '''
    Given a Hamming distance h, compute the corresponding JC69-corrected phylogenetic distance.
    '''
    return -3*log(1-(4*h/3))/4

def compute_jc69_corrected_distance_matrix(sequences):
    '''
    Given a dictionary of n sequences in which keys are identifiers and values are sequences, return an n-by-n pairwise distance matrix (dictionary of dictionaries) of JC69-corrected distances.
    '''
    hamming_distances = compute_hamming_distance_matrix(sequences)
    return {u:{v:jc69_correction(hamming_distances[u][v]) for v in sequences} for u in sequences}
