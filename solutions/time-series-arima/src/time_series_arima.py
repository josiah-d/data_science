#! /usr/bin/env python3
"""
This script produces the seasonal subseries plots in time-series-arima
assignment.

This script can also be imported as a module with functions that
separately create each plot.

Usage:
    time_series_arima.py [-h] [--dir_out] file_in

Authors:
    Kin-Yip Chien <kin-yip.chien@galvanize.com>

Functions:
    load_rides : Load uber dataset of pickup dates and times
        (forecasting).
    plot_hourly_subseries : Plot seasonal subseries for hourly rides
        data.
    plot_daily_subseries : Plot seasonal subseries for daily rides
        data.
    main : Encapsulates logic for running `time_series_arima.py` as a script.
"""
# TODO: plot functions only work with 2014 data.
import argparse
from datetime import datetime
import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd
from typing import Tuple


def load_series(filepath:str) -> 'pandas.core.series.Series':
    """
    Load dataset of occurrence dates and times (forecasting).

    Parameters
    ----------
    filepath : str
        Path of data file.

    Returns
    -------
    data : pandas Series
        Occurrence dates and times.
    """
    data = pd.read_csv(
        Path(filepath), squeeze=True, parse_dates=['date'])
    data = pd.Series(1, index=data)
    return data


def plot_hourly_subseries(
    filepath:str, figsize: Tuple[float, float] = (16, 9),
    tight_layout: bool = True
) -> Tuple['matplotlib.figure.Figure', 'matplotlib.axes.Axes']:
    """
    Plot seasonal subseries for hourly rides data.

    Parameters
    ----------
    filepath : str, default='../data/taxi.csv'
        String path of csv file.
    figsize : 2-tuple of floats, default=(16, 9)
        Figure dimension ``(width, height)`` in inches.
    tight_layout : bool or dict, default=True
        If ``False`` use the default subplot parameters
        :rc:`figure.subplot.*`. If ``True`` adjust subplot parameters
        using `tight_layout` with default padding=1.08. When providing
        a dict containing the keys ``pad``, ``w_pad``, ``h_pad``, and
        ``rect``, the default `tight_layout` paddings will be
        overridden.

    Returns
    -------
    fig : matplotlib figure
        Figure containing the seasonal subseries curves.
    axs : numpy.ndarray
        Array of matplotlib axes.
    """
    rides = load_rides(filepath)
    rides_hourly = rides.resample('H').count()
    # Reshape hourly data so that each column is a 'season' (hour of
    # the day) and each row is a day of the year.
    rides_hourly_long = pd.DataFrame(
        {'rides': rides_hourly, 'hourofday': rides_hourly.index.hour,
         'dayofyear': rides_hourly.index.dayofyear})
    rides_hourly_wide = rides_hourly_long.pivot(
        index='dayofyear', columns='hourofday')

    fig, axs = plt.subplots(2, 12, sharex=True, sharey=True,
                            figsize=figsize, tight_layout=tight_layout)
    for hour, ax in zip(range(24), axs.flat):
        # Access the column corresponding to the hour of the day.
        rides_hour = rides_hourly_wide[('rides', hour)]
        # 7-day rolling average rides per hour.
        ax.plot(rides_hour.rolling(7).mean(), '-', color='#E24A33')
        # Mean rides per hour (season) across time span.
        num_days = len(rides_hour)
        ax.plot(rides_hour.index, [rides_hour.mean()] * num_days, 'k')
        # Customizing plot labels.
        ax.set_title(hour)
    for ax in axs[:, 0]:
        ax.set_ylabel('rides')
    for ax in axs[:, -1]:
        ax.yaxis.set_label_position('right')
        ax.set_ylabel('rides')
        ax.tick_params(
            left=False, labelleft=False,
            right=True, labelright=True)
    for ax in axs[-1]:
        ax.set(xticks=[91, 182, 274],
               xticklabels=['Apr', 'Jul', 'Oct'])
    fig.suptitle('Rides By Hour Of The Day', size='xx-large')
    return fig, axs


