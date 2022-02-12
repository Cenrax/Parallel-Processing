#MAP REDUCE WITH JOB POSTINGS AS CHUNK. FOR EACH CHUNK WE WILL GET THE JOB POSTINGS
import pandas as pd
job_postings = pd.read_csv("DataEngineer.csv")
job_postings["Job Description"] = job_postings["Job Description"].str.lower()
skills = pd.read_csv("Skills.csv")

# Write code here
def mapper(jobs_chunk):
    frequency = {}
    for skill_name in skills["Name"]:
        frequency[skill_name] = jobs_chunk["Job Description"].str.count(skill_name).sum()
    return frequency

def reducer(freq_chunk1, freq_chunk2):
    merged = {}
    for skill in freq_chunk1:
        merged[skill] = freq_chunk1[skill] + freq_chunk2[skill]
    return merged
    
skill_freq = map_reduce(job_postings, 4, mapper, reducer)
