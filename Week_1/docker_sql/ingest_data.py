#!/usr/bin/env python
# coding: utf-8

import argparse
import pandas as pd
from time import time
from sqlalchemy import create_engine

parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

# user, password, host, port, database name, table name,
# url of the csv 
parser.add_argument('user', help='user name for posrgres')

parser.add_argument('password', help='password for posrgres')
parser.add_argument('host', help='host for posrgres')
parser.add_argument('port', help='port for posrgres')
parser.add_argument('db', help='database name for posrgres')
parser.add_argument('table-name', help='name of the table where we will write the results to')
parser.add_argument('csv', help='url of the csv file')

args = parser.parse_args()
print(args.accumulate(args.integers))


engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

df_iter = pd.read_csv("yellow_tripdata_2021-01.csv", iterator=True, chunksize=1000000)


df=next(df_iter)



df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)



get_ipython().run_line_magic('time', "df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')")

while True:
    t_start = time()
    df = next(df_iter)
    
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    
    df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')
    
    t_end = time()
    print("inserted another chunk..., took%.3f second" % (t_end-t_start))



