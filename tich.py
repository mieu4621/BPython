from multiprocessing import Pool
from multiprocessing import Pool, pool
from unittest import result

def sum_nums(args): 
    low = int(args[0])
    high = int(args[1])
    return sum(range(low,high + 1))
def sum_matrix():
    for i in row(0,r-1):
        for j in column(0,c-1):
            for k in nmb()

if  __name__ == "__main__":   
    n = 10000
    procs = 5
    sizeSegment = n / procs

    jobs = []
    for i in range(0, procs):
        jobs.append((i*sizeSegment + 1, (i + 1)* sizeSegment))
    pool = Pool(procs).map(sum_nums, jobs)
    result = sum(pool)
    print(result)
