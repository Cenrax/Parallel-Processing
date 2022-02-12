#Generalized method works with list and object too

import math

def make_chunks(data, num_chunks):
    chunk_size = math.ceil(len(data)/ num_chunks)
    return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

chunks = make_chunks([1,2,3,4,5,6],3)
