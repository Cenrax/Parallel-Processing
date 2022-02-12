#Generalized method works with list and object too

import math

def make_chunks(data, num_chunks):
    chunk_size = math.ceil(len(data)/ num_chunks)
    return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

chunks = make_chunks([1,2,3,4,5,6],3)

'''
import concurrent.futures

def map_parallel(mapper, data, num_processes):
    chunks = make_chunks(data, num_processes)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(mapper, chunk) for chunk in chunks]
    return [future.result() for future in futures]

values = [1, 4, 5, 2, 7, 21,     \
          31, 41, 3, 40, 5, 14,  \
          9, 32, 12, 18, 1, 30,  \
          6, 19, 23, 35, 12, 13, \
          0, 12, 42, 41, 11, 9]

results = map_parallel(max,values,5)
'''
