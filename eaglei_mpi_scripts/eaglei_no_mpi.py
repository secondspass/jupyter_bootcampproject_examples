import pandas as pd
import time as tp

t1=tp.time()
file_nums = ['2014','2015','2016','2017','2018','2019','2020','2021','2022']

blackouts_total = 0
for i in file_nums:
    df = pd.read_csv(f'../data/eaglei_outages/eaglei_outages_{i}.csv')

    blackouts = df['sum']
    blackouts_local = blackouts.sum()

    blackouts_total+=blackouts_local

    print('Done with year', i)

t2 = tp.time()

print('The total time of the script was:',t2-t1, 'seconds')
print('The total blackouts from 2014-2022:', blackouts_total)

