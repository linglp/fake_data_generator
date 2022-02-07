import pandas as pd 
import numpy as np
import time
import random
from re import search


def generate_random_dates(min_date, max_date, size):
    #create an empty pandas dataframe
    df_bucket=pd.DataFrame()

    min_date = pd.to_datetime(min_date)
    max_date = pd.to_datetime(max_date)
    #calculate the total number of days between max date and min date
    d = (max_date - min_date).days + 1
    #add that to your min date
    df_bucket['dates'] = min_date + pd.to_timedelta(np.random.randint(d,size=100), unit='d')

    #return a list of random dates
    random_dates_lst = df_bucket['dates'].to_list()
    
    return random_dates_lst


def generate_random_sites(size):
    group_of_sites = ['Sutter Health','University of Michigan','University of Minnesota','Baylor Scott and White Research Institute', 'Massachusetts General','Stanford','Weill Cornell','Loma Linda','Advanced Care Planning','Advanced Illness Management Service']
    lst_random_sites=random.choices(group_of_sites, k=size)
    return lst_random_sites


def generate_fake_data(dataframe):
    empty_dict={}
    lst_dummy = []
    for index, row in dataframe.iterrows():
        #print(row['column'], row['type'])
        fieldname = row['column']
        datatype = row['type']
        options = row['options']

        ####random integer for patient id
        if datatype =='integer':
            empty_dict[fieldname]=list(range(1, 301))
        
        #### random dates
        elif datatype == 'date':
            empty_dict[fieldname] = generate_random_dates('1960-01-01', '2000-12-01', 300)
        
        #### dummy  
        elif datatype == "dummy":
            empty_dict[fieldname]=random.choices(range(2), k=300)

        #### answer value 
        elif datatype.lower() == "answervalue":
            options_new = options.replace(" ","")
            opt_lst = options_new.split(',')
            opt_lst_int = [int(i) for i in opt_lst]
            empty_dict[fieldname]=random.choices(opt_lst_int, k=300)

        #### categorical variables
        elif datatype.lower() == "categorical":
            opt_lst_cat = options.split(',')
            empty_dict[fieldname]=random.choices(opt_lst_cat, k=300)

        #### float range
        elif datatype.lower() == "float_range":
            options_range = options.replace(" ","")
            opt_lst = options_new.split(',')
            opt_lst_int = [int(i) for i in opt_lst]

            ##create sample
            empty_dict[fieldname]  = np.random.uniform(low=opt_lst_int[0], high=opt_lst_int[-1], size=(300))
        
        #### integer range
        elif datatype.lower() == "integer_range":
        # similar to answer value: 
            options_range = options.replace(" ","")
            opt_lst = options_range.split(',')
            opt_lst_int = [int(i) for i in opt_lst]
            empty_dict[fieldname]  = np.random.randint(low=opt_lst_int[0], high=opt_lst_int[-1], size=(300))
  
        #return everything back to a dataframe
        final_df = pd.DataFrame.from_dict(empty_dict,orient='index').transpose()

    return final_df
