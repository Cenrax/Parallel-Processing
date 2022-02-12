import pandas as pd
job_postings = pd.read_csv("DataEngineer.csv")
job_postings["Job Description"] = job_postings["Job Description"].str.lower()
skills = pd.read_csv("Skills.csv")

# Write code here
def mapper(skill_chunk):
    frequency = {}
    for skill_name in skill_chunk["Name"]:
        frequency[skill_name] = job_postings["Job Description"].str.count(skill_name).sum()
    return frequency

def reducer(freq_chunk1, freq_chunk2):
    freq_chunk1.update(freq_chunk2)
    return freq_chunk1
    
skill_freq = map_reduce(skills, 4, mapper, reducer)
