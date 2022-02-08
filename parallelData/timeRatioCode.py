import pandas as pd
job_postings = pd.read_csv('DataEngineer.csv')
skills = pd.read_csv('Skills.csv')
"""
frequency = {}
frequency["postgres"]=job_postings["Job Description"].str.lower().str.count("postgres").sum()
"""

frequency["sql"]=job_postings["Job Description"].str.lower().str.count("sql").sum()
def count_skills(job_postings, skills):
    frequency = {}
    for skill_name in skills["Name"]:
        frequency[skill_name] = job_postings["Job Description"].str.count(skill_name).sum()
    return frequency

def count_skills_parallel(job_postings, skills, num_processes=4):
    # Calculate results using paralleld processing
    skill_chunks = make_chunks(skills, num_processes)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(count_skills, job_postings, skill_chunk) for skill_chunk in skill_chunks]
    results = [future.result() for future in futures]
    # Merge results
    merged_results = {}
    for result in results:
        merged_results.update(result)
    return merged_results

import time

start = time.time()
count_skills(job_postings, skills)
end = time.time()
time_normal = end - start

start = time.time()
count_skills_parallel(job_postings, skills)
end = time.time()
time_parallel = end - start

print(time_normal / time_parallel)

# Measure execution times here
