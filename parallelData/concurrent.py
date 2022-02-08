import concurrent.futures

def increment(value):
    return value + 1

values = [1, 2, 3, 4, 5, 6, 7, 8]

# Add code here
with concurrent.futures.ProcessPoolExecutor() as executor:
    futures = []
    futures = [executor.submit(increment, value) for value in values]
                       
results = [future.result() for future in futures]
    
