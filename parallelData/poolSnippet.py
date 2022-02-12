#Pool Example

import os
from multiprocessing import Pool

pool = Pool(6)
values = [1, 4, 5, 2, 7, 21,     \
          31, 41, 3, 40, 5, 14,  \
          9, 32, 12, 18, 1, 30,  \
          6, 19, 23, 35, 12, 13, \
          0, 12, 42, 41, 11, 9]

chunks = make_chunks(values, 6)
print(os.cpu_count())

results = pool.map(max,chunks)
pool.close()
pool.join()

with Pool(6) as pool:
    results = pool.map(max,chunks)

# Note that after calling the `Pool.map()` method, we call the `Pool.close()` and `Pool.join()` methods. The [`Pool.close()` method](https://docs.python.org/3.8/library/multiprocessing.html?highlight=pool join#multiprocessing.pool.Pool.close) prevents the addition of new processes to the pool. We need to execute this before we can join the processes. As before, the [`Pool.join()` method](https://docs.python.org/3.8/library/multiprocessing.html?highlight=pool join#multiprocessing.pool.Pool.join) makes the main program wait for all processes to finish before continuing executing. 
'''
we have a better way of applying a function to each data chunk, we need a way to combine the results of each chunk into a global result for the original data.

For this, we can use the reduce function from the functools module. The functools.reduce() function takes two arguments:

    A reducer function.
    An iterable (a list for example) on which we want to apply the reducer function.
   
'''
import functools
values = [1, 4, 5, 2, 7, 21,     \
          31, 41, 3, 40, 5, 14,  \
          9, 32, 12, 18, 1, 30,  \
          6, 19, 23, 35, 12, 13, \
          0, 12, 42, 41, 11, 9]

max_value = functools.reduce(max,values)

