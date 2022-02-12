import math
import functools
from multiprocessing import Pool

data = [1, 4, 5, 2, 7, 21,     \
        31, 41, 3, 40, 5, 14,  \
        9, 32, 12, 18, 1, 30,  \
        6, 19, 23, 35, 12, 13, \
        0, 12, 42, 41, 11, 9]

num_processes = 5

def make_chunks(data, num_chunks):
    chunk_size = math.ceil(len(data)/ num_chunks)
    return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]


chunks = make_chunks(data,num_processes)

with Pool(num_processes) as pool:
    chunk_results = pool.map(max, chunks)

overall_result = functools.reduce(max,chunk_results)
