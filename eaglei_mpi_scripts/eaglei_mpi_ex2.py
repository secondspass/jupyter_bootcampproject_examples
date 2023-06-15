import pandas as pd
import numpy as np
import time as tp
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
global_size = comm.Get_size()

df = pd.read_csv(f'./eaglei_dat/eaglei_outages/eaglei_outages_2014.csv')

#2152 total counties for year 2014
all_counties = df.fips_code.unique()
all_counties_count = len(all_counties)

local_size = all_counties_count // global_size

#This approach only works when dividing evenly/uniformly across MPI ranks
start_index = rank*local_size
end_index = (rank+1)*local_size
local_counties = all_counties[start_index:end_index]

t1=tp.time()
for i in local_counties:
    #Find the position in the CSV of a specific county (i)
    specific_county_filter = df['fips_code'] == i

    #Filter out the data so that we only look at a specific county (i)
    specific_county_data  = df[specific_county_filter]['sum']

    #Add up the total blackouts of a specific county (i)
    specific_county_sum = specific_county_data.sum()

    #Print out the data
    print(f'Total blackouts for county {i}:', specific_county_sum)
t2=tp.time()

tp.sleep(5) # just for I/O buffer
if (rank==0):
    print('Total time of script', t2-t1)

'''
Instead of printing out the data, can probably append to a new pandas dataframe (potential exercise?) (may need to do an MPI gather call, but may not)

some stats:

mpirun -np 1 python3 eaglei_mpi_ex2.py
Total time of script 1.2362239360809326
mpirun -np 2 python3 eaglei_mpi_ex2.py
Total time of script 0.6609437465667725
mpirun -np 4 python3 eaglei_mpi_ex2.py
Total time of script 0.44550299644470215
mpirun -np 8 python3 eaglei_mpi_ex2.py
Total time of script 0.359523773193359
'''
