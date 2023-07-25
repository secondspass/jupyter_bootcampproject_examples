import pandas as pd
from mpi4py import MPI
import time as tp

# running with 9 threads because 9 years of data, so assuming something like `mpirun -np 9 ...`
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

t1 = tp.time()
file_nums = ['2014','2015','2016','2017','2018','2019','2020','2021','2022']

df = pd.read_csv(f'../data/eaglei_outages/eaglei_outages_{file_nums[rank]}.csv')

blackouts = df['sum']
blackouts_local = blackouts.sum()

blackouts_total = comm.reduce(blackouts_local, op=MPI.SUM, root=0)

t2 = tp.time()

if rank==0:
    print('The total time of the script was:',t2-t1, 'seconds')
    print("Rank 0 got the sum, the total blackouts from 2014-2022:", int(blackouts_total))
