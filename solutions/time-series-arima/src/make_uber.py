#! /usr/bin/env python3
"""
This script makes uber datasets for the time-series-arima assignment.

Uber data comes from `FiveThirtyEight`_.  

This script can also be imported as a module with functions that
separately create each dataset.

.. _FiveThirtyEight: https://github.com/fivethirtyeight/uber-tlc-foil-response/tree/master/uber-trip-data

Usage:
    make_uber.py [-h] [--dir_in] [--dir_out]

Authors:
    Kin-Yip Chien <kin-yip.chien@galvanize.com>

Functions:
    make_aprsep14 : Return a Series of Uber pickup dates and times.
    make_janjun15 : Return a Series of Uber pickup dates and times.
    main : Encapsulates logic for running `make_uber.py` as a script.
"""
import argparse
from datetime import datetime
import pandas as pd
from pathlib import Path
from make_data_helpers import make_filepath


def make_aprsep14(filedir: str = '') -> 'pandas.core.series.Series':
    """
    Return a Series of Uber pickup dates and times.

    Concatenate monthly files and keep date and time column.

    Parameters
    ----------
    filedir : str, default=''
        Directory containing monthly files.

    Returns
    -------
    uber : pandas Series
        Uber pickup dates and times.
    """
    filepattern = 'uber-raw-data-{}.csv'
    filepath = make_filepath(filepattern, filedir)

    ss = []
    for month in ['apr14', 'may14', 'jun14', 'jul14', 'aug14', 'sep14']:
        s = pd.read_csv(
            Path(filepath.format(month)),
            usecols=['Date/Time'], squeeze=True)
        s.rename('date', inplace=True)
        ss.append(s)
    uber = pd.concat(ss)

    uber = pd.to_datetime(uber, format='%m/%d/%Y %H:%M:%S')
    return uber


def make_janjun15(file: str = 'uber-raw-data-janjune-15.csv.zip',
                  filedir: str = ''
) -> 'pandas.core.series.Series':
    """
    Return a Series of Uber pickup dates and times.

    Load file and keep date and time column.

    Parameters
    ----------
    file : str, default='uber-raw-data-janjune-15.csv'
        Data file name.
    filedir : str, default=''
        Directory containing data file.

    Returns
    -------
    uber : pandas Series
        Uber pickup dates and times.
    """
    filepath = make_filepath(file, filedir)
    uber = pd.read_csv(
        Path(filepath), usecols=['Pickup_date'], squeeze=True)
    uber.rename('date', inplace=True)
    uber = pd.to_datetime(uber, format='%Y-%m-%d %H:%M:%S')
    return uber


def main(dir_in: str = '', dir_out: str = '') -> None:
    """
    Encapsulates logic for running `make_uber.py` as a script.

    Parameters
    ----------
    dir_in : str, default=''
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
    aprsep14 = make_aprsep14(dir_in)
    file = dir_out + f'uber-aprsep-14_{now}.csv'
    aprsep14.to_csv(file, index=False)
    print(f'data written to {file}')

    now = datetime.now().strftime('%Y-%m-%dT%H%M%S')
    janjun15 = make_janjun15(filedir=dir_in)
    file = dir_out + f'uber-janjun-15_{now}.csv'
    janjun15.to_csv(file, index=False)
    print(f'data written to {file}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--dir_in', default=None,
        help='directory containing data files')
    parser.add_argument(
        '--dir_out', default=None,
        help='directory to write data files')
    args = parser.parse_args()
    main(args.dir_in, args.dir_out)