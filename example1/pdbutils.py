import gzip
import pandas as pd


def read_secondary_structure(file_name):
    """Reads a FASTA-formatted file with DSSP secondary structure info.
    """
    # unzip the gziped file, convert byte string to string, remove bytes character
    # and quotation mark, and store result in a list
    raw_text = [str(line)[2:-1] for line in gzip.open(file_name,'rb')]

    # get line number of lines with structure chain ID (starts with '>)
    line_numbers = [i for i,n in enumerate(raw_text) if n[0] == '>']

    # get the structure chain id from the from every 3 lines in the list of 
    # line numbers (the same structurechainId repreats 3times)
    structures = ['.'.join(raw_text[line].split(":")[:2])[1:] for line in line_numbers[::3]]   

    # function to join lines of string into a single string and remove new line characters
    def parse_input(x): return ''.join(x).replace("\\n","")

    # data parsed into format: [structureChainId, amino acid sequence, secondary structure]
    # missing secondary structure labeled as coil
    structure_sequence = [[s,parse_input(raw_text[a+1:b]),parse_input(raw_text[b+1:c]).replace(' ','C')] for s,a,b,c in zip(structures, *[iter(line_numbers)]*3)]
    
    dic = {'pdbChainId': [s[0] for s in structure_sequence],
           'sequence': [s[1] for s in structure_sequence],
           'secondary_structure': [s[2] for s in structure_sequence]                            
          }
    
    return pd.DataFrame(dic)

def read_pisces_representatives(file_name):
    """Reads a PISCES file of representative protein chains.   
    """
    rep = pd.read_csv(file_name, delim_whitespace=True)
    
    # standardize representation of chain ids: <pdbId>.<chainId>
    rep['pdbChainId'] = rep['IDs'].apply(lambda s: s[:4] + '.' + s[4:])
    rep = rep.drop('IDs', axis=1)
    
    return rep

 