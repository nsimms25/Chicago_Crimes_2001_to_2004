import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dict_of_crimes = {}
type_of_crime = []
number_of_crime = []
loc_of_crimes = {}
index_list = []
number_of_crimes = []
total_crimes = 0

#Read in the CSV file, indicate separator is comma and skip any lines with errors (line 1513591 has error).
#Load file in 1,000,000 lines at a time
chunk_size = 1000000
section_number = 0
for crimes_2001_to_2004 in pd.read_csv('trimmed_Chicago_crimes_2001_to_2004.csv', sep=',', chunksize=chunk_size, error_bad_lines=False, index_col='Date', low_memory=False):
    section_number += 1
    print('Load in Section: ', section_number)
    #Force index to be datetime format.
    #crimes_2001_to_2004.index = pd.to_datetime(crimes_2001_to_2004.index)

    #Count the number of crimes.
    for i in range(len(crimes_2001_to_2004)):
        #Slice dataframe by row.
        row = crimes_2001_to_2004.iloc[i]
        #Find the crime type that is reported.
        s = row['Primary Type']
        #Create dict entry and initialize or increase count.
        if s in dict_of_crimes:
            dict_of_crimes[s] += 1
        else:
            dict_of_crimes[s] = 1

    #print(dict_of_crimes)
    
    for k, v in dict_of_crimes.items():
        type_of_crime.append(k)
        number_of_crime.append(v)

    #Create ordered list of crimes.
    ordered_amount_of_crimes = pd.DataFrame(number_of_crime, index=type_of_crime)
    ordered_amount_of_crimes.columns = ['Number of Crimes']
    ordered_amount_of_crimes.sort_values('Number of Crimes', ascending=False, inplace=True, axis=0)
    #print(ordered_amount_of_crimes)

    #Where do crimes most occur?
    for i in range(len(crimes_2001_to_2004)):
        row = crimes_2001_to_2004.iloc[i]
        place = row['Location Description']
        if place in loc_of_crimes:
            loc_of_crimes[place] += 1
        else:
            loc_of_crimes[place] = 1

    for k, v in loc_of_crimes.items():
        index_list.append(k)
        number_of_crimes.append(v)

    #Create a DataFrame of sorted values.
    sorted_loc_of_crimes = pd.DataFrame(number_of_crimes, index=index_list)
    sorted_loc_of_crimes.columns = ['Location of Crimes']
    sorted_loc_of_crimes.sort_values('Location of Crimes', ascending=False, inplace=True, axis=0)

#get total crimes
total_crimes = ordered_amount_of_crimes['Number of Crimes'].sum()

#Find the breakdown in percentage for each crime.
ordered_amount_of_crimes['Percentage of Crime'] = ordered_amount_of_crimes['Number of Crimes'] / total_crimes * 100

print('Total number of crimes commited 2001 to 2004: ', total_crimes)
print('Crime breakdown: \n', ordered_amount_of_crimes)
print('Location of crimes: \n', sorted_loc_of_crimes)
