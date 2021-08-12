import numpy as np
import pandas as pd
import re
from bs4 import BeautifulSoup

def clean_data(data:pd.DataFrame) -> pd.DataFrame:
    """Cleaner for UFO DataFrame"""
    # Copy data to avoid collision
    df_copy = data.copy()
    
    
    # Rename ID Column for Clarity
    df_copy.columns.values[0] = 'ID'
    
    # Convert Time to DateTime Object
    df_copy['time'] = pd.to_datetime(df_copy['time'])
    
    # Parse data from HTML Column
    df_copy['state'] = None
    df_copy['content'] = None
    df_copy['shape'] = None
    for i in range(len(df_copy)):
        soup = BeautifulSoup(df_copy['html'][i], 'html.parser')
        meta_data = soup.find_all('tbody')[0].find_all('tr')[0]
        s = meta_data.get_text('|', strip=True).split("|")
        # store data into a dictionary
        s_dict = {x.partition(":")[0]:x.partition(":")[-1] for x in s}
        state = s_dict['Location'][-2:]
        df_copy.loc[i, 'state'] = state
        entry = soup.find_all('tbody')[0].find_all('tr')[1]
        df_copy.loc[i, 'content'] = entry.get_text(strip=True)
        duration = s_dict['Duration']
        df_copy.loc[i, 'duration'] = duration
        shape = s_dict['Shape']
        df_copy.loc[i, 'shape'] = shape
    
    
    return df_copy