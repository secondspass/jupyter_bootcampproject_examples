import pandas as pd
import numpy as np
import time as tp
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
global_size = comm.Get_size()

df = pd.read_csv(f'../data/eaglei_outages/eaglei_outages_2014.csv')

#2152 total counties for year 2014
all_counties = df.fips_code.unique()
all_counties_count = len(all_counties)

local_size = all_counties_count // global_size

#This approach only works when dividing evenly/uniformly across MPI ranks
start_index = rank*local_size
end_index = (rank+1)*local_size
local_counties = all_counties[start_index:end_index]

t1=tp.time()

counties = []
sums = []

for i in local_counties:
    #Find the position in the CSV of a specific county (i)
    specific_county_filter = df['fips_code'] == i

    #Filter out the data so that we only look at a specific county (i)
    specific_county_data  = df[specific_county_filter]['sum']

    #Add up the total blackouts of a specific county (i)
    specific_county_sum = specific_county_data.sum()

    #Print out the data
    counties.append(int(i))
    sums.append(int(specific_county_sum))
    

d = {'FIPS Code': counties, 'Blackout Sum' : sums}
blackouts_df = pd.DataFrame(data=d) 
blackouts_df.to_csv('county_blackouts.csv', index=False)

t2=tp.time()

tp.sleep(5) # just for I/O buffer
if (rank==0):
    print('Total time of script', t2-t1)