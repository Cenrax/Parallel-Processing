import math

def count_skills(job_postings, skills):
    frequency = {}
    for skill_name in skills["Name"]:
        frequency[skill_name] = job_postings["Job Description"].str.count(skill_name).sum()
        
    return frequency

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
"""
d1 = {'a': 1, 'b': 2} #usage of dict.update() The way the dict.update() method works is that for each key in the dictionary provided as an argument, it will update the corresponding value in the other dictionary. If the key didn't exist, it creates a new entry.
d2 = {'c': 3, 'd': 4}
merged = {}
merged.update(d1)
merged.update(d2)
print(merged)
"""

merged_results = {}
for result in results:
    merged_results.update(result)
