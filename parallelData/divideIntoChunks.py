import math

def make_chunks(df, num_chunks):
    num_rows = df.shape[0]
    chunk_size = math.ceil(num_rows/num_chunks)
    chunks = [df[i:i+chunk_size] for i in range(0, num_rows, chunk_size)]
    return chunks

#skill_chunks = make_chunks(skills,8)
