import math

def make_chunks(df, num_chunks):
    num_rows = df.shape[0]
    chunk_size = math.ceil(num_rows/num_chunks)
    chunks = [df[i:i+chunk_size] for i in range(0, num_rows, chunk_size)]
    return chunks

#skill_chunks = make_chunks(skills,8)

import concurrent.futures

skill_chunks = make_chunks(skills,8)

with concurrent.futures.ProcessPoolExecutor() as executor:
    futures = [executor.submit(count_skills, job_postings,skill_chunk) for skill_chunk in skill_chunks]
    
results = [future.result() for future in futures]

print(results[0])