def plot_daily_subseries(
    filepath:str, figsize: Tuple[float, float] = (16, 4.5),
    tight_layout: bool = False
) -> Tuple['matplotlib.figure.Figure', 'matplotlib.axes.Axes']:
    """
    Plot seasonal subseries for daily rides data.

    Parameters
    ----------
    filepath : str, default='../data/taxi.csv'
        String path of csv file.
    figsize : 2-tuple of floats, default=(16, 4.5)
        Figure dimension ``(width, height)`` in inches.
    tight_layout : bool or dict, default=False
        If ``False`` use the default subplot parameters
        :rc:`figure.subplot.*`. If ``True`` adjust subplot parameters
        using `tight_layout` with default padding=1.08. When providing
        a dict containing the keys ``pad``, ``w_pad``, ``h_pad``, and
        ``rect``, the default `tight_layout` paddings will be
        overridden.

    Returns
    -------
    fig : matplotlib figure
        Figure containing the seasonal subseries curves.
    axs : numpy.ndarray
        Array of matplotlib axes.
    """
    rides = load_rides(filepath)
    rides_daily = rides.resample('D').count()
    # Reshape daily data so that each column is a 'season' (day of the
    # week) and each row is a week of the year.
    rides_daily_long = pd.DataFrame(
        {'rides': rides_daily,
         'dayofweek': rides_daily.index.dayofweek,
         'weekofyear': rides_daily.index.isocalendar().week})
    rides_daily_wide = rides_daily_long.pivot(
        index='weekofyear', columns='dayofweek')

    daysofweek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    fig, axs = plt.subplots(1, 7, sharey=True, figsize=figsize,
                            tight_layout=tight_layout)
    for day_idx, day, ax in zip(range(7), daysofweek, axs.flat):
        # Access the column corresponding to the day of the week.
        rides_day = rides_daily_wide[('rides', day_idx)]
        # Daily rides.
        ax.plot(rides_day)
        # Mean rides per day (season) across time span.
        num_weeks = len(rides_day)
        ax.plot(rides_day.index, [rides_day.mean()] * num_weeks, 'k')
        # Customizing plot labels.
        if day == 'Mon':
            ax.set_ylabel('Rides')
        if day == 'Thu':
            ax.set_xlabel('Date', size='large')
        if day == 'Sun':
            ax.yaxis.set_label_position('right')
            ax.set_ylabel('Rides')
            ax.tick_params(
                left=False, labelleft=False,
                right=True, labelright=True)
        if day not in ['Mon', 'Sun']:
            ax.tick_params(left=False, labelleft=False)
        ax.set(title=day, xticks=[14, 22, 31, 40],
               xticklabels=['Apr', 'Jun', 'Aug', 'Oct'])
    fig.suptitle('Rides By Day Of The Week', size='xx-large')
    return fig, axs


def main(filepath:str, dir_out: str = '') -> None:
    """
    Encapsulates the logic for running `time_series_arima.py` as a
    script.

    Parameters
    ----------
    filepath : str
        Data file path.
    dir_out : str, default=''
        Directory to save plots.

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

    plt.style.use('ggplot')

    plot_hourly_subseries(filepath)
    now = datetime.now().strftime('%Y-%m-%dT%H%M%S')
    file = dir_out + f'hourly-subseries_{now}.png'
    plt.savefig(Path(file), dpi=300)
    print(f'figure saved to {file}')

    plot_daily_subseries(filepath)
    now = datetime.now().strftime('%Y-%m-%dT%H%M%S')
    file = dir_out + f'daily-subseries_{now}.png'
    plt.savefig(Path(file), dpi=300)
    print(f'figure saved to {file}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file_in', help='data file')
    parser.add_argument(
        '--dir_out', default='',
        help='directory to save plots')
    args = parser.parse_args()
    main(args.file_in, args.dir_out)