import pandas as pd
import numpy as np
import time as tp

df = pd.read_csv(f'./eaglei_dat/eaglei_outages/eaglei_outages_2014.csv')

all_counties = df.fips_code.unique()

t1=tp.time()
for i in all_counties:
    #Find the position in the CSV of a specific county (i)
    specific_county_filter = df['fips_code'] == i

    #Filter out the data so that we only look at a specific county (i)
    specific_county_data  = df[specific_county_filter]['sum']

    #Add up the total blackouts of a specific county (i)
    specific_county_sum = specific_county_data.sum()

    #Print out the data (can probably make this append to a new pandas dataframe instead of printing -- potential exercise)
    counties.append(int(i))
    sums.append(int(specific_county_sum))
    

d = {'FIPS Code': counties, 'Blackout Sum' : sums}
blackouts_df = pd.DataFrame(data=d) 
blackouts_df.to_csv('county_blackouts.csv', index=False)

t2=tp.time()

print('Total time of script', t2-t1)
