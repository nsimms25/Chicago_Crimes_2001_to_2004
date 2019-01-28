#Nick Simms
#1/27/20129
#Import and trim Chicago_Crimes_2001_to_2004.csv to only included relevant columns to make importing to ChicagoCrimes.py quicker

import pandas as pd 
import numpy as np 

chunk_size=300000

columns = ['Date', 'Primary Type', 'Location Description', 'Beat', 'District']
crimes_2001_to_2004 = pd.read_csv('Chicago_Crimes_2001_to_2004.csv', sep=',',low_memory=False,  error_bad_lines=False, index_col='Date', infer_datetime_format=True, parse_dates=True, usecols=columns, dtype=str)

crimes_2001_to_2004.to_csv('trimmed_Chicago_crimes_2001_to_2004.csv')


#['Date', 'Primary Type', 'Location Description', 'Arrest', 'Domestic', 'Beat', 'District']
#{'Date': str, 'Primary Type': str, 'Location Description': str, 'Arrest': bool, 'Domestic': bool , 'Beat': 'Int64', 'District': 'Int64'}
