#! /usr/bin/env python3
"""
This script makes lapd datasets for the time-series-arima assignment.

LAPD data comes from `Los Angeles Open Data`_.

This script can also be imported as a module with functions that
separately create each dataset.

.. _Los Angeles Open Data: https://data.lacity.org/browse?tags=911

Usage:
    make_lapd.py [-h] [--dir_data] [--dir_out]

Authors:
    Kin-Yip Chien <kin-yip.chien@galvanize.com>

Functions:
    make_lapd : Return a DataFrame of LAPD calls for service.
    main : Encapsulates logic for running `make_lapd.py` as a script.
"""
import argparse
from datetime import datetime
import pandas as pd
from pathlib import Path
import re
from make_data_helpers import make_filepath
from time_series_arima import load_series


def make_lapd(filedir: str = '') -> 'pandas.core.frame.DataFrame':
    """
    Return a DataFrame of LAPD calls for service.

    Clean and concatenate yearly files.

    Parameters
    ----------
    filedir : str, default=''

    Returns
    -------
    lapd : pandas DataFrame
        Merged LAPD calls for service.
    """
    filepattern = 'LAPD_Calls_for_Service_[2-9][0-9][0-9][0-9].zip'
    filepath = make_filepath(filepattern, filedir)
    prog = re.compile(r'^.*?LAPD_Calls_for_Service_(\d{4})\.[a-zA-Z0-9]+$')
    
    dfs = []
    for file in Path.cwd().glob(filepath):
        df = pd.read_csv(Path(file))

        result = prog.match(file.as_posix())
        year = int(result[1])
        if year < 2018:
            df.rename(
                columns={'Incident Number': 'Incident_Number',
                         'Reporting District': 'Rpt_Dist',
                         'Area Occurred': 'Area_Occ',
                         'Dispatch Date': 'Dispatch_Date',
                         'Dispatch Time': 'Dispatch_Time',
                         'Call Type Code': 'Call_Type_Code',
                         'Call Type Description': 'Call_Type_Text'},
                inplace=True)
        if year == 2020:
            df.drop_duplicates(inplace=True)

        df['Dispatch_Date'] = df['Dispatch_Date'].str.extract(
            '^(\d{2}\/\d{2}\/\d{4})')[0]
        df['Dispatch_Date_Time'] = df['Dispatch_Date'].str.cat(
            df['Dispatch_Time'], sep=' ')
        df['Dispatch_Date_Time'] = pd.to_datetime(
            df['Dispatch_Date_Time'], format='%m/%d/%Y %H:%M:%S')

        df.drop(columns=['Incident_Number', 'Dispatch_Date', 'Dispatch_Time'],
                inplace=True)
        dfs.append(df)

    lapd = pd.concat(dfs)
    return lapd


def main(dir_data: str = '', dir_out: str = '') -> None:
    """
    Encapsulates logic for running `make_data.py` as a script.

    Parameters
    ----------
    dir_data : str, default=''
        Directory containing data files.
    dir_out : str, default=''
        Directory to write data files.

    Returns
    -------
    None
    """
    if dir_out:
        # filedir must end with a forward-slash.
        if dir_out[-1] != '/':
            dir_out += '/'
        if not Path(dir_out).is_dir():
            Path.mkdir(Path(dir_out))

    now = datetime.now().strftime('%Y-%m-%dT%H%M%S')
    lapd = make_lapd(dir_data)
    file = dir_out + f'lapd_{now}.csv'
    lapd.to_csv(file, index=False)
    print(f'data written to {file}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--dir_data', default='',
        help='directory containing data files')
    parser.add_argument(
        '--dir_out', default='',
        help='directory to write data files')
    args = parser.parse_args()
    main(args.dir_data, args.dir_out)